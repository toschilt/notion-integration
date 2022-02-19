#Discord bot command.
#Plays something in the user voice channel.

import asyncio
from discord import FFmpegPCMAudio

from bot_modules.utils import readJSONFileAsDict

from bot_modules.config import audio_files_folder
from bot_modules.config import jsonMusicFiles

async def play(context, song):
    if context.author.voice is not None or context.author.voice.channel is not None:
        voice_channel = context.author.voice.channel

        if context.voice_client is None:
            vc = await voice_channel.connect()
        else:
            await context.voice_client.move_to(voice_channel)
            vc = context.voice_client

        musicFile = readJSONFileAsDict(jsonMusicFiles)

        vc.play(
            FFmpegPCMAudio(audio_files_folder + musicFile[song]), 
            after = lambda e: print('Música tocada!'))
        
        while context.voice_client.is_playing():
            pass

        await vc.disconnect()

    else:
        print("Usuário precisa se conectar em um canal.")