#Discord bot command.
#Replicate the data from one Notion database into another.

import json
from bot_modules.config import jsonDatabasesRegisteredNotionPath

from bot_modules.notion_modules import NotionAutomations
from bot_modules.notion_modules import NotionWorkspace
from bot_modules.notion_modules import NotionDatabase

#TODO Other commands use this same function. Generalize for all of them.
def constructNotionComponents(jsonData, databaseAlias):
    #TODO Maybe there is a more elegant way to do this.
    #Reads the .json file
    targetWorkpaceData = {}
    targetDatabaseData = {}
    for register in jsonData:
        #Gets all the databases in a workspace.
        workspace = jsonData[register]
        databases = workspace["databases"]

        for database in databases:
            #For a single database, checks if it was already registered.
            if(database == databaseAlias):
                targetWorkpaceData = {k: workspace[k] for k in set(list(workspace)) - set(["databases"])}
                targetDatabaseData = databases[database]
                break

    workspaceObject = NotionWorkspace.NotionWorkspace(targetWorkpaceData["secretToken"])
    databaseObject = workspaceObject.addDatabase(databaseAlias, targetDatabaseData["id"])
    
    return workspaceObject, databaseObject

async def replicateDatabase(context, databaseFromAlias, databaseToAlias):
    registers = {}
    with open(jsonDatabasesRegisteredNotionPath, "r") as openfile:
        try:
            registers = json.load(openfile)
        except json.decoder.JSONDecodeError:
            pass

    workspaceFromObject, databaseFromObject = constructNotionComponents(registers, databaseFromAlias)
    workspaceToObject, databaseToObject = constructNotionComponents(registers, databaseToAlias)

    NotionAutomations.copyEntriesBetweenDatabases(databaseFromObject, databaseToObject)

    await context.send("Entradas do database " + databaseFromAlias + " copiadas para o database " + databaseToAlias + "!")