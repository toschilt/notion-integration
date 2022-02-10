import json

from bot_modules.config import sid
from bot_modules.config import jsonGoogleKey

from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ['https://www.googleapis.com/auth/drive']
DOCUMENT_ID = "1S1rvPpXDTX2DXbaCSqlGnOb5IQB80D47Nie1D1D4AIw"

@sid.event
async def on_message(message):
    if not message.guild:
        #Message comes from DM message.  

        googleCredentials = service_account.Credentials.from_service_account_file(jsonGoogleKey, scopes=SCOPES)
        service = build('docs', 'v1', credentials=googleCredentials)

        requests = [
            {
                'insertText': {
                    'location': {
                        'index': 1,
                    },
                    'text': "text1"
                }
            },
                    {
                'insertText': {
                    'location': {
                        'index': 6,
                    },
                    'text': "text2"
                }
            },
                    {
                'insertText': {
                    'location': {
                        'index': 11,
                    },
                    'text': "text3"
                }
            },
        ]
        
        result = service.documents().batchUpdate(
            documentId=DOCUMENT_ID, body={'requests': requests}).execute()

    await sid.process_commands(message)