import boto3
import os
import boto3.session as s3

def main():
    s3 = boto3.client('s3')

    # Upload data/dataset.json to s3 bucket "bmv2"
    s3.upload_file('data/dataset.json', 'bmv2', 'dataset.json')

    # figure out labeling
    # large-scale data processing
    # train model
    # deploy model

if __name__ == "__main__":
    main()