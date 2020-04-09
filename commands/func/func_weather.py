import discord
from discord.ext import commands

import json
from urllib import request


from settings import (
    setting_city,
    setting_countries_code,
    temprature_scale,
)


class func_weather(commands.Cog):
    def __intit__(self, client):
        self.client = client

    # @commands.command()
    # async def weather(self, ctx):
    #    weather()
    #    await ctx.send(
    #        f"""
    #        Weather Report:\nWeather: :{weather_info_dict["weather_icon"]}:\nWind: {weather_info_dict["wind_speed"]}\nWind Direction: {weather_info_dict["wind_direction"]}\nTemprature: {weather_info_dict["temp"]}
    #        """
    #    )

    # @commands.command()
    # async def weather_city(self, ctx, city, countries_code):
    #    weather()
    #    await ctx.send(
    #        f"""
    #        Weather Report:\nWeather: :{weather_info_dict["weather_icon"]}:\nWind: {weather_info_dict["wind_speed"]}\nWind Direction: {weather_info_dict["wind_direction"]}\nTemprature: {weather_info_dict["temp"]}
    #        """
    #    )


def setup(client):
    client.add_cog(func_weather(client))
