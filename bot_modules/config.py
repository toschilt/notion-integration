import json
import os
from discord.ext.commands import Bot

#Path basic configuration
botModulesPath = os.path.dirname(__file__)
jsonDatabasesPath = botModulesPath + "/databases"

#Create the database folder, if it not exist.
if not os.path.exists(jsonDatabasesPath):
    os.mkdir(jsonDatabasesPath)

#Notion configurations
jsonDatabasesRegisteredNotionPath = jsonDatabasesPath + "/registered_notion.json"

#Bot configurations
jsonUsersRegisteredPath = jsonDatabasesPath + "/users.json"

#TODO Elaborate a cool description for the bot.
sid = Bot(command_prefix = "!",
          description = "")

#Calling Python scripts to define commands and events
import bot_modules.commandsDef
import bot_modules.eventsDef