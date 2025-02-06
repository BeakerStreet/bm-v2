import sagemaker
from sagemaker import KMeans
import numpy as np

from src.dataset import Dataset

def train():
    '''
    Train the model
    '''
    
    dataset = Dataset()
    print(dataset.images_list)


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