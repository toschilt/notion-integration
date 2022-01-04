#TODO How to deal with import secrets here?
import secrets

import bot_modules.commands as cmd
from bot_modules.config import *

#Python dictionary that keeps track of all the available commands.
#TODO Use a JSON file to configure that externally.
available_commands = {
    "help": [],
    "retrieveTasks": ["rt"]
}

#Implements the retrieveTasks command.
@sid.command(aliases = available_commands["retrieveTasks"])
async def retrieveTasks(context, databaseID):
    await cmd.retrieveTasks.retrieveTasks(context, personalWorkspace, databaseID, secrets.NotionKEY)