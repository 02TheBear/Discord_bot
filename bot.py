import discord
from discord.ext import commands
from auth import token

client = commands.Bot(command_prefix="§")


@client.event
async def on_ready():
    print("Ready to go")


@client.event
async def on_message(message):
    #    await client.send(message.channel, "hi")
    pass


@client.event
async def on_member_join(member):
    print(f"hi {member}")


@client.event
async def on_member_remove(member):
    print(f"bye {member}")


@client.command()
async def ping(ctx):
    await ctx.send("Pong!")


client.run(token)

