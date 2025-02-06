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

def iter_img_dirs():
    root = 'data/images/' 
    dirs = ['102AztecDeity', '103MapucheDiety', '104NubiaDeity', '105SwedenDeity', '106RamsesDeity', '107AmericaDeity', '108FranceDeity', '109ArabiaDeity', '110ScythiaDeity']
    for dir in dirs:
        files = os.listdir(f"{root}{dir}")

    return files

def rn():
    root = 'data/images/' 
    dirs = ['110ScythiaDeity']
    count = 1
    for dir in dirs:
        files = os.listdir(f"{root}{dir}")

        for file in files:
            
            os.rename(f"{root}{dir}/{file}", f"{root}{dir}/{dir}_{count}.jpg")
            count += 1

def s3_ul():
    s3 = boto3.client('s3')

    root = 'data/images/' 
    dirs = ['102AztecDeity', '103MapucheDiety', '104NubiaDeity', '105SwedenDeity', '106RamsesDeity', '107AmericaDeity', '108FranceDeity', '109ArabiaDeity', '110ScythiaDeity']
    for dir in dirs:
        files = os.listdir(f"{root}{dir}")

        for file in files:
            s3.upload_file(f"data/images/{dir}/{file}", 'bmv2', f"data/images/{file}")

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

    # rn()
    # s3_ul()

    '''
    Plan:

    - create the labeling sequence in dataset:
        > create dataset.json and a labeling function for collecting build orders from screenshots (only)
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