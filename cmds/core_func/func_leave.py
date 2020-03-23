import discord
from discord.ext import commands

client = commands.Bot(command_prefix="§")


@client.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()
