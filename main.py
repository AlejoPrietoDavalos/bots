import os
import json
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()

from discord import Intents
from discord.ext import commands

from dsai.config import CfgDS
from dsai.msg_ds import MsgDS
from dsai.intents import get_intents
from dsai.client import BaseClientDS, on_message_wrapper
from oaikit import OAI, ChatCompletionHandler

LIMIT_DS_SEND_MSG = 1999
def iter_blocks(content, block_size=LIMIT_DS_SEND_MSG):
    for i in range(0, len(content), block_size):
        yield content[i:i + block_size]




class DSClient(BaseClientDS):
    def __init__(self, *, cfg_ds: CfgDS, intents: Intents, **options):
        super().__init__(cfg_ds=cfg_ds, intents=intents, **options)
        self.oai = OAI(api_key=os.getenv("OAI_API_KEY"))
    
    async def on_ready(self) -> None:
        print(f"Logged on as: {self.user}")

    @on_message_wrapper
    async def on_message(self, msg_ds: MsgDS) -> None:
        if not self.cfg_ds.is_author_allowed(msg_ds=msg_ds):
            return
        
        ctx = await self.get_context(msg_ds.message)
        if ctx.command:
            print("----> Process commands.")
            await self.process_commands(msg_ds.message)
            return
        
        msgs_ds = await self.get_last_msgs_ds(msg_ds=msg_ds, leak_by_author=True)
        cfg_channel = self.cfg_ds.cfg_from_channel_id(channel_id=msg_ds.channel_id)
        msgs_oai = await self.msgs_oai_from_ds(msgs_ds=msgs_ds, cfg_channel=cfg_channel)

        response = self.oai.completions.create(messages=[m.model_dump() for m in msgs_oai], model=cfg_channel.model)
        response_handler = ChatCompletionHandler(response=response)

        # Por si la respuesta es demaciado grande.
        l_partial = 0
        for i, content_block in enumerate(iter_blocks(response_handler.message.content)):
            l_block = len(content_block)
            l_content = len(response_handler.message.content)
            l_partial += l_block
            usage_prompt = response.usage.prompt_tokens
            usage_resp = response.usage.completion_tokens
            usage_total = response.usage.total_tokens
            # TODO: Poner precio en oaikit.
            print(f"{i}. {l_partial}/{l_content} | usage | {usage_prompt}+{usage_resp}={usage_total}")
            await self.send_message(channel=msg_ds.channel, content=content_block)


path_cfg_ds = Path(os.getenv("PATH_CFG_DS"))
with open(path_cfg_ds, "r") as f:
    cfg_ds = CfgDS(**json.load(f))

client = DSClient(
    cfg_ds=cfg_ds,
    intents=get_intents(),
    command_prefix='!'
)


#@commands.has_permissions(manage_messages=True)
@client.command(name="clear")
async def _clear(ctx):
    print("----> Clear all messages.")
    await ctx.channel.purge()

client.run(os.getenv('DS_TKN'))