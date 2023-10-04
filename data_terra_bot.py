from dotenv import load_dotenv
load_dotenv()

from chatgpt.message import MsgGPT
from dsbot.user import UserDS
from dsbot.bot import DSBot
from dsbot.context import ContextExt

from chatgpt.botgpt import ManagerGPT
from chatgpt.conversation import ConvGPT

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
manager_gpt = ManagerGPT(os.getenv("OPENAI_TKN"))

# @bot.command(name="help")
# async def _help(_ctx: commands.Context):
#     await _ctx.send("Listar todos los comandos, o ver si ya existe esa funcionalidad.")
# @bot.command(name="gpt_save")
# async def _gpt_save(_ctx: commands.Context):
#     pass
# @bot.command(name="gpt_load")
# async def _gpt_load(_ctx: commands.Context):
#     pass
# @bot.command(name="gpt_list")
# async def _gpt_list(_ctx: commands.Context):
#     pass

# TODO: user = UserDS(ctx_ext.author_id, ctx_ext.author_name)


@bot.command(name="gpt")
async def _gpt(_ctx: commands.Context, *, prompt: str = None) -> None:
    """
    - Si no tiene una conversación activa, crea la conversación.
    - De tenerla, agrega el prompt a la conversación y busca
    el response, se agrega a la conversación y se muestra.
    """
    if prompt is None:
        return None
    ctx_ext = ContextExt(_ctx)
    user = (ctx_ext.author_id, ctx_ext.author_name)
    if user not in manager_gpt.convs:
        manager_gpt.convs[user] = ConvGPT()
        print("entro")
    conv: ConvGPT = manager_gpt.convs[user]
    
    msg = MsgGPT("user", prompt)
    conv.add_msg(msg)
    response = await manager_gpt.send_prompt(conv)
    print("------------")
    print(response)
    print(type(response))



    print(conv)
    #print(ctx_ext.author)
    #print(bot.get_user(ctx_ext.author_id))
    #print(type(bot.get_user(ctx_ext.author_id)))
    #user = UserDS(ctx_ext.author_id, ctx_ext.author_name)
    #response = manager_gpt.send_prompt(ctx_ext.author_id, prompt)
    #print(response)
    #print(type(response))

@bot.command(name="prueba")
async def _prueba(_ctx: commands.Context, *, speech: str = None):
    if speech is not None:
        await _ctx.send("=play rosa rosa la maravillosa")


bot.run(os.getenv("DISCORD_TKN"))