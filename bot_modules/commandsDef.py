import bot_modules.commands as cmd
from bot_modules.config import *
from bot_modules.utils import checkPermission

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
    "endSprint": ["es"],
    "response": ["r"]
}

#databaseID: the alias of the desired database
@sid.command(aliases = available_commands["retrieveTasks"])
async def retrieveTasks(context, databaseAlias):
    if await checkPermission(context, "retrieveTasks"):
        await cmd.retrieveTasks.retrieveTasks(context, databaseAlias)

@sid.command(aliases = available_commands["listWorkspaces"])
async def listWorkspaces(context):
    if await checkPermission(context, "listWorkspaces"):
        await cmd.listWorkspaces.listWorkspaces(context)

#workspaceAlias: the workspace that the user wants to list the databases
@sid.command(aliases = available_commands["listDatabases"])
async def listDatabases(context, workspaceAlias):
    if await checkPermission(context, "listDatabases"):
        await cmd.listDatabases.listDatabases(context, workspaceAlias)

#alias: the name that the workspace is known.
#secretToken: the private token of the workpace integration
@sid.command(aliases = available_commands["registerWorkspace"])
async def registerWorkspace(context, alias, secretToken):
    if await checkPermission(context, "registerWorkspace"):
        await cmd.registerWorkspace.registerWorkspace(context, alias, secretToken)

#databaseAlias: the name that the database is known.
#id: the id of the database
#workspaceAlias: the alias of its workspace
@sid.command(aliases = available_commands["registerDatabase"])
async def registerDatabase(context, databaseAlias, id, workspaceAlias):
    if await checkPermission(context, "registerDatabase"):
        await cmd.registerDatabase.registerDatabase(context, databaseAlias, id, workspaceAlias)

#specialFunction: indicates if the database has a special function.
@sid.command(aliases = available_commands["setSpecialDatabase"])
async def setSpecialDatabase(context, databaseAlias, specialFunction):
    if await checkPermission(context, "setSpecialDatabase"):
        await cmd.setSpecialDatabase.setSpecialDatabase(context, databaseAlias, specialFunction)

#databaseFromAlias: the database that the data comes from.
#databaseToAlias: the database that the data comes to.
@sid.command(aliases = available_commands["replicateDatabase"])
async def replicateDatabase(context, databaseFromAlias, databaseToAlias):
    if await checkPermission(context, "replicateDatabase"):
        await cmd.replicateDatabase.replicateDatabase(context, databaseFromAlias, databaseToAlias)

#email: the email registered in DEF_MEMBERS special database.
@sid.command(aliases = available_commands["registerUser"])
async def registerUser(context, email):
    if await checkPermission(context, "registerUser"):
        await cmd.registerUser.registerUser(context, email)

@sid.command(aliases = available_commands["endSprint"])
async def endSprint(context):
    if await checkPermission(context, "endSprint"):
        await cmd.endSprint.endSprint(context)

@sid.command(aliases = available_commands["response"])
async def response(context):
    if await checkPermission(context, "response"):
        await cmd.response.response(context)