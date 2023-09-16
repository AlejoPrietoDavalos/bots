import discord
from discord.message import Message
from discord.ext.commands.bot import Bot



class DSBot(Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def on_ready(self):
        """ Tareas que se quieran hacer cuando el bot logea."""
        print("~~~~~~ready~~~~~~")

    async def on_message(self, message: Message):
        if message.author.id == self.application_id: return
        await self.process_commands(message)
        
