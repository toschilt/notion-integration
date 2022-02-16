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

    #Gets the content of a field with "title" type. jsonData needs to be the dictionary with type info.
    def getTitleContent(self, jsonData):
        if jsonData["type"] == "title":
            return jsonData["title"][0]["text"]["content"]
        else:
            print("[getTitleContent] Tipo inválido! Precisa ser do tipo 'title'")
            return None

    #Gets the content of a field with "rich_text" type. jsonData needs to be the dictionary with type info.
    def getRichTextContent(self, jsonData):
        if jsonData["type"] == "rich_text":
            return jsonData["title"][0]["text"]["content"]
        else:
            print("[getRichTextContent] Tipo inválido! Precisa ser do tipo 'rich_text'")
            return None

    #Gets the content of a field with "number" type. jsonData needs to be the dictionary with type info.
    def getNumberContent(self, jsonData):
        if jsonData["type"] == "number":
            return str(jsonData["number"])
        else:
            print("[getNumberContent] Tipo inválido! Precisa ser do tipo 'number'")
            return None

    #Gets the content of a field with "select" type. jsonData needs to be the dictionary with type info.
    def getSelectContent(self, jsonData):
        if jsonData["type"] == "select":
            return jsonData["select"]["name"]
        else:
            print("[getSelectContent] Tipo inválido! Precisa ser do tipo 'select'")
            return None

    #Gets the content of a field with "multi_select" type. jsonData needs to be the dictionary with type info.
    def getMultiSelectContent(self, jsonData):
        if jsonData["type"] == "multi_select":
            tags = []
            for tag in jsonData["multi_select"]:
                tags.append(tag["name"])
                
            #Checks if it is empty. 
            if tags:
                return tags
            else:
                return None
        else:
            print("[getMultiSelectContent] Tipo inválido! Precisa ser do tipo 'multi_select'")
            return None

    #Gets the content of a field with "date" type. jsonData needs to be the dictionary with type info.
    #TODO Implement finish date
    def getDateContent(self, jsonData):
        if jsonData["type"] == "date":
            return jsonData["date"]["start"]
        else:
            print("[getDateContent] Tipo inválido! Precisa ser do tipo 'date'")
            return None

    #Gets the content of a field with "email" type. jsonData needs to be the dictionary with type info.
    def getEmailContent(self, jsonData):
        if jsonData["type"] == "email":
            return jsonData["email"]
        else:
            print("[getEmailContent] Tipo inválido! Precisa ser do tipo 'email'")
            return None

    #Gets the content of a field with "phone_number" type. jsonData needs to be the dictionary with type info.
    def getPhoneNumberContent(self, jsonData):
        if jsonData["type"] == "phone_number":
            return jsonData["phone_number"]
        else:
            print("[getPhoneNumberContent] Tipo inválido! Precisa ser do tipo 'phone_number'")
            return None

    #Gets the content of a field with "person" type. jsonData needs to be the dictionary with type info.
    #TODO Insert new person info.
    def getPeopleContent(self, jsonData):
        if jsonData["type"] == "people":
            people = []
            
            #Gets the name of all people.
            for person in jsonData["people"]:
                people.append(person["name"])

            if people:
                return people
            else:
                return None
        else:
            print("[getPeopleContent] Tipo inválido! Precisa ser do tipo 'people'")
            return None

    #Gets the data from a ID database and returns only the field required.
    def verticalSearch(self, primaryKeyFieldName, primaryKeyValue):
        allData = self.getDatabaseDataInJSON()["results"]

        #for result in allData:
        #    if result["propert"]
        

    #Gets the data from a ID database and formats it to a human-friendly table
    #TODO Super ugly - needs refactoring
    #TODO Enable table customization
    #TODO Get file and relation infos
    def getDatabaseDataToTablePrint(self):
        response = self.getDatabaseDataInJSON()
        tableRows = response["results"]

        strLoad = ''

        #Gets the table header (properites names)
        for column in tableRows[0]["properties"]:
            strLoad = strLoad + column
            strLoad = strLoad + " | "

        strLoad = strLoad + "\n"

        for row in tableRows:
            #Gets all properties of a single entry.
            columns = row["properties"]

            for prop in columns:
                #Gets info about a single property.
                propInfo = columns[prop]
                propType = propInfo["type"]
                propValue = None

                if propType == "title":
                    propValue = self.getTitleContent(propInfo)
                elif propType == "rich_text":
                    propValue = self.getRichTextContent(propInfo)
                elif propType == "number":
                    propValue = self.getNumberContent(propInfo)
                elif propType == "select":
                    propValue = self.getSelectContent(propInfo)
                elif propType == "multi_select":
                    selections = self.getMultiSelectContent(propInfo)
                elif propType == "date":
                    propValue = self.getDateContent(propInfo)
                elif propType == "email":
                    propValue = self.getEmailContent(propInfo)
                elif propType == "phone_number":
                    propValue = self.getPhoneNumberContent(propInfo)
                elif propType == "people":
                    propValue = self.getPeopleContent(propInfo)[0]

                if(propValue != None):
                    strLoad = strLoad + str(propValue)
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
               