#TODO How to deal with import secrets here?
import secrets

from bot_modules.notion_modules import NotionWorkspace
from discord.ext.commands import Bot

#Notion configurations
storageNotionComponentsFilePath = "../databases/registered_notion.json"

#TODO Remove this later
personalWorkspace = NotionWorkspace.NotionWorkspace(secrets.NotionKEY)

#Bot configurations
#TODO Elaborate a cool description for the bot.
sid = Bot(command_prefix = "!",
          description = "")