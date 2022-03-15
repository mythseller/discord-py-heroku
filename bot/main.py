import os
import discord
from datetime import datetime
from discord.ext import commands

bot = commands.Bot(command_prefix="!")
TOKEN = os.getenv("DISCORD_TOKEN")


@bot.listen()
async def on_ready():
    print(f"Logged in as {bot.user.name}({bot.user.id})")


@bot.listen()
async def on_message(message):
    if message.author.bot:
        return
    guild = message.guild
    # Fetch target channels
    target1_channel = guild.get_channel(879466084116336660)
    target2_channel = guild.get_channel(882606056184897536)
    target3_channel = guild.get_channel(879468481492447254)
    target4_channel = guild.get_channel(879467246953570305)
    # Fetch target roles
    role_1 = guild.get_role(942052888333676634)
    role_2 = guild.get_role(942051860167159819)
    role_3 = guild.get_role(942052324615004250)
    role_4 = guild.get_role(942052501228777493)
    role_5 = guild.get_role(942052699921321984)
    role_6 = guild.get_role(942052789100617728)
    role_7 = guild.get_role(950706317482410015)

    if role_1 in message.role_mentions:
        msg = message.content.strip(f"<@&{role_1.id}>")
        embed = discord.Embed(
            title="Market Commentary",
            description=msg,
            color=0x0be60b,
            timestamp=datetime.now(),
        )
        embed.add_field(name="Index:", value=role_1.mention)
        embed.set_author(
            name=message.author.display_name, icon_url=message.author.avatar_url
        )
        await target2_channel.send(embed=embed)
        await message.channel.send(embed=embed)

    elif role_2 in message.role_mentions:
        msg = message.content.strip(f"<@&{role_2.id}>")
        embed = discord.Embed(title=msg, color=0x349434, timestamp=datetime.now())
        embed.add_field(name="Trade Type:", value=role_2.mention)
        embed.set_author(
            name=message.author.display_name, icon_url=message.author.avatar_url
        )
        await target1_channel.send(embed=embed)
        await message.channel.send(embed=embed)

    elif role_3 in message.role_mentions:
        msg = message.content.strip(f"<@&{role_3.id}>")
        embed = discord.Embed(title=msg, color=0x782ea6, timestamp=datetime.now())
        embed.add_field(name="Trade Type:", value=role_3.mention)
        embed.set_author(
            name=message.author.display_name, icon_url=message.author.avatar_url
        )
        await target1_channel.send(embed=embed)
        await message.channel.send(embed=embed)
        
    elif role_4 in message.role_mentions:
        msg = message.content.strip(f"<@&{role_4.id}>")
        embed = discord.Embed(title=msg, color=0xc45a25, timestamp=datetime.now())
        embed.add_field(name="Trade Type:", value=role_4.mention)
        embed.set_author(
            name=message.author.display_name, icon_url=message.author.avatar_url
        )
        await target1_channel.send(embed=embed)
        await message.channel.send(embed=embed)
        
    elif role_5 in message.role_mentions:
        msg = message.content.strip(f"<@&{role_5.id}>")
        embed = discord.Embed(title=msg, color=0xe31e87, timestamp=datetime.now())
        embed.add_field(name="Trade Type:", value=role_5.mention)
        embed.set_author(
            name=message.author.display_name, icon_url=message.author.avatar_url
        )
        await target1_channel.send(embed=embed)
        await message.channel.send(embed=embed)
        
    elif role_6 in message.role_mentions:
        msg = message.content.strip(f"<@&{role_6.id}>")
        embed = discord.Embed(title=msg, color=0xe0dd12, timestamp=datetime.now())
        embed.add_field(name="Trade Type:", value=role_6.mention)
        embed.set_author(
            name=message.author.display_name, icon_url=message.author.avatar_url
        )
        await target3_channel.send(embed=embed)
   
    elif role_7 in message.role_mentions:
        msg = message.content.strip(f"<@&{role_7.id}>")
        embed = discord.Embed(title="some dumb shit", description=msg, color=0xe31e87, timestamp=datetime.now())
        embed.add_field(name="we goin", value=role_7.mention)
        embed.set_author(
            name=message.author.display_name, icon_url=message.author.avatar_url
        )
        
        await target4_channel.send(embed=embed)
        message2 = await message.channel.send(embed=embed)
        await message2.add_reaction(":smile:")


@bot.listen()
async def on_message(message):
  '''simple on message to respond if a message containing "hello" is sent'''
  # prevent bot from answering other bots, including self
  if message.author.bot:
     return
  # create message content and channel variables
  content = message.content.lower()
  channel = message.channel
  # check if message includes "hello"
  if 'hello' in content:
    msg = await channel.send('HI!')
    await msg.add_reaction(':heart:')
    
@bot.command()
async def ping(ctx):
    await ctx.send("pong")


if __name__ == "__main__":
    bot.run(TOKEN)
