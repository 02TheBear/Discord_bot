import discord
from discord.ext import commands
from auth import token

from discord.ext import commands

client = commands.Bot(command_prefix="§")


@client.event
async def on_ready():
    print("Ready to go")


# @client.event
# async def on_message(message):
#    if str(message.author) != "Lester.py#3460":
#        print(message.author)
#        await message.channel.send("Hi!")


@client.event
async def on_guild_join(member):
    print(f"hi {member}!")


@client.event
async def on_guild_remove(member):
    print(f"bye {member}!")


@client.command()
async def ping(ctx):
    await ctx.send(f"Pong! {}")


client.run(token)

