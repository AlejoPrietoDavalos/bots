from dotenv import load_dotenv
load_dotenv()

from dsbot.bot import DSBot
from dsbot.context import ContextExt
from chatgpt import ChatGPT
import discord

import attr
import os

from typing import Tuple, Dict
from discord.ext import commands
from discord.message import Message


class TerraBot(DSBot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    async def on_ready(self):
        print("~~~~~~ ATR cumbia cuambia....~~~~~~")
    
    async def on_message(self, message: Message):
        return await super().on_message(message)



intents = discord.Intents.default()
intents.message_content = True
bot = TerraBot(command_prefix='!', intents=intents)
chatgpt = ChatGPT(os.getenv("OPENAI_TKN"))



@bot.command(name="gpt")
async def _gpt(_ctx: commands.Context, *, speech: str = None):
    """
    - Si no tiene una conversación activa, crea la conversación.
    - De tenerla, agrega el prompt a la conversación y busca
    el response, se agrega a la conversación y se muestra.
    """
    ctx_ext = ContextExt(_ctx)
    if speech is None:
        await ctx_ext.send()
        return
    
    print(speech)
    print(type(speech))
    #await ctx_ext.send("jlansdjkas")


bot.run(os.getenv("DISCORD_TKN"))