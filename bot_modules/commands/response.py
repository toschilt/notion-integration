#Discord bot command.
#Allows the user to awnser the end sprint message.

from bot_modules.config import jsonUsersRegisteredPath
from bot_modules.config import jsonGoogleKey

from bot_modules.utils import readJSONFileAsDict

from bot_modules.google_modules.SprintDocument import SprintDocument

async def response(context):
    DOCUMENT_ID = "1S1rvPpXDTX2DXbaCSqlGnOb5IQB80D47Nie1D1D4AIw"
    sprintDocument = SprintDocument(jsonGoogleKey, DOCUMENT_ID)

    users = readJSONFileAsDict(jsonUsersRegisteredPath)
    userName = users[str(context.author.id)]["notion"]["name"]

    sprintDocument.insertNewRegister(
        context.message.created_at.date(),
        userName, 
        context.message.content[3:])