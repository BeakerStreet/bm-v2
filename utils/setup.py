import boto3
import os
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

SERVICE_ACCOUNT_FILE = os.getenv('SERVICE_ACCOUNT_FILE')
SCOPES = os.getenv('SCOPES').strip("[]").replace("'", "").split(", ")

def authenticate_gdrive():
    
    # Build the Drive API client
    service = gdrive_build()

    # Get the name of the folder
    folder_id = os.getenv('GDRIVE_ROOT_FOLDER_ID')
    folder = service.files().get(fileId=folder_id, fields='name').execute()
    folder_name = folder.get('name')

    # Return a success message
    response = f"{folder_name}/"

    return response

def gdrive_build():
    credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    service = build('drive', 'v3', credentials=credentials)

    return service

def gdrive_download_file(service, path, file):
    
    # Extract the file ID from the path
    file_id = path.split('/')[-1]
    
    # Request the file from Google Drive
    request = service.files().get_media(fileId=file_id)
    
    with open(file, 'wb') as f:
        downloader = MediaIoBaseDownload(f, request)
        done = False
        while not done:
            status, done = downloader.next_chunk()
    
    return file

def gdrive_get_folder_list(service, path):
    files = []
    folder_id = path.split('/')[-1]
    
    # List folders
    results = service.files().list(
        q="mimeType='application/vnd.google-apps.folder'",
        fields="nextPageToken, files(id, name)"
    ).execute()
    folders = results.get('files', [])

    return folders

def main():
    s3 = boto3.client('s3')

    root_folder = authenticate_gdrive()
    service = gdrive_build()
    folders = gdrive_get_folder_list(service, f"{root_folder}/training_data")
    

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