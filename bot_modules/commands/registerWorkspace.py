#Discord bot command.
#Register a Notion workspace for posterior usage.

import os
import json
from bot_modules.config import jsonDatabasesRegisteredNotionPath

#TODO Defines secretToken keyword in config file.
async def registerWorkspace(context, alias, secretToken):  
    #Gets the already registered workspaces
    registers = {}
    with open(jsonDatabasesRegisteredNotionPath, "r") as openfile:
        try:
            registers = json.load(openfile)
        except json.decoder.JSONDecodeError:
            pass

    #Reads the .json file
    alreadyExists = False
    for register in registers:
        if(registers[register]['secretToken'] == secretToken):
            alreadyExists = True

    #If the secretToken doesn't exists, insert it into file.
    #If exists, gives a warning to the user.
    if not alreadyExists:
        registers[alias] = {'secretToken': secretToken}
        json_object = json.dumps(registers, indent = 2)

        with open(jsonDatabasesRegisteredNotionPath, "w") as outfile:
            outfile.write(json_object)

        await context.send("Registrado!")
    
    else:
        await context.send("Chave secreta já existe no database!")