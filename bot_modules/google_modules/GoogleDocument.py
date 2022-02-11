import json
from tracemalloc import start

from google.oauth2 import service_account
from googleapiclient.discovery import build

#Encapsules all the comunication within a specific Google document.
class GoogleDocument:

    #Constructor. Needs the path to the json credentials file
    #and the ID of the Google document.
    #TODO Scope array is hardcoded. I don't see a reason why it should not.
    def __init__(self, jsonCredentials, documentID):
        self.scopes = ['https://www.googleapis.com/auth/drive']
        self.documentID = documentID

        credentials = service_account.Credentials.from_service_account_file(
            jsonCredentials, scopes = self.scopes)
        
        self.service = build('docs', 'v1', credentials = credentials)
        self.requests = []

    #Gets the entire document structure and contents.
    def retrieveAllDocumentAsJSON(self):
        return self.service.documents().get(
            documentId = self.documentID).execute()
        
    #Gets the entire document structure and formats it to human visualization.
    def retrieveAllDocumentToPrint(self, q_indent = 2):
        return json.dumps(
            self.retrieveAllDocumentAsJSON(), 
            indent = q_indent)

    #Insert some text at a specific index of the document.
    #The method DO NOT execute the changes.
    def insertTextAtIndex(self, text, startIndex):
        self.requests.append({
            'insertText': {
                'location': {
                    'index': startIndex,
                    },
                'text': str(text)
                }
            }
        )

    #Execute the batchUpdates changes and cleans the requests dict.
    def executeChanges(self):
        result = self.service.documents().batchUpdate(
            documentId=self.documentID, 
            body={'requests': self.requests}).execute()

        self.requests = []
        
        return result
