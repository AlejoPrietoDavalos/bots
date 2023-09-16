from __viejo_api_openai.prompt import Prompt

import openai
from openai.openai_object import OpenAIObject
import os
openai.api_key = os.getenv("TOKEN_OPENAI")


import numpy as np

from typing import Union, List, Dict, TypeVar
user_id = TypeVar(name = "user_id")


class ModelsOpenAI:
    class GPT3_5:
        max_tokens = 4096
        model_name = "gpt-3.5-turbo"
    
    class Davinci:
        max_tokens = 4097
        model_name = "text-davinci-003"


class __ChatGPT:
    def __init__(self, user_id: int, chat_id: int, context: str = ""):
        self.__user_id = user_id
        self.__chat_id = chat_id
        self.__chat: List[Prompt] = self.__create(context = context)

    @property
    def user_id(self): return self.__user_id

    @property
    def chat_id(self): return self.__chat_id

    @property
    def chat(self): return self.__chat
    
    @property
    def messages(self) -> List[dict]:
        """ Retorna la conversación en un formato que le gusta a openai."""
        msgs: List[dict] = [prompt.message for prompt in self.chat]
        return msgs

    def __create(self, context: str = "") -> List[Prompt]:
        return [] if context == "" else [Prompt(role="system", content=context)]


class ChatGPT(__ChatGPT):
    """
    Roles:
    ------
        - `system` -> Contexto.
        - `user` -> Usuario que envia el prompt.
        - `assistant` -> Asistente, respuesta de GPT.

    Averiguar:
    ----------
        - Como es el response cuando GPT interpreta que hay una pregunta maliciosa.
        - Acá esta explicado cuantos tokens se usan. | Link: https://platform.openai.com/docs/guides/chat/introduction
    """
    def __init__(self, user_id: int, chat_id: int, context: str = ""):
        super().__init__(user_id, chat_id, context)

    def append_prompt(self, prompt: Prompt):
        self.chat.append(prompt)

    def get_response(
            self,
            input_prompt: str,
            max_tokens: int = 3000,
            model = ModelsOpenAI.GPT3_5,
            temperature = 0) -> OpenAIObject:
        """
        Hace una consulta a la API de OpenAI con
        el prompt ingresado y retorna el response.
        
        - See https://platform.openai.com/docs/api-reference/completions/create for a list of valid parameters
        - See https://platform.openai.com/docs/api-reference/chat-completions/create for a list of valid parameters.
        
        TODO: assert max_tokens <= self.MODELS[model]["max_tokens"], "Se superó el máximo número de tokens que puede generar el modelo."
        """
        self.append_prompt(Prompt(role = "user", content = input_prompt))

        #~~~~~~~~~~Ver bien que devuelve este obj~~~~~~~~~~
        response: OpenAIObject = openai.ChatCompletion.create(
            messages = self.messages,
            model = model.model_name,
            temperature = temperature,
            max_tokens = max_tokens
        )

        content_response = response["choices"][-1]["message"]["content"]
        self.append_prompt(Prompt(role = "assistant", content = content_response))

        return response

    def save(self):
        """
        Implementar un método de guardado, que guarde la conversación
        y después se pueda levantar a partir de un fichero.
        """
        pass

    def load(self, path):
        pass



