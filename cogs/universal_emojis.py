import discord
from discord.ext import commands

"""
Has a repository of emojis that can be uploaded and named
"""

class Emoji_storage(commands.Cog):
    def __init__(self, bot):
        super().__init__()
        self.bot = bot


async def setup(bot):
    await bot.add_cog(Emoji_storage(bot))