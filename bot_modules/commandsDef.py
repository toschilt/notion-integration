import bot_modules.commands as cmd
from bot_modules.config import *

#Python dictionary that keeps track of all the available commands.
#TODO Use a JSON file to configure that externally.
available_commands = {
    "help": [],
    "retrieveTasks": ["rt", "tasks", "tarefas"],
    "listWorkspaces": ["lw"],
    "listDatabases": ["ld"],
    "registerWorkspace": ["rw"],
    "registerDatabase": ["rd"]
}

#databaseID: the alias of the desired database
@sid.command(aliases = available_commands["retrieveTasks"])
async def retrieveTasks(context, databaseAlias):
    await cmd.retrieveTasks.retrieveTasks(context, databaseAlias)

@sid.command(aliases = available_commands["listWorkspaces"])
async def listWorkspaces(context):
    await cmd.listWorkspaces.listWorkspaces(context)

#workspaceAlias: the workspace that the user wants to list the databases
@sid.command(aliases = available_commands["listDatabases"])
async def listDatabases(context, workspaceAlias):
    await cmd.listDatabases.listDatabases(context, workspaceAlias)

#alias: the name that the workspace is known.
#secretToken: the private token of the workpace integration
@sid.command(aliases = available_commands["registerWorkspace"])
async def registerWorkspace(context, alias, secretToken):
    await cmd.registerWorkspace.registerWorkspace(context, alias, secretToken)

#databaseAlias: the name that the database is known.
#id: the id of the database
#workspaceAlias: the alias of its workspace
@sid.command(aliases = available_commands["registerDatabase"])
async def registerDatabase(context, databaseAlias, id, workspaceAlias):
    await cmd.registerDatabase.registerDatabase(context, databaseAlias, id, workspaceAlias)