import json
from readline import insert_text

from bot_modules.config import sid
from bot_modules.config import jsonGoogleKey

from bot_modules.google_modules import GoogleDocument

DOCUMENT_ID = "1S1rvPpXDTX2DXbaCSqlGnOb5IQB80D47Nie1D1D4AIw"
sprintDocument = GoogleDocument.GoogleDocument(jsonGoogleKey, DOCUMENT_ID)

@sid.event
async def on_message(message):
    if not message.guild:
        #Message comes from DM message.  
        sprintDocument.insertTextAtIndex(message.content, 25)
        sprintDocument.executeChanges()

    await sid.process_commands(message)