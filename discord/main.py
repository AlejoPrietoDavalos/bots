from src.bot import DSBot
from src.commands import set_commands

import discord

import os

class Apps:
    class cha:
        pass


if __name__ == "__main__":
    intents = discord.Intents.all()
    bot = DSBot(command_prefix = '!', intents = intents)

    set_commands(bot)
    
    bot.run(os.getenv("TOKEN"))