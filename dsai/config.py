from typing import List, Dict

from pydantic import BaseModel
from oaikit import T_OAIModels

from dsai.msg_ds import MsgDS

class CfgChannelDS(BaseModel):
    author_ids: List[int]
    ctx: str
    model: T_OAIModels

class CfgDS(BaseModel):
    channel_id2author_ids_allowed: Dict[int, CfgChannelDS]
    limit_msg: int

    def cfg_from_channel_id(self, *, channel_id: int) -> CfgChannelDS:
        return self.channel_id2author_ids_allowed[channel_id]

    def is_author_allowed(self, *, msg_ds: MsgDS) -> bool:
        cfg_channel = self.cfg_from_channel_id(channel_id=msg_ds.channel_id)
        if msg_ds.channel_id not in self.channel_id2author_ids_allowed:
            # Se verifica que el channel esté dentro de los permitidos.
            return False
        elif msg_ds.author_id not in cfg_channel.author_ids:
            # Se verifica que el usuario esté permitido dentro del channel.
            return False
        return True
