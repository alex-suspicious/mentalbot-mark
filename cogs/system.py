import discord  
from discord.ext import commands

class System(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.app_commands.command(name="ping", description="test slash command")
    async def ping(self, interaction: discord.Interaction):
        bot_latency = round(self.client.latency * 1000)
        await interaction.response.send_message(f"Pong! {bot_latency} ms.")

async def setup(bot):
    await bot.add_cog(System(bot))