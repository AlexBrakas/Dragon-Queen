import discord
from discord.ext import commands
from requests import get
from discord.ui import button
from discord import ButtonStyle
import os

"""
Gets the image attament of previous messages and checks for stickers to pull back info and upload to another server
"""

class Steal_Buttons(discord.ui.View):
    def __init__(self, stickers:list, pos:int, ctx:commands.Context):
        super().__init__(timeout=None)
        self.stickers = stickers
        self.pos = pos
        self.ctx = ctx

    @button(label="<", style=ButtonStyle.blurple, custom_id='persistent_back')
    async def back(self, interaction:discord.Interaction, 
                   btn: discord.ui.Button):
        if self.pos > 0:
            self.pos-=1
            embed = await embed_maker(stickers=self.stickers, 
                                      color=discord.Color.blue(), 
                                      ctx=self.ctx, page_num=self.pos)

            await interaction.response.edit_message(embed=embed, view=self)

        else:
            await interaction.response.send_message("""Already at the first 
                                                    one found""", 
                                                    ephemeral=True)

    @button(label=">", style=ButtonStyle.blurple, custom_id='forward')
    async def forward(self, interaction:discord.Interaction,
                      btn: discord.ui.Button):
        
        if self.pos < len(self.stickers)-1:
            self.pos+=1
            embed = await embed_maker(stickers=self.stickers, 
                                      color=discord.Color.blue() , 
                                      ctx=self.ctx, page_num=self.pos)
            
            await interaction.response.edit_message(embed=embed, view=self)

        else:
            await interaction.response.send_message("""Already at the last one found, 
                                                    target a bigger search to go further""",
                                                      ephemeral=True)

    @button(label="STEAL!", style=ButtonStyle.blurple, custom_id='steal')
    async def steal(self, interaction:discord.Interaction, btn:discord.ui.Button):
        try:
            for each_sticker in self.ctx.guild.stickers:
                if each_sticker.name == self.stickers[self.pos][3]:
                    await self.ctx.send("name already exists", ephemeral=True)
                    raise Exception("Name already exists")

            await get_image(self.stickers[self.pos], self.ctx.guild)
            embed = await embed_maker(stickers=self.stickers, color=discord.Color.green(), ctx=self.ctx, page_num=self.pos)
            embed.set_footer(text=f"Success!\n{self.pos+1}/{len(self.stickers)}")
            await interaction.response.edit_message(embed=embed)
        
        except Exception as e:
            print(e)
            embed = await embed_maker(stickers=self.stickers, color=discord.Color.red(), ctx=self.ctx, page_num=self.pos)
            embed.set_footer(text=f"Failed!\n{self.pos+1}/{len(self.stickers)}")
            await interaction.response.edit_message(embed=embed, view=self)


class Stickers(commands.Cog):
    def __init__(self, bot):
        super().__init__()
        self.bot = bot

    @commands.has_permissions(manage_emojis_and_stickers=True)
    @commands.command(pass_context=True)
    async def steal(self, ctx:commands.Context, amount:int=2):
        self.stickers = []
        async for message in ctx.channel.history(limit=amount+1):
            msg = await ctx.channel.fetch_message(message.id)
            if msg.stickers:
                sticker_data = await msg.stickers[0].fetch()
                temp = (sticker_data.url,
                        sticker_data.id,
                        sticker_data.emoji,
                        sticker_data.name,
                        sticker_data.description)
                self.stickers.append(temp)

        if len(self.stickers) > 0:
            try:
                await ctx.send(embed=await embed_maker(self.stickers, ctx=ctx, color=discord.Color.blue(), page_num=0), 
                               view=Steal_Buttons(stickers=self.stickers, pos=0, ctx=ctx))

            except Exception as e:
                print(e)
                await ctx.send("an unexpected error happened (what did you do to my poor bot???)")
        else:
            await ctx.send(f"There are no stickers in the last {amount+1} messages")
    
    @steal.error
    async def steal_error(self, ctx:commands.Context):
        pp_fire = 1091493045763047434
        emoji = self.bot.get_emoji(pp_fire)
        await ctx.send(f"Who the ***FUCK*** are you??? <:{emoji.name}:{emoji.id}>")

async def get_image(sticker_data, guild):
    img_bytes = get(sticker_data[0], allow_redirects=True, stream=True).content
    file_name = f"{sticker_data[3]}.png".replace(" ", "_")
    with open(file_name, "wb") as file:
        file.write(img_bytes)
    
    await guild.create_sticker(name=sticker_data[3], description=sticker_data[4], 
                                emoji=sticker_data[2], file=discord.File(file_name), reason="Ang said so")
    os.remove(file_name)
        
async def embed_maker(stickers, color, ctx:commands.Context, page_num:int):
    embed = discord.Embed(description="Steal those STICKERS!", color=color)
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.display_avatar) #display_avatar is for profile in that guild, default_avatar is general
    sticker_length = len(stickers)
    embed.set_footer(text=f"{page_num+1}/{sticker_length}")
    embed.set_image(url=stickers[page_num][0])
    return embed

async def setup(bot):
    await bot.add_cog(Stickers(bot))