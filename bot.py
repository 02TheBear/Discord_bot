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
import validators
*
import urllib.request
import urllib.parse
import re


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

if __name__ == "__main__":
    client.run(token)
