#Discord bot command.
#Register the correspondence in Discord and Notion indentifiers.

import json

from bot_modules.notion_modules.NotionWorkspace import NotionWorkspace

from bot_modules.config import jsonUsersRegisteredPath
from bot_modules.config import jsonDatabasesRegisteredNotionPath

from bot_modules.utils import readJSONFileAsDict

#TODO Other commands use this same function. Generalize for all of them.
def constructWorkspace(workspaceAlias):
    jsonData = readJSONFileAsDict(jsonDatabasesRegisteredNotionPath)
    
    if jsonData is not None:
        targetWorkspaceData = {}

        for workspace in jsonData:
            if workspace == workspaceAlias:
                targetWorkspaceData = jsonData[workspace]
                break

        if targetWorkspaceData:
            workspaceObject = NotionWorkspace(targetWorkspaceData["secretToken"])
            return workspaceObject
        else:
            return None

    else:
        return None

#TODO define Discord and Notion keyword in config file.
#TODO Defines id and name keyword in config file.
#TODO Explicit in help that compound names must be within quotes.
async def registerUser(context, notionUsername, notionWorkspace):
    #Gets the already registered users
    users = readJSONFileAsDict(jsonUsersRegisteredPath)

    if users is None:
        users = {}

    discordID = context.author.id
    discordName = context.author.name

    workspaceObject = constructWorkspace(notionWorkspace)    
    if workspaceObject is not None:
        notionUsers = workspaceObject.getAllUsers().json()

        notionID = None
        notionName = None
        for user in notionUsers["results"]:
            if(user["name"] == notionUsername):
                notionName = user["name"]
                notionID = user["id"]
                break
    
        #Checks if the Notion info is valid
        if notionID is not None and notionName is not None:
    
            #Uses the user Discord ID as primary key.
            users[discordID] = {"discord": {"id": discordID,
                                            "name": discordName},
                                "notion":  {"id": notionID,
                                            "name": notionName}}

            with open(jsonUsersRegisteredPath, "w") as outfile:
                outfile.write(json.dumps(users, indent = 2))
                
            await context.send("Registrado!")
        
        else:
            await context.send("Não encontrei esse nome no workspace do Notion fornecido!")
    else:
        await context.send("O nome do workspace do Notion não está cadastado/é inválido!")


    #Testing - clean later
    #print(context.author.name)
    #print(context.author.public_flags)
    #print(context.author.dm_channel)
    #print(context.author.id)
    #print(context.author.mention)
    #print(context.author.roles)
    #await context.send("Debugging, " + context.author.mention)