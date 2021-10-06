import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    dia_response = "Can it be, that you’re talking about μ’s? How dare you mistaken their name?! Hm? In the school " \
                   "idol world, μ’s are legendary. They’re the holy ground, holy scripture, the origin of life " \
                   "equivalent to the universe. And you mistaken their name?! Absolutely ridiculous. "
    if "u's" in message.content:
        await message.channel.send(dia_response)

    dragon_response = "Dragons are gay"
    if message.content == "dragon":
        await message.channel.send(dragon_response)

    egypt_response = "I lub Egypt"
    if message.content == "Egypt is the best":
        await message.channel.send(egypt_response)

client.run(TOKEN)
