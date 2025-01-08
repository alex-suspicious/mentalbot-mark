import discord  
from discord.ext import commands

class Greetings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = discord.utils.get(self.bot.get_all_channels(), id=1109046513247735889)
        if channel is not None:
            await channel.send(f'Yay, {member.mention} has joined our party 🥳.')

async def setup(bot):
    await bot.add_cog(Greetings(bot))