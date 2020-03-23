import discord
from discord.ext import commands


class core:
    def __intit__(self, client):
        self.client = client

    @commands.command()
    async def join(self):
        if self.message.author.voice:
            await self.message.author.voice.channel.connect()


def setup(client):
    client.add_cog(core(client))
