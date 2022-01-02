from notion_modules import NotionConstants
import requests
import json

#Encapsule all the comunication within a specific Notion database.
class NotionDatabase:

    #Constructor. Needs the private key of the workspace
    #and the ID of the Notion database.
    def __init__(self, privateKey, id):
        self.privateKey = privateKey
        self.id = id

    #Gets the sctructural info from a ID database. 
    def retrieveDatabase(self):
        header = {"Authorization":self.privateKey, 
                  "Notion-Version":NotionConstants.notionVersion}

        response = requests.get(NotionConstants.base_url_db + self.id,
                                headers = header)

        return response

    #Gets the structural info from a ID database and converts to JSON.
    def retrieveDatabaseInJSON(self):
        response = self.retrieveDatabase()
        return response.json()

    #Gets the structural info from a ID database and converts to printable JSON.
    def retrieveDatabaseToPrint(self, q_indent = 2):
        response = self.retrieveDatabaseInJSON()
        return json.dumps(response, indent = q_indent)

    #Gets the data from the database.
    def getDatabaseData(self):
        header = {"Authorization":self.privateKey, 
                  "Notion-Version":NotionConstants.notionVersion,
                  "Content-Type":"application/json"}

        response = requests.post(NotionConstants.base_url_db + self.id + "/query",
                                 headers = header)

        return response

    #Gets the data from a ID database and converts to JSON.
    def getDatabaseDataInJSON(self):
        response = self.getDatabaseData()
        return response.json()

    #Gets the data from a ID database and converts to printable JSON.
    def getDatabaseDataToPrint(self, q_indent = 2):
        response = self.getDatabaseDataInJSON()
        return json.dumps(response, indent = q_indent)
    
    #Creates and insert a new page in the database.
    #Needs a python dictionary to be JSON serialized.
    def insertEntry(self, dataJSON):
        #TODO Generalize header definition?
        header = {"Authorization":self.privateKey, 
                  "Notion-Version":NotionConstants.notionVersion,
                  "Content-Type":"application/json"}

        response = requests.post(NotionConstants.base_url_page,
                                 headers = header,
                                 data = json.dumps(dataJSON))

        return response
               