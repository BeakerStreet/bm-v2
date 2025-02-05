import boto3
import sagemaker
import pandas as pd

class Dataset:
    def __init__(self):
        self.bucket = os.environ['BUCKET']
        self.role = self.get_role()
        
    
    def get_role(self):
        return sagemaker.get_execution_role()
    
    def download_data(self):
        s3 = boto3.client('s3')
        response = s3.list_objects_v2(Bucket=self.bucket, Prefix='data/')

        pass
    
    def clean_data(self):

        pass

