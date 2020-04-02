import discord
from discord.ext import commands


class func_send_dm(commands.Cog):
    def __intit__(self, client):
        self.client = client

    @commands.command()
    async def send_dm(self, ctx, member: discord.Member, *, content):
        channel = await member.create_dm()
        await channel.send(f"{content}\nFrom: {ctx.message.author}")


def setup(client):
    client.add_cog(func_send_dm(client))
