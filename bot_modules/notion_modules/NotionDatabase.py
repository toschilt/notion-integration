from bot_modules.notion_modules import NotionConstants
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
    def getDatabaseDataToJSONPrint(self, q_indent = 2):
        response = self.getDatabaseDataInJSON()
        return json.dumps(response, indent = q_indent)

    #Gets the data from a ID database and formats it to a
    #human-friendly table
    #TODO Super ugly - needs refactoring
    def getDatabaseDataToTablePrint(self):
        response = self.getDatabaseData()
        tableRows = response.json()["results"]
        print(json.dumps(tableRows, indent = 2))
        strLoad = ''

        #TODO Enable table customization
        #Gets the table header
        for column in tableRows[0]["properties"]:
            strLoad = strLoad + column
            strLoad = strLoad + " | "

        strLoad = strLoad + "\n"

        for row in tableRows:
            columns = row["properties"]
            for prop in columns:
                propType = columns[prop]["type"]
                propValue = None

                if propType == "title":
                    propValue = columns[prop][propType][0]["text"]["content"]
                elif propType == "rich_text":
                    propValue = columns[prop][propType][0]["text"]["content"]
                elif propType == "number":
                    propValue = str(columns[prop][propType])
                elif propType == "select":
                    propValue = columns[prop][propType]["name"]
                elif propType == "multi_select":
                    selections = columns[prop][propType]
                    values = ''
                    for option in selections:
                        values = values + option["name"]
                        values = values + ", "
                    
                    if values == '':
                        propValue = None
                    else:
                        propValue = values
                #TODO Implement finish date
                elif propType == "date":
                    propValue = columns[prop][propType]["start"]
                #TODO Implement more features in people property?
                #TODO Implement getting more than one person
                #elif propType == "people":
                #    propValue = columns[prop][propType][0]["name"]
                #TODO Implement checking all the files
                #elif propType == "files":
                #   propValue = columns[prop][propType][0]
                elif propType == "email":
                    propValue = columns[prop][propType]
                elif propType == "phone_number":
                    propValue = columns[prop][propType]

                #TODO Implement relation property

                if(propValue != None):
                    strLoad = strLoad + propValue
                else:
                    strLoad = strLoad + "null"

                strLoad = strLoad + " | "

            strLoad = strLoad + "\n"

        return strLoad
    
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
               