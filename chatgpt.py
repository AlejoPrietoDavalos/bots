from abc import ABC, abstractmethod

import openai
import os

import attr
from attr import validators, asdict

from typing import List

ROLES_ALLOWED = ("user", "assistant", "system")


@attr.s(frozen=True)
class MsgGPT:
    role: str = attr.ib(validator=validators.in_(ROLES_ALLOWED))
    content: str = attr.ib(validator=validators.instance_of(str))

    def to_json(self) -> dict:
        return asdict(self)



class ConvGPT(List[MsgGPT]):
    def __init__(self):
        super().__init__()

    @staticmethod
    def from_json():
        pass

class ChatGPT:
    """ Volverla luego abstracta."""
    def __init__(self, api_key: str):
        assert isinstance(api_key, str)
        if openai.api_key != api_key:
            openai.api_key = api_key
    
    def create_conv(self, user_id: int) -> ConvGPT:
        pass