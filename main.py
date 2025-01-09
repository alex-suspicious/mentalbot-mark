import os
from dotenv import load_dotenv
import discord
import cogs_loader
from discord.ext import commands

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot("!",intents=intents)

@client.event
async def on_ready():
    await cogs_loader.load(client)
    print(f'I am logged in as {client.user}')

    synced = await client.tree.sync()
    print(f"Synced {len(synced)} command(s).")


client.run(os.getenv('BOT_TOKEN'))