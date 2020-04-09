import discord
from discord.ext import commands
import random
import asyncio


class func_randomint(commands.Cog):
    def __intit__(self, client):
        self.client = client

    # Random number command
    @commands.command()
    async def random(self, ctx, number):
        try:
            arg = random.randint(1, int(number))
        except ValueError:
            await ctx.send("Invalid number")
        else:
            await ctx.send(str(arg))


def setup(client):
    client.add_cog(func_randomint(client))
