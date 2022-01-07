#Discord bot command.
#List the Notion workspaces previously registered.

import json
from bot_modules.config import jsonDatabasesRegisteredNotionPath

async def listWorkspaces(context):
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
        strLoad = "Workspaces registrados: \n"
        for register in registers:
            strLoad = strLoad + register + "\n"

        await context.send(strLoad)
    else:
        await context.send("Não há workpaces registrados!")