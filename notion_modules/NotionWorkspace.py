from notion_modules import NotionConstants
from notion_modules.NotionDatabase import NotionDatabase
import requests
import json

#Encapsule all the comunication with a specific Notion workspace.
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