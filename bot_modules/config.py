import os
from discord.ext.commands import Bot

#Notion configurations
botModulesPath = os.path.dirname(__file__)
jsonDatabasesPath = botModulesPath + "/databases"
jsonDatabasesRegisteredNotionPath = jsonDatabasesPath + "/registered_notion.json"

#Bot configurations
#TODO Elaborate a cool description for the bot.
sid = Bot(command_prefix = "!",
          description = "")