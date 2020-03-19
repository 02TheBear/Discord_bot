import discord
from discord.ext import commands
from auth import token
import time
from urllib import request
import json
from cmds.api.api_func.api_setting_and_keys.api_keys import weather_api_key
from cmds.api.api_func.api_setting_and_keys.weather_api_settings import (
    setting_city,
    setting_countries_code,
)

client = commands.Bot(command_prefix="§")
client.remove_command("help")


@client.event
async def on_ready():
    print("Ready to go")


@client.event
async def on_guild_join(member):
    print(f"hi {member}!")


@client.event
async def on_guild_remove(member):
    print(f"bye {member}!")


@client.command()
async def ping(ctx):
    start_time = time.time()
    await ctx.send(f"Pong!\n{(int((time.time() - start_time)/10000)*10)}")


@client.command()
async def hi(ctx):
    await ctx.send(f"HI!")


@client.command()
async def send_dm(ctx, member: discord.Member, *, content):
    channel = await member.create_dm()
    await channel.send(content)


# join channel
@client.command()
async def join(ctx):
    if ctx.message.author.voice:
        await ctx.message.author.voice.channel.connect()


# leave channel
@client.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()


# Help command
@client.command()
async def help(ctx):
    await ctx.message.author.send(
        f"Hello I am Lester here is some commands you may need:\n\n Music Commanads:\n§play <song name/yt-link>, §start , §stop, §queue <song name/yt-link>, §skip\n\nWeather Commands:\n§weather, §weather <city>\n\nTimer and Alarm Commands:\n§timer <time>, §alarm <time>\n Statistic Commands:\n§stats csgo <player/link>, §stats rs6 <player/link>\n\n Other Commands:\n§tts <text>, §einar, §help\n\nThis are some commands that will help you with my key features. For more information visit: https://github.com/02TheBear/Discord_bot.py/blob/master/README.md"
    )


@client.command()
async def weather(ctx):

    url = f"https://api.openweathermap.org/data/2.5/weather?q={setting_city},{setting_countries_code}&appid={weather_api_key}"

    weather_info_dict = request.urlopen(url)
    weather_info_dict = json.load(weather_info_dict)
    zero_degrees = 273.15

    # Reformating
    weather_info_dict["humidity"] = weather_info_dict["main"]["humidity"]
    weather_info_dict["temp"] = weather_info_dict["main"]["temp"]
    weather_info_dict["clouds"] = weather_info_dict["clouds"]["all"]
    weather_info_dict["weather"] = weather_info_dict["weather"][0]["description"]
    # weather_info_dict["wind_speed"] = weather_info_dict[]

    # removing unused info
    del weather_info_dict["coord"]
    del weather_info_dict["base"]
    del weather_info_dict["main"]
    del weather_info_dict["visibility"]
    del weather_info_dict["dt"]
    del weather_info_dict["sys"]
    del weather_info_dict["timezone"]
    del weather_info_dict["id"]
    del weather_info_dict["cod"]

    # temp reformating to celsius 1 decimal
    weather_info_dict["temp"] -= zero_degrees
    weather_info_dict["temp"] = round(weather_info_dict["temp"], 1)

    wind_dict = {
        "NE": {"min_deg": 23, "max_deg": 68, "direction": "nordöstlig"},
        "E": {"min_deg": 68, "max_deg": 113, "direction": "östlig"},
        "SE": {"min_deg": 113, "max_deg": 158, "direction": "sydöstlig"},
        "S": {"min_deg": 158, "max_deg": 203, "direction": "sydlig"},
        "SW": {"min_deg": 203, "max_deg": 248, "direction": "sydvästlig"},
        "W": {"min_deg": 248, "max_deg": 293, "direction": "västlig"},
        "NW": {"min_deg": 293, "max_deg": 338, "direction": "nordvästlig"},
    }
    temporary_wind = "nordlig"
    for wind_direction in wind_dict:
        if (
            int(weather_info_dict["wind"]["deg"]) < wind_dict[wind_direction]["min_deg"]
            and int(weather_info_dict["wind"]["deg"])
            < wind_dict[wind_direction]["max_deg"]
        ):
            temporary_wind = wind_dict[wind_direction]["direction"]

    weather_info_dict["wind"]["deg"] = temporary_wind

    if weather_info_dict["clouds"] < 100:
        temporary_cloud = "mycket målnigt"
    elif weather_info_dict["clouds"] < 75:
        temporary_cloud = "måtligt målnigt"
    elif weather_info_dict["clouds"] < 50:
        temporary_cloud = "något målnigt"
    elif weather_info_dict["clouds"] < 25:
        temporary_cloud = "lätt målnigt"

    weather_info_dict["clouds"] = temporary_cloud

    await ctx.send(weather_info_dict)


client.run(token)

