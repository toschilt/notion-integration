#TODO How to deal with import secrets here?
import secrets

import bot_modules.commands as cmd
from bot_modules.config import *

#Python dictionary that keeps track of all the available commands.
#TODO Use a JSON file to configure that externally.
available_commands = {
    "help": [],
    "retrieveTasks": ["rt", "tasks", "tarefas"],
    "registerWorkspace": ["rw"],
    "registerDatabase": ["rd"]
}


#context: the Discord Bot context of the command;
#alias: the name that the workspace is known.
#secretToken: the private token of the workpace integration
@sid.command(aliases = available_commands["registerWorkspace"])
async def registerWorkspace(context, alias, secretToken):
    await cmd.registerWorkspace.registerWorkspace(context, alias, secretToken)

#context: the Discord Bot context of the command;
#databaseAlias: the name that the database is known.
#id: the id of the database
#workspaceAlias: the alias of its workspace
@sid.command(aliases = available_commands["registerDatabase"])
async def registerDatabase(context, databaseAlias, id, workspaceAlias):
    await cmd.registerDatabase.registerDatabase(context, databaseAlias, id, workspaceAlias)

#databaseID: the id of the database
@sid.command(aliases = available_commands["retrieveTasks"])
async def retrieveTasks(context, databaseID):
    await cmd.retrieveTasks.retrieveTasks(context, personalWorkspace, databaseID, secrets.NotionKEY)