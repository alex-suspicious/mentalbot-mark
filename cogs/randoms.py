# The thing with socks 🧦
import discord 
import random 
import math  
from discord.ext import commands

class Randoms(commands.Cog):
    messages = [
        "Sometimes i dream about electric sheep 🤔",
        "How's it going y'all?",
        "Agree",
        "Shut up",
        "I'm so glad that i'm not a human, don't need to pay taxes and all yk 💃🏻",
        "💀",
        "👀",
        "Hey @user, your steam profile looks amazing bro 🗣️",
        "hey @user",
        "I see you @user"
    ]

    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.Cog.listener("on_message")
    async def random_messages(self,message):
        if message.author.bot:
            return

        if( random.randint(0,100) > 98 ):
            await message.channel.send( random.choice(self.messages).replace("@user",message.author.name) )


async def setup(bot):
    await bot.add_cog(Randoms(bot))