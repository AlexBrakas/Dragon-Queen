from typing import Any
import discord
from discord.ext import commands
from discord import app_commands


class CustomHelpCommand(app_commands.commands):
    """
    """
    def __init__(self, **options: Any):
        super().__init__(**options)


async def setup(bot:commands.Bot):
    bot.old_help = bot.help_command
    bot.help_command = CustomHelpCommand()


