#Discord bot command.
#Returns the tasks in the Notion workspace.

import json
from bot_modules.config import jsonDatabasesRegisteredNotionPath

from bot_modules.notion_modules import NotionWorkspace
from bot_modules.notion_modules import NotionDatabase

#TODO Defines secretToken keyword in config file.
#TODO Defines id keyword in config file.
#TODO Defines database keyword in config file.
#TODO Treatment when some info not match the register.
async def retrieveTasks(context, databaseAlias):
    registers = {}
    with open(jsonDatabasesRegisteredNotionPath, "r") as openfile:
        try:
            registers = json.load(openfile)
        except json.decoder.JSONDecodeError:
            pass

    #TODO Maybe there is a more elegant way to do this.
    #Reads the .json file
    targetWorkpaceData = {}
    targetDatabaseData = {}
    for register in registers:
        #Gets all the databases in a workspace.
        workspace = registers[register]
        databases = workspace["databases"]

        for database in databases:
            #For a single database, checks if it was already registered.
            if(database == databaseAlias):
                targetWorkpaceData = {k: workspace[k] for k in set(list(workspace)) - set(["databases"])}
                targetDatabaseData = databases[database]
                break

    workspaceObject = NotionWorkspace.NotionWorkspace(targetWorkpaceData["secretToken"])
    databaseObject = workspaceObject.addDatabase(databaseAlias, targetDatabaseData["id"])
    
    formattedTable = databaseObject.getDatabaseDataToTablePrint()

    await context.send(formattedTable)