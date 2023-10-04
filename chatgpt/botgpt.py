from abc import ABC, abstractmethod

from chatgpt.message import MsgGPT
from chatgpt.conversation import ConvGPT

import openai

import os
import attr



class ManagerGPT:
    """ Volverla luego abstracta."""
    def __init__(self, api_key: str):
        assert isinstance(api_key, str)
        if openai.api_key != api_key:
            openai.api_key = api_key
        self.convs = {}
    
    def create_conv(self):
        pass

    def load_conv(self):
        pass

    def save_conv(self):
        pass

    async def send_prompt(self, conv: ConvGPT) -> MsgGPT:
        response = openai.ChatCompletion.create(
            messages = {"messages": conv.msgs_json},
            model = "gpt-3.5-turbo",
            temperature = 0,
            #max_tokens = 2000
        )
        # FIXME: MsgGPT(response....)
        content = response["choices"][-1]["message"]["content"]
        print(content)
        return response
