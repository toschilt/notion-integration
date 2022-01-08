from bot_modules.config import *

@sid.event
async def on_message(message):
    if message.guild:
        #The message comes from a server.
        print("Guild")
        if message.content == 'test':
            await message.channel.send("Testing 1 2 3!")
    else:
        #The message comes from a DM.
        print("DM")

    await sid.process_commands(message)