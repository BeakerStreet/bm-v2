import boto3



def main():
    s3 = boto3.client('s3')
    s3.download_file('bucket-name', 'key', 'filename')
    