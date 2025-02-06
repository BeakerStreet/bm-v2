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

class Turn(BaseModel):
    turn: int
    cities: list[City]

class CivViBuildAnalysis(BaseModel):
        '''

        Data structure for the raw dataset
        generated by LLM from a gameplay
        screenshot, following the structure
        of the prompting in Dataset.generate()
        
        Eg. 
        build_orders = {
            "game_id": "game_001",
            "build_order": [],
            "turns": [
                {
                    "turn": 1,
                    "cities": [
                        {
                            "name": "City_1",
                            "current_build": "Settler"
                        }
                    ]
                }   
            ]
        }

        '''

        game_id: str
        build_order: list[str]
        turns: list[Turn]

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

    def generate(self):
        '''
        Generates a text dataset 
        by downloading gameplay images
        one at a time and generating
        a list of the build decisions
        made by the player by city and 
        turn for CivViBuildAnalysis
        '''

        raw_text = []
        
        # Open the file once and write the opening bracket
        with open('data/raw_text.json', 'w') as f:
            f.write('[\n')

            for idx, image in enumerate(self.images_list[:2], start=1):
                logging.info(f"Processing image {idx} of {len(self.images_list)}")
                completion = self.client.beta.chat.completions.parse(
                    model="gpt-4o-2024-08-06",
                    messages=[
                        {"role": "system", "content": os.environ['OPEN_AI_SYSTEM_PROMPT']},
                        {
                            "role": "user",
                            "content": [
                                {"type": "text", "text": "Return the data in the format of the CivViBuildAnalysis class."},
                                {
                                    "type": "image_url",
                                    "image_url": {
                                        "url": image['url'],
                                    }
                                },
                            ],
                        },
                    ],
                    response_format=CivViBuildAnalysis,
                )

                event = completion.choices[0].message.parsed

                # Write each JSON object, adding a comma before each except the first
                if idx > 0:
                    f.write(',\n')
                json.dump(event.dict(), f, indent=4)

                raw_text.append(event)

            # Write the closing bracket
            f.write('\n]')

        return raw_text
