#Discord bot command.
#List the Notion workspaces previously registered.

import json
from bot_modules.config import jsonDatabasesRegisteredNotionPath
from bot_modules.utils import readJSONFileAsDict

async def listWorkspaces(context):
    #Gets the already registered workspaces
    registers = readJSONFileAsDict(jsonDatabasesRegisteredNotionPath)

    if registers is not None:
        strLoad = "Workspaces registrados: \n"
        for register in registers:
            strLoad = strLoad + register + "\n"

        await context.send(strLoad)
    else:
        await context.send("Não há workpaces registrados!")