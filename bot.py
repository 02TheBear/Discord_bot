# Important imports
import discord
from discord.ext import commands

# Imports important for commands
import asyncio
import youtube_dl
import time
import random
import os
from discord.utils import get
from discord import FFmpegPCMAudio

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


# extensions
@client.command()
async def load(ctx, extension):
    client.load_extension(f"commands.func.{extension}")


@client.command()
async def unload(ctx, extension):
    client.unload_extension(f"commands.func.{extension}")


for filename in os.listdir("./commands/func"):
    if filename.endswith(".py"):
        client.load_extension(f"commands.func.{filename[:-3]}")

# Ping_test
@client.command()
async def ping(ctx):
    start_time = time.time()
    await ctx.send(f"Pong!\n{int(client.latency * 1000)}ms")


# Music play command
@client.command()
async def play(ctx, url: str):
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
    except PermissionError:
        await ctx.send(
            "Wait for the current playing music end or use the 'stop' command"
        )
        return
    await ctx.send("Getting everything ready, playing audio soon")
    print("Someone wants to play music let me get that ready for them...")
    voice = get(client.voice_clients, guild=ctx.guild)
    ydl_opts = {
        "format": "bestaudio/best",
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.rename(file, "song.mp3")
    voice.play(discord.FFmpegPCMAudio("song.mp3"))
    voice.volume = 100
    voice.is_playing()


if __name__ == "__main__":
    client.run(token)
