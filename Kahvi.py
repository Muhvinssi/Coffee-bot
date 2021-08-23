import os
import discord
from discord import message
from dotenv import load_dotenv
import asyncio
from discord_slash import SlashCommand

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} Has connected')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if 'Kahvi' or 'kahvi' in message.content:
        await message.channel.send('Kahvia?! Mitä, Missä?')
client.run(TOKEN)