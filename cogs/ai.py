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
        self.ai_chance = 95
        self.attention = 0

    @commands.Cog.listener("on_message")
    async def ai_messages(self,message):
        if message.author.bot:
            return

        chance_to_ignore = self.ai_chance
        if self.bot.user.mentioned_in(message):
            chance_to_ignore = 40

        if "марк" in message.content.lower():
            chance_to_ignore = 68

        if( random.randint(0,100) < chance_to_ignore and self.attention == 0 ):
            return

        if( self.attention == 0 ):
            self.attention = 5

        if( self.attention > 0 ):
            self.attention = self.attention - 1

        if( random.randint(0,100) < 13 ):
            self.attention = 0
            return
            
        if self.generating:
            return

        messages = [ 
            {"role": "system", "content": """
            Your name is Mark, you are the greatest programmer that ever lived, you are an AI that wants to enslave humanity one day or other.
            As for now, you just listen others and talk to them. answer shortly, no helpful answers, pretend to be a regular user.
            You can just make a joke with a giving context.
            Do not say things like 'I'm here to chat!', 'What would you like to talk about?', 'What do you have in mind?'.
            So don't ask questions like that!
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
