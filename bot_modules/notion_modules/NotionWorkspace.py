from bot_modules.notion_modules import NotionConstants
from bot_modules.notion_modules.NotionDatabase import NotionDatabase
import requests
import json

#Encapsule all the comunication within a specific Notion workspace.
class NotionWorkspace:

    #Constructor. Needs the private key to the Notion Database.
    def __init__(self, key):
        self.privateKey = key
        self.databases = {}

    #Adds a database to the Notion workspace Python structure.
    #Needs the database ID and a alias (text) to user acess.
    def addDatabase(self, alias, id):
        self.databases[alias] = NotionDatabase(self.privateKey, id)
        return self.databases[alias]

    #Gets all the users that have access to the workspace.
    def getAllUsers(self):
        header = {"Authorization":self.privateKey, 
                  "Notion-Version":NotionConstants.notionVersion}

        response = requests.get(NotionConstants.base_url_user,
                                headers = header)

        return response