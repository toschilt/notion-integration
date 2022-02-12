from bot_modules.config import sid

@sid.event
async def on_message(message):
    if not message.guild:
        #Message comes from DM message.  
        pass

    await sid.process_commands(message)