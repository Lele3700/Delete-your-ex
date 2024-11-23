from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
import googleapiclient
from googleapiclient.discovery import build
from googleapiclient.errors import UnknownApiNameOrVersion
from googleapiclient.errors import HttpError

import os
from google.auth.transport.requests import Request

SCOPES = ['https://www.googleapis.com/auth/photoslibrary',
]
base_dir = os.path.dirname(os.path.abspath(__file__))  # Get the directory of the current script
credentials_path = os.path.join(base_dir, 'credentials.json')  # Join the base directory with 'backend/credentials.json'



def setup():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(credentials_path, SCOPES)
            creds = flow.run_local_server(port=8080)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    
def getalbums():
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    try:
        # Build the Google Photos Library API service
        service = build('photoslibrary', 'v1', credentials = creds, static_discovery = False)

        # List the albums in the user's Google Photos account
        results = service.albums().list(pageSize=10).execute()
        albums = results.get('albums', [])

        # If albums are found, print album details
        if not albums:
            print("No albums found.")
        else:
            print("Albums found:")
            for album in albums:
                print(f"Album title: {album['title']}, Album ID: {album['id']}")

    except HttpError as error:
        print(f"An error occurred: {error}")
    except UnknownApiNameOrVersion as e:
        print("Fetching discovery document failed:", str(e))

def download_file(file_id, access_token):
    """Download a file from Google Drive using its file ID."""
    creds = Credentials(token=access_token)
    service = build('photoslibrary', 'v3', credentials=creds, static_discovery = False)

    # Fetch file metadata
    file = service.files().get(fileId=file_id).execute()
    file_name = file['name']
    
    # Download file
    request = service.files().get_media(fileId=file_id)
    with open(file_name, 'wb') as fh:
        downloader = googleapiclient.http.MediaIoBaseDownload(fh, request)
        done = False
        while not done:
            status, done = downloader.next_chunk()
            print(f"Download progress: {int(status.progress() * 100)}%")
    print(f"File {file_name} downloaded.")

def main():
    setup()
    getalbums()
    download_file()

if __name__ == '__main__':
    main()
