import boto3
import sagemaker
import pandas as pd
import os
import json
from openai import OpenAI
from pydantic import BaseModel
import logging
from dotenv import load_dotenv

load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class City(BaseModel):
    name: str
    current_build: str

class TurnAnalysis(BaseModel):
    turn: int
    cities: list[City]

class Dataset:
    def __init__(self):
        self.s3 = boto3.client('s3')
        self.client = OpenAI()
        self.bucket = os.environ['BUCKET']
        self.images_list = self.list_images()
        
        self.raw = []
        self.cleaned = []
            
    def list_images(self):
        '''
        Creates a list of 
        all the images currently 
        available for the 
        dataset 
        '''

        response = self.s3.list_objects_v2(Bucket=self.bucket, Prefix='data/images/')
        images_list = [{"name": obj["Key"], "url": f"https://{self.bucket}.s3.amazonaws.com/{obj['Key']}"} for obj in response.get("Contents", []) if obj["Key"] != 'data/images/']

        logging.info(f"Found {len(images_list)} images.")

        return images_list

    def process_cities(self, event):
        """
        Process the cities from the event and return a list of city dictionaries.
        """
        return [{"name": city.name, "current_build": city.current_build} for city in event.cities]

    def update_raw_text(self, raw_text, game_id, turn, cities):
        """
        Update the raw_text DataFrame with the new turn data.
        """
        turn_data = {
            "turn": turn,
            "cities": cities
        }

        if game_id in raw_text['game_id'].values:
            raw_text.loc[raw_text['game_id'] == game_id, 'turns'].values[0].append(turn_data)
        else:
            new_row = {
                "game_id": game_id,
                "build_order": [],
                "turns": [turn_data]
            }
            raw_text = pd.concat([raw_text, pd.DataFrame([new_row])], ignore_index=True)

        return raw_text

    def generate(self):
        '''
        Generates a text dataset 
        by downloading gameplay images
        one at a time and generating
        a list of the build decisions
        made by the player by city and 
        turn for CivViBuildAnalysis
        '''

        # initialize the data frame
        raw_text = pd.DataFrame({
            "game_id": [],
            "build_order": [],
            "turns": []
        })
        
        # parse the images in images_list for turn and cities data
        for idx, image in enumerate(self.images_list[:5], start=1):
            logging.info(f"Processing image {idx} of {len(self.images_list)}, filename: {image['name']}")
            game_id = image['name'][:25]

            event = self.getTurnAnalysis(image)
            cities = self.process_cities(event)
            
            # Update raw_text with the new data
            raw_text = self.update_raw_text(raw_text, game_id, event.turn, cities)

        raw_text.to_json('data/dataset.json', orient='records', lines=True)

        return raw_text
    
    def getTurnAnalysis(self, image):
        # get the CGPT analysis
            completion = self.client.beta.chat.completions.parse(
                model="gpt-4o-2024-08-06",
                messages=[
                    {"role": "system", "content": os.environ['OPEN_AI_SYSTEM_PROMPT']},
                    {
                        "role": "user",
                        "content": [
                            {"type": "text", "text": "Return the data in the format of the TurnAnalysis class."},
                            {
                                "type": "image_url",
                                "image_url": {
                                    "url": image['url'],
                                }
                            },
                        ],
                    },
                ],
                response_format=TurnAnalysis,
            )

            # parse the completion
            event = completion.choices[0].message.parsed

            return event
