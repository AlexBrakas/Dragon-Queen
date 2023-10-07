import json
import discord
from discord.ext import commands
from discord.types.emoji import Emoji as BuiltEmojis
import yaml

class Emojis(BuiltEmojis):
    personal: bool


# create dectorator for personal option that must be a authorized users

class Emoji_collection():
    def __init__(self, *, bot:commands.Bot, guild:discord.Guild, **kwargs):
        self._bot:commands.Bot = bot
        self._guild:discord.Guild = guild
        with open("emojis.yaml", "r") as file:
            __data:dict = yaml.safe_load(file)
            for key, value in __data.items():
                setattr(self, key, self.create_emoji(value))

    def create_emoji(self, emoji_data):
        tmp = discord.Emoji(guild=self._guild, state=self._bot._connection, data={
            'id':int(emoji_data[1]),
            'name':emoji_data[0],
            'animated':bool(emoji_data[2])
        })
        return tmp

    def add_emoji(self, new_emoji):
        with open("emojis.json", "+") as file:
            __data:dict = yaml.safe_load(file)
            