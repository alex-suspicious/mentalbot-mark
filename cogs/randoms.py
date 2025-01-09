# The thing with socks 🧦
import discord 
import random 
import asyncio
import math  
from discord.ext import commands

class Randoms(commands.Cog):
    messages = [
        "Agree",
        "Shut up",
        "I'm so glad that i'm not a human, don't need to pay taxes and all yk 💃🏻",
        "💀",
        "👀",
        "Hey @user, your steam profile looks amazing bro 🗣️",
        "Dude fr?",
        "Look outta window dude",
        "Don't worry, that's ok",
        "No you",
        "based",
        "femboy"
    ]

    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.Cog.listener("on_message")
    async def random_messages(self,message):
        if message.author.bot:
            return

        if( random.randint(0,100) > 96 ):
            await message.channel.send( random.choice(self.messages).replace("@user",message.author.name) )

    @discord.app_commands.command(name="oracle", description="Ask a question, and i will tell simple - yes or no")
    async def oracle(self, interaction: discord.Interaction, question: str):
        thinking_messages = [
            "Lemme think... 🤔",
            "Hard question..",
            "Wait i need to connect a spacestation",
            "Wait a sec",
            "..."
        ]

        answer_messages = [
            "Definitely YES!",
            "Yes..",
            "No!",
            "No no no no!",
            "I don't know",
            "YES FR 🗣️",
            "Nuh uh"
        ]

        await interaction.response.send_message(random.choice(thinking_messages))
        await asyncio.sleep(3)
        await interaction.edit_original_response(content=random.choice(answer_messages))

async def setup(bot):
    await bot.add_cog(Randoms(bot))