#Discord bot command.
#Register the correspondence in Discord and Notion indentifiers.

import json

from bot_modules.notion_modules.NotionWorkspace import NotionDatabase

from bot_modules.config import jsonUsersRegisteredPath
from bot_modules.config import jsonDatabasesRegisteredNotionPath
from bot_modules.config import jsonSpecialDatabases

from bot_modules.utils import readJSONFileAsDict

#TODO define Discord and Notion keyword in config file.
#TODO Defines keyworks in config file.
#TODO Explicit in help that the user info is always overrided.
async def registerUser(context, email):
    #Gets the special databases registered.
    #The registerUser command only runs if the needed special database is registered.
    specialDatabases = readJSONFileAsDict(jsonSpecialDatabases)
    workspaceName = None
    databaseName = None
    
    if specialDatabases is not None:
        workspaceName = specialDatabases["DEF_MEMBERS"]["workspace"]
        databaseName = specialDatabases["DEF_MEMBERS"]["database"]
        
    if workspaceName is not None and databaseName is not None:
        discordID = str(context.author.id)
        discordName = context.author.name
        
        #Gets the already registered users.
        users = readJSONFileAsDict(jsonUsersRegisteredPath)
        if users is None:
            users = {}

        #Gets the member info from Notion database.
        workspaces = readJSONFileAsDict(jsonDatabasesRegisteredNotionPath)
        workspacePrivateKey = workspaces[workspaceName]["secretToken"]
        memberDatabaseID = workspaces[workspaceName]["databases"][databaseName]["id"]

        databaseObject = NotionDatabase(workspacePrivateKey, memberDatabaseID)
        membersData = databaseObject.getDatabaseDataInJSON()

        #Iterate over every single member.
        #TODO This strategy is not optimal. For a small team, works fine.
        targetMember = None
        for member in membersData["results"]:
            if member["properties"]["E-mail"]["email"] == email:
                targetMember = member
                break
        
        #Gets the user metadata.
        memberMetaData = targetMember["properties"]["Referencia"]["people"][0]
        notionID = memberMetaData["id"]
        notionName = memberMetaData["name"]

        #Gets the projects that the member works on.
        memberProjects = []
        for project in targetMember["properties"]["Projetos"]["multi_select"]:
            memberProjects.append(project["name"])

        #Gets the roles that the member have.
        memberRoles = []
        for role in targetMember["properties"]["Cargo"]["multi_select"]:
            memberRoles.append(role["name"])

        #Compile the info in a single dictionary.
        users[discordID] = {"discord": {"id": discordID,
                                        "name": discordName},
                            "notion":  {"id": notionID,
                                        "name": notionName},
                            "roles": memberRoles,
                            "projects": memberProjects}

        #Write the info down in the file.
        with open(jsonUsersRegisteredPath, "w") as outfile:
                outfile.write(json.dumps(users, indent = 2))
                
        await context.send("Registrado!")

    else:
        await context.send("É necessário setar o database de membros com a flag DEF_MEMBERS!")