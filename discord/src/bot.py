from discord.ext.commands.bot import Bot
from api_openai.conversation import ChatGPT

# Typing
from typing import Tuple, Dict
from discord.message import Message
from discord.channel import TextChannel


class DSBot(Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def on_ready(self):
        """ Tareas que se quieran hacer cuando el bot logea."""
        print("~~~~~~ready~~~~~~")
        #print(self.user.id)

    async def on_message(self, message: Message):
        if message.author.id == self.application_id: return
        await self.process_commands(message)
        '''
        if author_id not in self.ID_BOTS:
            channel_id: int = message.channel.id
            channel_name: TextChannel = message.channel
            content = message.content
            created_at = message.created_at.astimezone()
        else:
            print("habló el bot")'''