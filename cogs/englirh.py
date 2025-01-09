# The thing with socks 🧦
import discord 
import random 
import math  
from discord.ext import commands

class Englirh(commands.Cog):
    reactions = ["🧦","👏","😰","🗣","🙏","💀"]

    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.Cog.listener("on_message")
    async def message_englirfying(self,message):
        if message.author.bot:
            return

        if( random.randint(0,100) > 97 ):
            await message.channel.send(message.content.replace("s","r") + " 🧦")

    @commands.Cog.listener("on_message")
    async def random_reactions(self,message):
        if message.author.bot:
            return

        if( random.randint(0,100) > 80 ):
            await message.add_reaction(random.choice(self.reactions))

async def setup(bot):
    await bot.add_cog(Englirh(bot))