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
    "registerDatabase": ["rd"],
    "replicateDatabase": ["repd"],
    "registerUser": ["ru"],
    "setSpecialDatabase": ["sed"],
    "endSprint": ["es"]
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

#specialFunction: indicates if the database has a special function.
@sid.command(aliases = available_commands["setSpecialDatabase"])
async def setSpecialDatabase(context, databaseAlias, specialFunction):
    await cmd.setSpecialDatabase.setSpecialDatabase(context, databaseAlias, specialFunction)

#databaseFromAlias: the database that the data comes from.
#databaseToAlias: the database that the data comes to.
@sid.command(aliases = available_commands["replicateDatabase"])
async def replicateDatabase(context, databaseFromAlias, databaseToAlias):
    await cmd.replicateDatabase.replicateDatabase(context, databaseFromAlias, databaseToAlias)

#email: the email registered in DEF_MEMBERS special database.
@sid.command(aliases = available_commands["registerUser"])
async def registerUser(context, email):
    await cmd.registerUser.registerUser(context, email)

@sid.command(aliases = available_commands["endSprint"])
async def endSprint(context):
    await cmd.endSprint.endSprint(context)