from sagemaker.processing import ScriptProcessor, ProcessingInput, ProcessingOutput
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import string
import pandas as pd
class Dataset:
    def __init__(self, bucket: str):
        self.bucket = bucket
        self.role = self.get_role()
        self.raw = self.download_data()
        self.cleaned = self.clean_data()
        self.labelled = pass
    

    def get_role(self):
        return sagemaker.get_execution_role()
    
    def download_data(self):
        s3 = boto3.client('s3')
        file_name = 'dataset.json'
        s3.download_file(self.bucket, f'data/{file_name}', file_name)
        
        with open(file_name, 'r') as f:
            data = f.read()
        
        return data
    
    def clean_data(self):
        cleaned_data = pd.DataFrame()
        
        cleaned_data = cleaned_data.dropna()
        cleaned_data = cleaned_data[cleaned_data.apply(lambda row: all(key in row for key in ["turn", "actions", "game_state"]), axis=1)]
        cleaned_data = cleaned_data.applymap(lambda x: x.lower() if isinstance(x, str) else x)
        cleaned_data = cleaned_data.applymap(lambda x: ''.join(e for e in x if e.isalnum() or e.isspace()) if isinstance(x, str) else x)
                
        
        return cleaned_data
