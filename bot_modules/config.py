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



#----- BOT CONFIGURATIONS -----
jsonUsersRegisteredPath = jsonDatabasesPath + "/users.json"

#Check if the JSON user file exists. If not, create it.
if not os.path.exists(jsonUsersRegisteredPath):
    with open(jsonUsersRegisteredPath, 'w'):
        pass

#TODO Elaborate a cool description for the bot.
sid = Bot(command_prefix = "!",
          description = "")

#Calling Python scripts to define commands and events
import bot_modules.commandsDef
import bot_modules.eventsDef