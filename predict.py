import sagemaker
from sagemaker import KMeans
import numpy as np
import argparse

from src.dataset import Dataset

def train():
    '''
    Train the model
    '''
    
    dataset = Dataset()
    print("Dataset loaded")


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


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Train, deploy, or predict using the model.")
    parser.add_argument("action", choices=["train", "deploy", "predict"], help="Action to perform")
    parser.add_argument("--data", type=str, help="Data for prediction")

    args = parser.parse_args()

    if args.action == "train":
        train()
    elif args.action == "deploy":
        deploy()
    elif args.action == "predict":
        if args.data:
            predict(args.data)
        else:
            print("Please provide data for prediction using --data")
