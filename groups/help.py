from typing import Any
import discord
from discord.ext import commands
from discord import app_commands


class CustomHelpCommand(app_commands.commands):
    """
    """
    def __init__(self, **options: Any) -> None:
        super().__init__(**options)


# Save old help command and create a new one
async def setup(bot:commands.Bot):
    bot.old_help = bot.help_command
    bot.help_command = CustomHelpCommand()


