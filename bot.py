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


@client.command()
async def weather(ctx):

    url = f"https://api.openweathermap.org/data/2.5/weather?q={setting_city},{setting_countries_code}&appid={weather_api_key}"

    json_dict_list = request.urlopen(url)
    dict_list = json.load(json_dict_list)
    zero_degrees = 273.15

    # Reformating
    dict_list["main"]["temp"] -= zero_degrees
    dict_list["main"]["temp"] = int(dict_list["main"]["temp"])

    wind_dict = {
        "NE": {"min_deg": 23, "max_deg": 68, "direction": "nordöstlig"},
        "E": {"min_deg": 68, "max_deg": 113, "direction": "östlig"},
        "SE": {"min_deg": 113, "max_deg": 158, "direction": "sydöstlig"},
        "S": {"min_deg": 158, "max_deg": 203, "direction": "sydlig"},
        "SW": {"min_deg": 203, "max_deg": 248, "direction": "sydvästlig"},
        "W": {"min_deg": 248, "max_deg": 293, "direction": "västlig"},
        "NW": {"min_deg": 293, "max_deg": 338, "direction": "nordvästlig"},
    }
    temporary = "nordlig"
    for wind_direction in wind_dict:
        if (
            int(dict_list["wind"]["deg"]) < wind_dict[wind_direction]["min_deg"]
            and int(dict_list["wind"]["deg"]) < wind_dict[wind_direction]["max_deg"]
        ):
            temporary = wind_dict[wind_direction]["direction"]

    dict_list["wind"]["deg"] = temporary

    if dict_list["clouds"]["all"] < 100:
        dict_list["wind"]["all"] = "mycket målnigt"
    elif dict_list["clouds"]["all"] < 75:
        dict_list["wind"]["all"] = "måtligt målnigt"
    elif dict_list["clouds"]["all"] < 50:
        dict_list["wind"]["all"] = "något målnigt"
    elif dict_list["clouds"]["all"] < 25:
        dict_list["wind"]["all"] = "lätt målnigt"
    await ctx.send(dict_list)


client.run(token)

