import os
import discord
import random
import utils.constants as constants
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()
media_file_path = os.path.join(os.path.dirname(__file__), "media")


@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    angry_dia_gifs = [os.path.join(media_file_path, constants.dia_yell_gif),
                      os.path.join(media_file_path, constants.dia_stare_gif)]
    if constants.muse_trigger in message.content:
        await message.channel.send(constants.dia_response)
        await message.channel.send(file=discord.File(random.choice(angry_dia_gifs)))

    warn_trigger_responses = [constants.sobbing_face_response, constants.nauseated_face_response]
    if constants.warn_trigger in message.content:
        await message.channel.send(random.choice(warn_trigger_responses))

client.run(TOKEN)
