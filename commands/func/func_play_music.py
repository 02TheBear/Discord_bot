import discord
from discord.ext import commands
import os
import urllib.request
import urllib.parse
import re
import asyncio
import youtube_dl
from discord.utils import get
from discord import FFmpegPCMAudio
import validators


class func_play_music(commands.Cog):
    def __intit__(self, client):
        self.client = client

    @commands.command()
    async def play(self, ctx, url: str):
        if ctx.message.author.voice:
            await ctx.message.author.voice.channel.connect()
        else:
            pass
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
        voice = get(ctx.voice_client, guild=ctx.guild)
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
            if validators.url(url):
                pass
            else:
                query_string = urllib.parse.urlencode({"search_query": url})
                html_content = urllib.request.urlopen(
                    "http://www.youtube.com/results?" + query_string
                )
                search_results = re.findall(
                    r"href=\"\/watch\?v=(.{11})", html_content.read().decode()
                )
                url = "http://www.youtube.com/watch?v=" + str(search_results[0])

            print(url)
            ydl.download([url])
        for file in os.listdir("./"):
            if file.endswith(".mp3"):
                os.rename(file, "song.mp3")
        voice.play(discord.FFmpegPCMAudio("song.mp3"))
        voice.volume = 20
        voice.is_playing()


def setup(client):
    client.add_cog(func_play_music(client))
