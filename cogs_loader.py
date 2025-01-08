import os

async def load(bot, path="cogs"):
	for filename in os.listdir(f"./{path}"):
		if filename.endswith(".py"):
			await bot.load_extension(f"cogs.{filename[:-3]}")  
