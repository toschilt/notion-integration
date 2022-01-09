#Discord bot command.
#Register the correspondence in Discord and Notion indentifiers.

import json

from bot_modules.notion_modules.NotionWorkspace import NotionWorkspace

from bot_modules.config import jsonUsersRegisteredPath
from bot_modules.config import jsonDatabasesRegisteredNotionPath

#TODO Other commands use this same function. Generalize for all of them.
def constructWorkspace(workspaceAlias):
    jsonData = {}
    with open(jsonDatabasesRegisteredNotionPath, "r") as openfile:
        try:
            jsonData = json.load(openfile)
        except json.decoder.JSONDecodeError:
            pass

    targetWorkspaceData = {}
    for workspace in jsonData:
        if workspace == workspaceAlias:
            targetWorkspaceData = jsonData[workspace]
            break

    workspaceObject = NotionWorkspace(targetWorkspaceData["secretToken"])
    
    return workspaceObject

#TODO define Discord and Notion keyword in config file.
#TODO Defines id and name keyword in config file.
#Compound names must be within quotes.
async def registerUser(context, notionUsername, notionWorkspace):
    #Gets the already registered users
    users = {}
    with open(jsonUsersRegisteredPath, "r") as openfile:
        try:
            users = json.load(openfile)
        except json.decoder.JSONDecodeError:
            pass

    discordID = context.author.id
    discordName = context.author.name

    workspaceObject = constructWorkspace(notionWorkspace)
    notionUsers = workspaceObject.getAllUsers().json()

    notionID = None
    notionName = None
    for user in notionUsers["results"]:
        if(user["name"] == notionUsername):
            notionName = user["name"]
            notionID = user["id"]
            break
        
    #Uses the user Discord ID as primary key.
    users[discordID] = {"discord": {"id": discordID,
                                    "name": discordName},
                        "notion":  {"id": notionID,
                                    "name": notionName}}

    with open(jsonUsersRegisteredPath, "w") as outfile:
        outfile.write(json.dumps(users, indent = 2))
        await context.send("Registrado!")

    #print(context.author.name)
    #print(context.author.public_flags)
    #print(context.author.dm_channel)
    #print(context.author.id)
    #print(context.author.mention)
    #print(context.author.roles)
    #await context.send("Debugging, " + context.author.mention)