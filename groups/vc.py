import discord
from discord.ext import commands
from discord import app_commands
import emojis
import nacl

class vc(app_commands.Group):

    def __init__(self, bot:commands.Bot):
        super().__init__()
        self.bot = bot
        self.vc = None

    @app_commands.command(name="join", description="joins the VC")
    async def join(self, interaction: discord.Interaction):
        if not interaction.user.voice:
            await interaction.response.send_message("You are not in a VC", delete_after=10)
        else:
            if self.vc != None:
                await interaction.response.send_message("???")
            else:
                self.vc = await interaction.user.voice.channel.connect()
                await interaction.response.send_message("I'm here!!", delete_after=5)

    @app_commands.command(name="leave", description="Leaves the VC")
    async def leave(self, interaction: discord.Interaction):
        if self.vc == None:
            await interaction.response.send_message("I am not in a VC", delete_after=10)
        else:
            await self.vc.disconnect()
            self.vc = None
            await interaction.response.send_message("Goodbye!", delete_after=5)