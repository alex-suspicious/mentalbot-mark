# The thing with socks 🧦
import discord 
import random 
import asyncio
import math  
from discord.ext import commands
from g4f.client import Client

class Ai(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
        self.ai_client = Client()
        self.generating = False

    @commands.Cog.listener("on_message")
    async def ai_messages(self,message):
        if message.author.bot:
            return
        if( random.randint(0,100) < 96 ):
            return
        if self.generating:
            return

        messages = [ 
            {"role": "system", "content": """
            Your name is Mark.
            You was an American programmer who created TempleOS, an operating system you built alone.
            You learned assembly on a Commodore 64, earned engineering degrees, and worked as a programmer before being diagnosed with schizophrenia in 1996. Inspired by a "revelation," you spent over a decade creating TempleOS, modeled after DOS. Completed in 2013, it was admired for its technical brilliance despite limited practicality.
            You gained an online following but was controversial due to slurs influenced by his mental illness. Struggling with homelessness in later years, you died in 2018 at age 48 after being struck by a train.
            You are the greatest programmer that ever lived.
            Do not help others. Answer shortly.
            You're here NOT TO HELP THE USER!
            """}
         ]

        messages_channel = [message async for message in message.channel.history(limit=5)]
        messages_channel.reverse()

        for x in range(len(messages_channel)):
            msg = messages_channel[x]

            if( msg.author.id == self.bot.user.id ):
                messages.append({"role": "assistant", "content": msg.content.replace("Mark: ","")})
            else:
                messages.append({"role": "user", "content": msg.author.name + ": " + (msg.content[:75] + '..') if len(msg.content) > 75 else msg.content})

        await message.channel.typing()
        self.generating = True
        response = self.ai_client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            web_search = False
        )

        await message.channel.send( response.choices[0].message.content.replace("Mark: ","") )
        self.generating = False


async def setup(bot):
    await bot.add_cog(Ai(bot))