from typing import List, Any
from functools import wraps
from abc import ABC, abstractmethod

import discord
from discord.message import Message
from discord import Intents
from discord.channel import TextChannel
from oaikit import OAIMsg, ContentText, USER, ASSISTANT

from dsai.config import CfgDS, CfgChannelDS
from dsai.msg_ds import MsgDS


def on_message_wrapper(func):
    @wraps(func)
    async def wrapper(self, message: Message):
        msg_ds = MsgDS(message=message, user=self.user)
        if msg_ds.is_bot:
            return
        return await func(self, msg_ds)
    return wrapper


class BaseClientDS(discord.Client, ABC):
    """
    Properties:
    -----------
    - `user ()`
    """
    def __init__(self, *, cfg_ds: CfgDS, intents: Intents, **options: Any):
        super().__init__(intents=intents, **options)
        self.cfg_ds = cfg_ds
    
    @abstractmethod
    async def on_ready(self) -> None:
        ...

    @abstractmethod
    async def on_message(self, message: Message) -> None:
        ...

    async def get_last_msgs_ds(self, *, msg_ds: MsgDS, leak_by_author: bool = True, pop_bot_in_extremes: bool = True) -> List[MsgDS]:
        iter_msgs_ds = msg_ds.channel.history(limit=self.cfg_ds.limit_msg)
        msgs_ds = [MsgDS(message=message, user=self.user) async for message in iter_msgs_ds]
        msgs_ds.reverse()

        if pop_bot_in_extremes:
            flag = True
            while flag and len(msgs_ds)>0:
                if msgs_ds[0].is_bot:
                    msgs_ds.pop(0)
                    continue
                elif msgs_ds[-1].is_bot:
                    msgs_ds.pop(-1)
                    continue
                else:
                    flag = False
        #if leak_by_author:  # TODO: Testear con otra persona.
        #    is_author_msg = message.author.id == msg_ds.author_id
        #    is_bot_msg = message.author.id == msg_ds.user.id
        #    if not is_author_msg or not is_bot_msg:
        #        continue
        return msgs_ds

    def msgs_oai_from_ds(self, *, msgs_ds: List[MsgDS], cfg_channel: CfgChannelDS) -> List[OAIMsg]:
        msgs_oai = [OAIMsg.system(content=[ContentText(text=cfg_channel.ctx)])]
        for m in msgs_ds:
            role = USER if not m.is_bot else ASSISTANT
            if msgs_oai[-1].role == role:
                msgs_oai[-1].content.append(ContentText(text=m.content))
            else:
                msgs_oai.append(OAIMsg(role=role, content=[ContentText(text=m.content)]))
        return msgs_oai

    async def send_message(self, *, channel: TextChannel, content: str) -> None:
        if not isinstance(content, str) or content == "":
            raise ValueError("txt is a string, for now...")
        await channel.send(content)
