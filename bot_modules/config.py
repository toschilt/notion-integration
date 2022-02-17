import json
import os
from discord.ext.commands import Bot


#----- BASIC PATH CONFIGURATION -----
botModulesPath = os.path.dirname(__file__)
jsonDatabasesPath = botModulesPath + "/databases"

#Create the database folder, if it not exist.
if not os.path.exists(jsonDatabasesPath):
    os.mkdir(jsonDatabasesPath)



#----- NOTION CONFIGURATIONS -----
jsonDatabasesRegisteredNotionPath = jsonDatabasesPath + "/registered_notion.json"

#Check if the JSON database file exists. If not, create it.
if not os.path.exists(jsonDatabasesRegisteredNotionPath):
    with open(jsonDatabasesRegisteredNotionPath, 'w'):
        pass


#----- GOOGLE INTEGRATION CONFIGURATIONS -----
googleModulesPath = botModulesPath + "/google_modules"
jsonGoogleKey = googleModulesPath + "/credentials.json"



#----- BOT CONFIGURATIONS -----
jsonCommandsAlias = jsonDatabasesPath + "/commands_alias.json"
jsonUsersRegisteredPath = jsonDatabasesPath + "/users.json"
jsonSpecialDatabases = jsonDatabasesPath + "/special_databases.json"
jsonTextOut = jsonDatabasesPath + "/textOut.json"
jsonPermissions = jsonDatabasesPath + "/permissions.json"

#Check if the JSON user file exists. If not, create it.
if not os.path.exists(jsonUsersRegisteredPath):
    with open(jsonUsersRegisteredPath, 'w'):
        pass

#Check if the JSON special databases file exists. If not, create it.
if not os.path.exists(jsonSpecialDatabases):
    with open(jsonSpecialDatabases, 'w'):
        pass



#----- BOT START -----
#TODO Elaborate a cool description for the bot.
sid = Bot(command_prefix = "!",
          description = "")

#Calling Python scripts to define commands and events
import bot_modules.commandsDef
import bot_modules.eventsDef