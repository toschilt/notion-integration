#Discord bot command.
#Returns the tasks in the Notion workspace.

import json
from bot_modules.config import jsonDatabasesRegisteredNotionPath
from bot_modules.utils import readJSONFileAsDict

from bot_modules.notion_modules import NotionWorkspace
from bot_modules.notion_modules import NotionDatabase

#TODO Defines secretToken keyword in config file.
#TODO Defines id keyword in config file.
#TODO Defines database keyword in config file.
async def retrieveTasks(context, databaseAlias):
    registers = readJSONFileAsDict(jsonDatabasesRegisteredNotionPath)

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
            
            formattedTable = databaseObject.getDatabaseDataToTablePrint()

            await context.send(formattedTable)
        
        else:
            await context.send("Database informado não foi cadastrado ou tem nome inválido!")
    else:
        await context.send("Não há databases cadastrados!")