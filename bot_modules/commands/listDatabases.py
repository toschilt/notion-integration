#Discord bot command.
#List the Notion databases previously registered in a single workspace
#also previously registered.

import json
from bot_modules.config import jsonDatabasesRegisteredNotionPath

#TODO Defines databases keyword in config file.
async def listDatabases(context, workspaceAlias):
    #Gets the already registered workspaces
    registers = {}
    isEmpty = True
    with open(jsonDatabasesRegisteredNotionPath, "r") as openfile:
        try:
            registers = json.load(openfile)
            isEmpty = False
        except json.decoder.JSONDecodeError:
            pass

    if not isEmpty:
        strLoad = "Databases registrados no workpace " + workspaceAlias + ": \n"
    
        databasesExist = False
        #TODO Maybe is a more elegant way to implement this.
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