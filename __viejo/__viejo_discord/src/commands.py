from src.bot import DSBot
from __viejo_api_openai.conversation import ChatGPT, ListChatGPT

import discord
from discord.ext.commands.context import Context


def set_commands(bot: DSBot):
    """
    Enumerar uno a uno todos los comandos del bot.
    """
    @bot.command(name = "random")
    async def __random(ctx: Context):
        import random
        await ctx.send(random.randint(0,10))

    @bot.command(name = "print")
    async def __print(ctx: Context, *, speech: str):
        await ctx.send(speech)

    @bot.command(name = "clear")
    async def __clear(ctx: Context):
        await ctx.channel.purge(limit = None)

    @bot.command(name = "gpt")
    async def __gpt(ctx: Context, *, prompt):#flag, *, prompt):
        author_id = ctx.message.author.id
        asd = bot.container_chatgpt

        if author_id not in asd.keys():
            asd.create_chat(author_id, "")
        chat_ = asd.get_specific_chat(author_id, 0)

        response = chat_.get_response(prompt)
        await ctx.send(chat_.conversation[-1].content)

        # if flag in ("-c"):      # Context
        #     pass
        # elif True:
        #     pass
        # else:                   # No-Flag
        #     pass

        
        
        # flag_prompt = flag + " " + prompt
        # 
        # if (author_id not in bot.container_chatgpt) or (flag in ("-c", "--context")):
        #     bot.container_chatgpt[author_id] = ChatGPT(author_id, flag_prompt)
        # elif flag in ("-add"):
        #     
        #     response = bot.container_chatgpt[author_id].get_response(flag_prompt)
        #     await ctx.send(bot.container_chatgpt[author_id].conversation[-1]["content"])
        
