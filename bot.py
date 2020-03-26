# Important imports
import discord
from discord.ext import commands

# Imports important for commands
import asyncio
import youtube_dl
import time
import random
import os

# Local imports
from settings import prefix

# Import hidden keys and tokens
from auth import token

client = commands.Bot(command_prefix=prefix)
client.remove_command("help")


@client.event
async def on_ready():
    print("Logged in as")
    print(client.user.name)
    print(client.user.id)
    print("------")


@client.event
async def on_guild_join(member):
    print(f"A person joined a server {member}!")


@client.event
async def on_guild_remove(member):
    print(f"A person left a server {member}!")


@client.command()
async def load(ctx, extension):
    client.load_extension(f"commands.func.{extension}")


@client.command()
async def unload(ctx, extension):
    client.unload_extension(f"commands.func.{extension}")


for filename in os.listdir("./commands/func"):
    if filename.endswith(".py"):
        client.load_extension(f"commands.func.{filename[:-3]}")

# Ping
@client.command()
async def ping(ctx):
    start_time = time.time()
    await ctx.send(f"Pong!\n{int(client.latency * 1000)}ms")


# DM command
@client.command()
async def send_dm(ctx, member: discord.Member, *, content):
    channel = await member.create_dm()
    await channel.send(f"{content}\nFrom: {ctx.message.author}")


# Help command
@client.command()
async def help(ctx, message):
    await ctx.message.author.send(
        f"**Hello {ctx.message.author}!**\nI am Lester, here is some commands you may need:\n\n **Music Commanads:**\n§play <song name/yt-link>, §start , §stop, §queue <song name/yt-link>, §skip\n\n**Weather Commands:**\n§weather, §weather <city>\n\n**Timer and Alarm Commands:**\n§timer <time>, §alarm <time>\n\n **Statistic Commands:**\n§stats csgo <player/link>, §stats rs6 <player/link>\n\n **Other Commands:**\n§tts <text>, §einar, §help\n\nThis are some commands that will help you with my key features. For more information visit: https://github.com/02TheBear/Discord_bot.py/blob/master/README.md"
    )
    await client.delete_message(message)


# Music play command
@client.command()
async def play(ctx, content):
    voice = await ctx.message.author.voice.channel.connect()
    search_song = " ".join(content[1:1])
    url = f"https://www.youtube.com/watch?v={search_song}"
    player = await voice.create_ytdl_player(url)
    player.start()


# Random number command
@client.command()
async def random_number(ctx, content):
    if type(content) == int or type(content) == float:
        number = random.randint(0, int(content))
    else:
        await ctx.send(f"{content} is not a valid number")


if __name__ == "__main__":
    client.run(token)
