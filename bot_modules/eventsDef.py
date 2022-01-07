from bot_modules.config import *

@sid.event
async def on_message(message):
    if message.content == 'test':
        await message.channel.send("Testing 1 2 3!")
    
    await sid.process_commands(message)