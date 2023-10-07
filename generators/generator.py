import discord
from discord.ext import commands
from discord import app_commands

"""
TODO:
- Define types that can be passed like just text or more personalized etc.
- Add special characters like --append to determine special affects (add as option?)

"""

class custom_commands(app_commands.command):
    def __init__(self, bot: discord.Bot, interaction: discord.Interaction) -> None:
        super().__init__()
        self.user = interaction.user
        self.bot = bot
        self.interaction = interaction