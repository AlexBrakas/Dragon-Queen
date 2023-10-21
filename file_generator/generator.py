import discord
from discord.ext import commands
from discord import app_commands
from typing import Optional

"""
TODO:
- Define types that can be passed like just text or more personalized etc.
- Add special characters like --append to determine special affects (add as option?)

"""

#Change, needs to create py file
class custom_commands(app_commands.command): #Change setup, custom_commands is not the class as the name would be then custom_commands-command_name
    def __init__(self, bot: discord.Bot, interaction: discord.Interaction, guild: discord.Guild) -> None:
        super().__init__()
        self.user = interaction.user
        self.bot = bot
        self.interaction = interaction
        self.guild = guild
    
    @app_commands.command(name="add", description="")
    @app_commands.checks.has_permissions(manage_messages=True)
    @app_commands.describe(options="Options for command") #alter text
    @app_commands.describe(name="Name of command")
    @app_commands.describe(action="Action for coammand")
    def add(self, interaction: discord.Interaction, name: str, options: Optional[str] = None):
        self.__setattr__() #create functions/apps_commands
        self.__getattribute__() #check no pre-existing command exists
        dir(self) # Lists attr