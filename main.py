from dotenv import load_dotenv
load_dotenv()

from dsbot.bot import DSBot
import discord

import os

from typing import Tuple, Dict
from discord.ext.commands.context import Context



intents = discord.Intents.default()
intents.message_content = True
bot = DSBot(command_prefix = '!', intents = intents)




from chatgpt import get_gpt
@bot.command(name = "gpt")
async def __print(ctx: Context, *, speech: str):
    await ctx.send(get_gpt(speech))







bot.run(os.getenv("DISCORD_TKN"))