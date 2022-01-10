#Discord bot command.
#Register a Notion workspace for posterior usage.

import os
import json
from bot_modules.config import jsonDatabasesRegisteredNotionPath
from bot_modules.utils import readJSONFileAsDict

#TODO Defines secretToken keyword in config file.
#TODO Register workspace that already exists overwrites the json file. Ask user if that is intended.
async def registerWorkspace(context, alias, secretToken):  
    #Gets the already registered workspaces
    registers = readJSONFileAsDict(jsonDatabasesRegisteredNotionPath)
    
    alreadyExists = False
    if registers is not None:
        #Reads the .json file
        for register in registers:
            if(registers[register]['secretToken'] == secretToken):
                alreadyExists = True
    else:
        registers = {}

    #If the secretToken doesn't exists, insert it into file.
    #If exists, gives a warning to the user.
    if not alreadyExists:
        registers[alias] = {'secretToken': secretToken,
                            'databases': {}}
        json_object = json.dumps(registers, indent = 2)

        with open(jsonDatabasesRegisteredNotionPath, "w") as outfile:
            outfile.write(json_object)

        await context.send("Registrado!")
    
    else:
        await context.send("Chave secreta já existe no registro interno!")