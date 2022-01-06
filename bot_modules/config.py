#TODO How to deal with import secrets here?
import secrets

import os
from bot_modules.notion_modules import NotionWorkspace
from discord.ext.commands import Bot

#Notion configurations
botModulesPath = os.path.dirname(__file__)
jsonDatabasesPath = botModulesPath + "/databases"
jsonDatabasesRegisteredNotionPath = jsonDatabasesPath + "/registered_notion.json"

#TODO Remove this later
personalWorkspace = NotionWorkspace.NotionWorkspace(secrets.NotionKEY)

#Bot configurations
#TODO Elaborate a cool description for the bot.
sid = Bot(command_prefix = "!",
          description = "")