import discord
from os import getenv
from discord.ext import commands
from discord import app_commands
import asyncio
#from dotenv import load_dotenv

import cogs
import groups
from prefix import get_prefix
from emojis import Emoji_collection as ec

#load_dotenv()



"""
TODO:

ADD command to load/unload slash commands or specific command

"""


creator_id = int(getenv('my_id'))
ang_id = int(getenv('ang_id'))

owner_ids = {creator_id, ang_id}
TOKEN = getenv('Discord_token')
my_guild = discord.Object(id=getenv("server_id"))
app_id = getenv("app_id")

intents = discord.Intents().all()
bot = commands.Bot(command_prefix = commands.when_mentioned, owner_ids=owner_ids, intents=intents, application_id=app_id)
tree = bot.tree

bot.remove_command('help')

#prevents bot from responding to self
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    await bot.process_commands(message)

@tree.command(name="clear", description="Removes given number of messages", guild=my_guild)
@app_commands.checks.has_permissions(manage_messages=True)
@app_commands.describe(amount="Number of messages to remove")
async def clear(interaction:discord.Interaction, amount:int):
    await interaction.response.defer(thinking=True)
    hstry = [message async for message in interaction.channel.history(limit=amount+1)]
    await interaction.channel.delete_messages(hstry[1::])
    await asyncio.sleep(0.2)
    await interaction.followup.send(f"{amount} messages have been kicked off the server")

#Catch error if they are NOT an admin
@tree.error #app.commands.MissingPermissions error
#@clear.error
async def on_error(interaction:discord.Interaction, error):
    print(error)
    await interaction.response.send_message("Are you the great Ang??? **DIDN'T THINK SO**")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        return

@bot.command()
async def grab(ctx:commands.Context, name:str):
    try:
        response = getattr(emoji_collection, name)
        await ctx.send(response)
    except AttributeError as ae:
        await ctx.send(f"That doesn't exist {emoji_collection.NF_bonk}")

#waits till the bot is ready
@bot.event
async def on_ready():
    print('\nLogged in as ', end="")
    print(bot.user.name)
    print('------\n')
    
    for file in cogs.cog_list:
        await bot.load_extension(f'cogs.{file}')


    #bot.change_presence(activity=discord.CustomActivity())
    #bot.tree.add_command(groups.Bap(bot), guild=my_guild)
    #await tree.sync(guild=my_guild)

emoji_collection = ec(bot=bot, guild=my_guild)


if __name__ == '__main__':
    bot.run(TOKEN)