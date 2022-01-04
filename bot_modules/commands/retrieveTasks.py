#Discord bot command.
#Returns the tasks in the Notion workspace.

async def retrieveTasks(context, personalWorkspace, databaseID, notionKey):
    databaseObject = personalWorkspace.addDatabase("databaseLabel", databaseID)
    formattedTable = databaseObject.getDatabaseDataToTablePrint()
    await context.send(formattedTable)