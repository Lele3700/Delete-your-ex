from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import os
from google.auth.transport.requests import Request

SCOPES = ['https://www.googleapis.com/auth/photoslibrary.readonly',
          'https://www.photoslibrary.googleapis.com',
          'photospicker.googleapis.com'
]

def main():
    # Load credentials
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('backend/credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    # Use API
    service = build('photoslibrary', 'v1', credentials=creds)
    results = service.mediaItems().list().execute()
    for item in results.get('mediaItems', []):
        print(item['filename'])

if __name__ == '__main__':
    main()
