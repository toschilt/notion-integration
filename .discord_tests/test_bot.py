import secrets
import discord
from discord.ext.commands import Bot

bot = Bot(command_prefix = '!',
          description = 'Aaaaaaaaaaaaa')

@bot.event
async def on_ready():
    print(f'Bot connected as {bot.user}')

@bot.event
async def on_ready():
    await bot.change_presence(activity = discord.Activity(
                              type = discord.ActivityType.watching,
                              name = 'Diguê no mundo da animação'))

@bot.event
async def on_message(message):
    if message.content == 'test':
        await message.channel.send("Testing 1, 2, 3!")

    await bot.process_commands(message)

@bot.command(name='server', help = 'Get server info')
async def fetchServerInfo(context):
    guild = context.guild

    await context.send(f'Server Name: {guild.name}')
    await context.send(f'Server Size: {len(guild.members)}')
    

bot.run(secrets.KEY)