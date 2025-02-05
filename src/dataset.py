import boto3
import sagemaker
import pandas as pd
import os

class Dataset:
    def __init__(self):
        self.bucket = os.environ['BUCKET']
        self.images = []
        self.text = []
            
    def download_data(self):
        s3 = boto3.client('s3')
        response = s3.list_objects_v2(Bucket=self.bucket, Prefix='data/')

        pass
    
    def clean_data(self):

        pass

    def gen_build_orders(self):
        '''
        Downloads dataset images
        one at a time, and from the 
        content of the image generates
        a list of the build decisions
        made by the player, organised
        by city.

        Eg. 
        build_orders = {
            "game_id": "game_001",
            "cities": [
                {
                    "city_name": "City_1",
                    "build_order": [
                        {
                            "turn": 1, 
                            "build_decision": "settler",
                            "priority": 1
                        },
                        {
                        "turn": 5, 
                        "build_decision": "warrior", 
                            "priority": 2
                        }
                    ]
                }   
            ]
        }
        '''

        pass