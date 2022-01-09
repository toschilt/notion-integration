#Discord bot command.
#List the Notion databases previously registered in a single workspace
#also previously registered.

import json
from bot_modules.config import jsonDatabasesRegisteredNotionPath
from bot_modules.utils import readJSONFileAsDict

#TODO Defines databases keyword in config file.
async def listDatabases(context, workspaceAlias):
    #Gets the already registered workspaces
    registers = readJSONFileAsDict(jsonDatabasesRegisteredNotionPath)

    if registers is not None:
        strLoad = "Databases registrados no workpace " + workspaceAlias + ": \n"
        
        #Checks for the target database
        databasesExist = False
        try:
            for database in registers[workspaceAlias]["databases"]:
                databasesExist = True
                strLoad = strLoad + database + "\n"
        except KeyError:
            databasesExist = False

        if databasesExist:
            await context.send(strLoad)
        else:
            await context.send("Workspace inválido ou não há databases registrados para o workspace " + workspaceAlias + "!")
    else:
        await context.send("Não há workpaces registrados!")