from notion_modules import NotionConstants
import requests
import json

#Encapsule all the comunication with a specific Notion workspace.
class NotionWorkspace:

    #Constructor. Needs the private key to the Notion Database.
    def __init__(self, key):
        self.privateKey = key

    #Gets the structural info from a ID database.
    def retrieveDatabase(self, id):
        header = {"Authorization":self.privateKey, 
                  "Notion-Version":NotionConstants.notionVersion}
        
        response = requests.get(NotionConstants.base_url_db + id,
                                headers = header)

        return response

    #Gets the structural info from a ID database and converts to JSON.
    def retrieveDatabaseInJSON(self, id):
        response = self.retrieveDatabase(id)
        return response.json()

    #Gets the structural info from a ID database and converts to printable JSON.
    def retrieveDatabaseToPrint(self, id, q_indent = 2):
        response = self.retrieveDatabaseInJSON(id)
        return json.dumps(response, indent = q_indent)

    #Gets the data from the database.
    def getDatabaseData(self, id):
        header = {"Authorization":self.privateKey, 
                  "Notion-Version":NotionConstants.notionVersion,
                  "Content-Type":"application/json"}

        response = requests.post(NotionConstants.base_url_db + id + "/query",
                                 headers = header)

        return response

    #Gets the data from a ID database and converts to JSON.
    def getDatabaseDataInJSON(self, id):
        response = self.getDatabaseData(id)
        return response.json()

    #Gets the data from a ID database and converts to printable JSON.
    def getDatabaseDataToPrint(self, id, q_indent = 2):
        response = self.getDatabaseDataInJSON(id)
        return json.dumps(response, indent = q_indent)