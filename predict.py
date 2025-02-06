import sagemaker
from sagemaker import KMeans
import numpy as np

def train():
    '''
    Train the model
    '''
    
    dataset = Dataset()
    dataset.generate()

    print(dataset.raw)

def deploy():
    '''
    Deploy the model
    '''
    
    pass

def predict(data):
    '''
    Use the model
    '''

    pass 