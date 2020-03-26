import discord
from discord.ext import commands


class func_core(commands.Cog):
    def __intit__(self, client):
        self.client = client

    @commands.command()
    async def join(self, ctx):
        if ctx.message.author.voice:
            await ctx.message.author.voice.channel.connect()

    @commands.command()
    async def leave(self, ctx):
        await ctx.guild.voice_client.disconnect()


def setup(client):
    client.add_cog(func_core(client))
