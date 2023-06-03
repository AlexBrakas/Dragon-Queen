from typing import Any, Optional, Type
import aiohttp
import discord
from discord.ext import commands
from discord import app_commands
import asyncio
from discord.ext.commands.bot import PrefixType, _default
from discord.ext.commands.help import HelpCommand

from discord.types.embed import EmbedType

class CustomBot(commands.AutoShardedBot):
    class Embed(discord.Embed):
        def __init__(self, **kwargs):
            colour = kwargs.pop("colour", discord.Colour.green())
            super().__init__(**kwargs, colour=colour)
        
    def __init__(self, **kwargs) -> None:
        
        super().__init__(**kwargs, case_insensitive = True, strip_after_prefix=True)