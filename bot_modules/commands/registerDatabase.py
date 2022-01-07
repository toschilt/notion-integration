#Discord bot command.
#Register a Notion database for posterior usage.

import json
from bot_modules.config import jsonDatabasesRegisteredNotionPath 

#TODO Defines databases keyword in config file.
#TODO Defines id keyword in config file.
#TODO Databases can have same alias. That's a problem when retrieving entries.
async def registerDatabase(context, databaseAlias, id, workspaceAlias):
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
        #Gets all the databases in a workspace.
        databases = registers[register]["databases"]

        for database in databases:
            #For a single database, checks if it was already registered.
            registeredID = databases[database]["id"]
            if(registeredID == id):
                alreadyExists = True

    if not alreadyExists:
        registers[workspaceAlias]["databases"][databaseAlias] = {"id": id}
        json_object = json.dumps(registers, indent = 2)

        with open(jsonDatabasesRegisteredNotionPath, "w") as outfile:
            outfile.write(json_object)

        await context.send("Registrado!")
    
    else:
        await context.send("ID do database já existe no registro interno!")