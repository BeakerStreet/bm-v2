import boto3
import sagemaker
import pandas as pd

class Dataset:
    def __init__(self, bucket: str):
        self.bucket = bucket
        self.role = self.get_role()
        self.raw_text = self.download_data()
        self.cleaned_text = None
        self.input_labels = None
        self.output_labels = None
    
    def get_role(self):
        return sagemaker.get_execution_role()
    
    def download_data(self):
        s3 = boto3.client('s3')
        response = s3.list_objects_v2(Bucket=self.bucket, Prefix='data/')
        data = []

        # add download instructions when you know the structure of the files
        
        return data
    
    def clean_data(self):
        cleaned_data = pd.DataFrame()

        # add cleaning
        # split text into columns? maybe?

        self.cleaned_text = cleaned_data

        return cleaned_data

    def label(self, text: list) -> pd.DataFrame:
        # add labelling
        
        pass