import os
import discord
import random
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()


guilty_gear_characters = [
    "Sol Badguy", "Ky Kiske", "May", "Axl Low", "Chip Zanuff", "Potemkin",
    "Faust", "Millia Rage", "Zato-1", "Giovanna", "Ramlethal Valentive",
    "Leo Whitefang", "Nagoriyuki", "Anji Mito", "I-No", "Goldlewis Dickenson",
    "Jack-O", "Happy Chaos", "Baiken", "Testament", "Bridget"
]

league_characters = [
    "Sion"
]


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event 
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('-Guilty Gear'):
        await message.channel.send(random.choice(guilty_gear_characters))
    if message.content.startswith('-League'):
        await message.channel.send(random.choice(league_characters))

client.run(TOKEN)


