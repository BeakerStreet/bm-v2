import boto3
import os
import boto3.session as s3
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

def authenticate_gdrive():
    # to do: init gdrive auth
    return drive

def download_file_from_gdrive(drive, file_id, dest_path):
    file = drive.CreateFile({'id': file_id})
    file.GetContentFile(dest_path)



def main():
    s3 = boto3.client('s3')

    drive = authenticate_gdrive()
    print("auth successful")
    
    # sort access
    # folder dict: {'name': name, 'id': id}, 
    # for name, id in dict: 
    #   for image_filename in id:
    #       print(image_filename)
    #       input() just take a look

    '''
    Plan:

    - create the labeling sequence in dataset:
        > video -> images (done)
        > images -> build orders
        > build orders -> dataset.json
        > (opt) plot build orders 
    - create the mod prediction sequence in bmv2:
        > build orders -> PseudoYields
        > PseudoYields -> mod code
    - ai-generate some model tutorials: 
        > a multi-modal input that predicts the build order data in one shot
        > a transformer taking the images, generating a bunch of text, and outputting the mod code directly
    '''


if __name__ == "__main__":
    main()