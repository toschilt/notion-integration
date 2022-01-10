#Discord bot command.
#Replicate the data from one Notion database into another.

import json
from bot_modules.utils import readJSONFileAsDict
from bot_modules.config import jsonDatabasesRegisteredNotionPath

from bot_modules.notion_modules import NotionAutomations
from bot_modules.notion_modules import NotionWorkspace
from bot_modules.notion_modules import NotionDatabase

#TODO Other commands use this same function. Generalize for all of them.
def constructNotionComponents(registers, databaseAlias):
    if registers is not None:
        #Reads the .json file
        targetWorkpaceData = {}
        targetDatabaseData = {}
        databaseFound = False
        for register in registers:
            #Gets all the databases in a workspace.
            workspace = registers[register]
            databases = workspace["databases"]

            for database in databases:
                #For a single database, checks if it was already registered.
                if(database == databaseAlias):
                    targetWorkpaceData = {k: workspace[k] for k in set(list(workspace)) - set(["databases"])}
                    targetDatabaseData = databases[database]
                    databaseFound = True
                    break

        if databaseFound:
            workspaceObject = NotionWorkspace.NotionWorkspace(targetWorkpaceData["secretToken"])
            databaseObject = workspaceObject.addDatabase(databaseAlias, targetDatabaseData["id"])
            return workspaceObject, databaseObject

        else:
            return None, None
    else:
        return None, None

async def replicateDatabase(context, databaseFromAlias, databaseToAlias):
    registers = readJSONFileAsDict(jsonDatabasesRegisteredNotionPath)

    workspaceFromObject, databaseFromObject = constructNotionComponents(registers, databaseFromAlias)
    workspaceToObject, databaseToObject = constructNotionComponents(registers, databaseToAlias)

    if databaseFromObject is not None and databaseToObject is not None:
        NotionAutomations.copyEntriesBetweenDatabases(databaseFromObject, databaseToObject)
        await context.send("Entradas do database " + databaseFromAlias + " copiadas para o database " + databaseToAlias + "!")
    
    else:
        await context.send("Um dos databases não está cadastrado ou é inválido!")