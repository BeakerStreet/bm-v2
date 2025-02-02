import boto3
import os
import boto3.session as s3
from google.oauth2 import service_account
from googleapiclient.discovery import build
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

SERVICE_ACCOUNT_FILE = os.getenv('SERVICE_ACCOUNT_FILE')
SCOPES = os.getenv('SCOPES').strip("[]").replace("'", "").split(", ")

def authenticate_gdrive():
    
    # Authenticate with service account
    credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    # Build the Drive API client
    service = build('drive', 'v3', credentials=credentials)

    # Get the name of the folder
    folder_id = os.getenv('FOLDER_ID')
    folder = service.files().get(fileId=folder_id, fields='name').execute()
    folder_name = folder.get('name')

    # Return a success message
    response = f"Successfully accessed folder: {folder_name}"

    return response

def download_file_from_gdrive(drive, file_id, dest_path):
    file = drive.CreateFile({'id': file_id})
    file.GetContentFile(dest_path)



def main():
    s3 = boto3.client('s3')

    auth_response = authenticate_gdrive()
    print(auth_response)
    
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