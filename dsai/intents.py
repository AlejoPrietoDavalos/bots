import discord

def get_intents():
    intents = discord.Intents.default()
    intents.message_content = True
    return intents
