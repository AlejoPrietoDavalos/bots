from discord.message import Message
from discord.user import ClientUser
from discord.channel import TextChannel
from discord.member import Member

class MsgDS:
    def __init__(self, *, message: Message, user: ClientUser):
        self.message = message
        self.user = user

    @property
    def id(self) -> int:
        return self.message.id
    
    @property
    def is_bot(self) -> bool:
        return self.message.author.id == self.user.id

    @property
    def author(self) -> Member:
        return self.message.author

    @property
    def author_id(self) -> int:
        return self.author.id

    @property
    def content(self) -> str:
        return self.message.content

    @property
    def channel(self) -> TextChannel:
        return self.message.channel

    @property
    def channel_id(self) -> int:
        return self.message.channel.id
