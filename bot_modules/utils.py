#TODO Implement log function to mantain track of the commands.
#TODO Implement .json manipulations

import os
import json
from bot_modules.config import *
from bot_modules.config import jsonPermissions
from bot_modules.config import jsonUsersRegisteredPath

#Reads the JSON file as a python dictionary
def readJSONFileAsDict(path):
    data = {}
    isEmpty = False
    with open(path, "r") as openfile:
        #Checking if the file is empty
        openfile.seek(0, os.SEEK_END)
        if openfile.tell():
            openfile.seek(0)
        else:
            isEmpty = True

        #If is not empty, try to read.
        #If gets an exception, adds warning to log and returns nothing.
        if not isEmpty:
            try:
                data = json.load(openfile)
            except json.decoder.JSONDecodeError:
                #TODO Implement log archive here. 
                print("Erro na leitura do arquivo.")
                return None
        else:
            return None

    return data

#Check if the command can be executed by the user.
async def checkPermission(context, command):
    permissionList = readJSONFileAsDict(jsonPermissions)
    targetPermission = permissionList[command]

    usersRegistered = readJSONFileAsDict(jsonUsersRegisteredPath)
    targetUser = usersRegistered[str(context.author.id)]
    targetUserRoles = targetUser["roles"]

    if "everyone" in targetPermission or targetPermission in targetUserRoles:
        return True
    else:
        await context.send("Permissão negada!")
        return False