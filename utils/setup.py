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

def gdrive_dl_files(service, folder_id):
    files = []
    results = service.files().list(
        q=f"'{folder_id}' in parents and name='frames'",
        fields="nextPageToken, files(id, name)"
    ).execute()
    frames_folder = results.get('files', [])

    if frames_folder:
        frames_folder_id = frames_folder[0]['id']
        results = service.files().list(
            q=f"'{frames_folder_id}' in parents",
            fields="nextPageToken, files(id, name)"
        ).execute()
        files = results.get('files', [])

    print(files)
    input('')

    return files

def main():
    s3 = boto3.client('s3')

    root_folder = authenticate_gdrive()
    service = gdrive_build()

    folder_ids = [
        '1yzOgg7H3KZgMwPY3MnYkW5q6P_ZG14d_', 
        '1Ey5wkDfb3M7uc_4hupmQ76l13jlIBIJ9', 
        '1aMtCPrOzGtY7ubdG-bQM_Cy3lzxwDFi4', 
        '1OrqefN-AosC29VypHZXoCMYql7Pgl0Ss',
        '1HanOq6fMx5ZADrYxQEkDeeEgCV-nQVa8', 
        '1qv70hbPqkUEf4tUlhvlk4DzVMtP05EUk',
        '1ZMcarHkELxGUDu-r1TQfx2iuMlLAR08a',
        '1mQjgrWc4X3aNqTcNoNQVlg2FcyCW3MUC',
        '1YE-7wZtAtwcvThVPBn2gu88pZdhAaIba',
        '1KebxwrPwCVsYDcPxxsS4M0BE1nZPhgtB'
    ]
    
    for folder_id in folder_ids:
        files = gdrive_dl_files(service, folder_id)

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