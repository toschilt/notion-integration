#Discord bot command.
#Allows the user to awnser the end sprint message.
import json

from bot_modules.config import jsonUsersRegisteredPath
from bot_modules.config import jsonGoogleKey
from bot_modules.config import jsonSpecialDatabases
from bot_modules.config import jsonDatabasesRegisteredNotionPath

from bot_modules.utils import readJSONFileAsDict

from bot_modules.notion_modules.NotionDatabase import NotionDatabase
from bot_modules.google_modules.SprintDocument import SprintDocument

#TODO For a message send in the same day, will create a new register. Update it would be better.
async def response(context):
    #Get the target workspace and database names
    specialDatabases = readJSONFileAsDict(jsonSpecialDatabases)
    projectWorkspaceName = specialDatabases["DEF_PROJECTS"]["workspace"]
    projectDatabaseName = specialDatabases["DEF_PROJECTS"]["database"]

    #Get the info about the referred workspace and database
    allDatabases = readJSONFileAsDict(jsonDatabasesRegisteredNotionPath)
    privateKey = allDatabases[projectWorkspaceName]["secretToken"]
    projectDatabaseID = allDatabases[projectWorkspaceName]["databases"][projectDatabaseName]["id"]

    #Construct the Notion database object. 
    projectDatabase = NotionDatabase(privateKey, projectDatabaseID)
    projectsInfo = projectDatabase.getDatabaseDataInJSON()["results"]
    
    #Gets the Google Document ID from the table.
    googleDocumentID = None
    for project in projectsInfo:
        if project["properties"]["Nome"]["title"][0]["text"]["content"] == "IEEE Open":
            googleDocumentID = project["properties"]["[GD] Sprint Info"]["rich_text"][0]["text"]["content"]


    #Creates the Google Document object and uses it.
    sprintDocument = SprintDocument(jsonGoogleKey, googleDocumentID)

    users = readJSONFileAsDict(jsonUsersRegisteredPath)
    userName = users[str(context.author.id)]["notion"]["name"]

    sprintDocument.insertNewRegister(
        context.message.created_at.date(),
        userName, 
        context.message.content[3:])