from abc import ABC, abstractmethod

import discord
from discord.message import Message
from discord.ext.commands.bot import Bot



class DSBot(Bot, ABC):
    """
    Clase abstracta para el bot de discord.
    
    Implementar:
    ------------
    - `on_ready`: Se ejecuta por única vez cuando el bot logea.
    - `on_message`: Se ejecuta cuando un usuario envía un `Message`.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @abstractmethod
    async def on_ready(self):
        """ Tareas que se quieran hacer cuando el bot logea."""
        ...

    @abstractmethod
    async def on_message(self, message: Message):
        """ Se ejecuta cuando un usuario envía un mensaje."""
        if message.author.id == self.application_id:
            return
        await self.process_commands(message)
        
