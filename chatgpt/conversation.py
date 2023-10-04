from chatgpt.message import MsgGPT

from typing import List

class ConvGPT(List[MsgGPT]):
    """ Una conversación es una lista de mensajes ordenada."""
    def __init__(self):
        super().__init__()

    @property
    def msgs_json(self) -> List[dict]:
        return [msg.json for msg in self]
    
    def add_msg(self, msg: MsgGPT) -> None:
        assert isinstance(msg, MsgGPT)
        super().append(msg)
