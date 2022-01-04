import secrets

import discord
from discord.ext.commands import Bot

sid = Bot(command_prefix = '!',
          description = 'Aaaaaaaaaaaaa')

@sid.event
async def on_ready():
    print(f'Bot connected as {bot.user}')

@sid.event
async def on_ready():
    await sid.change_presence(activity = discord.Activity(
                              type = discord.ActivityType.watching,
                              name = 'Diguê no mundo da animação'))

@sid.event
async def on_message(message):
    if message.content == 'test':
        await message.channel.send("Testing 1, 2, 3!")

    await sid.process_commands(message)

@sid.command(name='server', help = 'Get server info')
async def fetchServerInfo(context):
    guild = context.guild
    message = context.message
    author = context.author

    await context.send(f'Server Name: {guild.name}')
    await context.send(f'Server Size: {len(guild.members)}')
    await context.send(f'Message send: {message}')
    await context.send(f'Message author: {author}')
    

sid.run(secrets.KEY)