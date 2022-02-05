#Discord bot command.
#Set a special database for specific usage.

import json
from bot_modules.config import jsonDatabasesRegisteredNotionPath
from bot_modules.config import jsonSpecialDatabases
from bot_modules.utils import readJSONFileAsDict

#TODO Check if the databaseAlias exists or let the user select from a list of databases
#TODO Check if the specialFunction is valid
async def setSpecialDatabase(context, databaseAlias, specialFunction):
    #Gets the already registered workspaces
    workspaces = readJSONFileAsDict(jsonDatabasesRegisteredNotionPath)

    targetWorkspace = None
    targetDatabase = None

    for workspace in workspaces:
        databases = workspaces[workspace]["databases"]
        for database in databases:
            if database == databaseAlias:
                targetWorkspace = workspace
                targetDatabase = database
                break

    specialDatabases = readJSONFileAsDict(jsonSpecialDatabases)
    if specialDatabases is None:
        specialDatabases = {}
    
    if targetWorkspace is not None and targetDatabase is not None:
        specialDatabases[specialFunction] = {"workspace": targetWorkspace, 
                                             "database": targetDatabase}
        json_object = json.dumps(specialDatabases, indent = 2)

        with open(jsonSpecialDatabases, "w") as outfile:
            outfile.write(json_object)

        await context.send("Função especial registrada!")
    
    else:
        await context.send("Workspace/database informado não foi registrado anteriormente")