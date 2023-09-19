from __future__ import annotations

from discord.ext import commands

from typing import NewType

AuthorId = NewType("author_id", int)


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
    def author_id(self) -> AuthorId:
        return self.author.id