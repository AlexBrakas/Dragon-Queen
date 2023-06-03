import discord
from discord.ext import commands
from discord import app_commands
import json


class Bap(app_commands.Group):

    def __init__(self, bot:commands.Bot):
        super().__init__()
        self.bot = bot
        with open("emojis.json", "r") as file:
            data = json.load(file)
            name = data["bap_name"]
            id = data["bap_id"]
            self.bap_emoji = f"<a:{name}:{id}>"

    @app_commands.command(name="join", description="Well to bap city")
    async def join(self, interaction: discord.Interaction):
        await interaction.response.send_message("You have joined the game!")

    @app_commands.command(name="leave", description="Why are you running away?")
    async def leave(self, interaction: discord.Interaction):
        await interaction.response.send_message("You have abandoned the baps")

    @app_commands.command(name="start", description="let the bapping begin")
    async def start(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"Let the baps begin {self.bap_emoji}")
