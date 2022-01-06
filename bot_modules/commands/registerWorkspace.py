#Discord bot command.
#Register a Notion workspace for posterior usage.

import os
import json
from bot_modules.config import storageNotionComponentsFilePath

async def registerWorkspace(context, alias, secretToken):
#   TODO Check if the component already exists in JSON file (by alias)
#   registers = {}s
#   with open(storageNotionComponentsFilePath, "r") as openfile:
#       registers = json.load(openfile)

    absolutePath = os.path.dirname(__file__)
    botModulesFolder = os.path.dirname(absolutePath)
    jsonPath = botModulesFolder + "/databases/registered_notion.json"

    workspace_dict = {
        alias: {
            "secretToken": secretToken,
        }
    }

    json_object = json.dumps(workspace_dict, indent = 2)

    with open(jsonPath, "w") as outfile:
        outfile.write(json_object)

    await context.send("Registrado!")