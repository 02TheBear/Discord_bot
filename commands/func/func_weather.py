import discord
from discord.ext import commands

import json
from urllib import request


from settings import (
    setting_city,
    setting_countries_code,
    temprature_scale,
)
from commands.api.api_func.func_weather_api import weather, city_weather


class func_weather(commands.Cog):
    def __intit__(self, client):
        self.client = client

    @commands.command()
    async def weather(self, ctx):
        weather_info = weather()
        print(weather_info)
        await ctx.send(
            f"""Weather Report:\nWeather: :{weather_info["weather_icon"]}:\nWind: {weather_info["wind_speed"]}\nWind Direction: {weather_info["wind_direction"]}\nTemprature: {weather_info["temp"]}"""
        )

    @commands.command()
    async def city_weather(self, ctx, city, countries_code):
        weather_info = city_weather(city, countries_code)
        await ctx.send(
            f"""Weather Report:\nWeather: :{weather_info["weather_icon"]}:\nWind: {weather_info["wind_speed"]}\nWind Direction: {weather_info["wind_direction"]}\nTemprature: {weather_info["temp"]}"""
        )


def setup(client):
    client.add_cog(func_weather(client))
