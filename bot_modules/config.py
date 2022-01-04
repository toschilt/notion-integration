#TODO How to deal with import secrets here?
import secrets

from bot_modules.notion_modules import NotionWorkspace
from discord.ext.commands import Bot

#Notion configurations
#TODO Storage the database and workspace objects persistently
personalWorkspace = NotionWorkspace.NotionWorkspace(secrets.NotionKEY)

#Bot configurations
#TODO Elaborate a cool description for the bot.
sid = Bot(command_prefix = "!",
          description = "")