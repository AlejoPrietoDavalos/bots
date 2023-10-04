from __future__ import annotations

from dsbot.user import UserIdDS, UserNameDS

from discord.ext import commands

from typing import NewType



class ContextExt(commands.Context):
    """ `discord.ext.commands.Context` con funcionalidad extendida."""
    def __init__(self, ctx: commands.Context):
        super().__init__(
            bot = ctx.bot,
            message = ctx.message,
            args = ctx.args,
            kwargs = ctx.kwargs,
            prefix = ctx.prefix,
            command = ctx.command,
            view = ctx.view
        )

    @property
    def author_id(self) -> UserIdDS:
        return self.author.id
    
    @property
    def author_name(self) -> UserNameDS:
        return self.author.global_name