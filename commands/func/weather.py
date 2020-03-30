import discord
from discord.ext import commands

import json
from urllib import request

from commands.api.api_func.api_setting_and_keys.api_keys import weather_api_key
from settings import (
    setting_city,
    setting_countries_code,
    temprature_scale,
)


class weather(commands.Cog):
    def __intit__(self, client):
        self.client = client

    @commands.command()
    async def weather(self, ctx):
        # Weather check command
        url = f"https://api.openweathermap.org/data/2.5/weather?q={setting_city},{setting_countries_code}&appid={weather_api_key}"

        weather_info_dict = request.urlopen(url)
        weather_info_dict = json.load(weather_info_dict)
        print(weather_info_dict)
        # Reformating
        weather_info_dict["humidity"] = weather_info_dict["main"]["humidity"]
        weather_info_dict["temp"] = weather_info_dict["main"]["temp"]
        weather_info_dict["clouds"] = weather_info_dict["clouds"]["all"]
        weather_info_dict["description_weather"] = weather_info_dict["weather"][0][
            "description"
        ]
        weather_info_dict["weather_icon"] = weather_info_dict["weather"][0]["icon"]
        weather_info_dict["weather"] = weather_info_dict["weather"][0]["main"]
        weather_info_dict["wind_speed"] = weather_info_dict["wind"]["speed"]
        weather_info_dict["wind_direction"] = weather_info_dict["wind"]["deg"]
        weather_info_dict["city"] = weather_info_dict["name"]

        # Removing unused information
        del_list = (
            "coord",
            "base",
            "main",
            "wind",
            "visibility",
            "dt",
            "sys",
            "timezone",
            "id",
            "cod",
            "name",
        )

        for item in del_list:
            del weather_info_dict[item]

        # Temp reformating to celsius with one decimal
        if temprature_scale == "C":
            weather_info_dict["temp"] = -273.15
        elif temprature_scale == "F":
            weather_info_dict["temp"] = 1.8 * (weather_info_dict["temp"] - 273.15) + 32
        elif temprature_scale == "K":
            pass
        else:
            weather_info_dict["temp"] = -273.15

        weather_info_dict["temp"]
        weather_info_dict["temp"] = round(weather_info_dict["temp"], 1)

        wind_dict = {
            "NE": {"min_deg": 23, "max_deg": 68},
            "E": {"min_deg": 68, "max_deg": 113},
            "SE": {"min_deg": 113, "max_deg": 158},
            "S": {"min_deg": 158, "max_deg": 203},
            "SW": {"min_deg": 203, "max_deg": 248},
            "W": {"min_deg": 248, "max_deg": 293},
            "NW": {"min_deg": 293, "max_deg": 338},
        }
        temporary_wind = "nordlig"
        for wind_direction in wind_dict:
            if (
                int(weather_info_dict["wind_direction"])
                < wind_dict[wind_direction]["min_deg"]
                and int(weather_info_dict["wind_direction"])
                < wind_dict[wind_direction]["max_deg"]
            ):
                temporary_wind = "wind_direction"

        weather_info_dict["wind_direction"] = temporary_wind

        await ctx.send(
            f"""
            Weather Report:\nWeather: :{weather_info_dict["weather_icon"]}:\nWind: {weather_info_dict["wind_speed"]}\nWind Direction: {weather_info_dict["wind_direction"]}\nTemprature: {weather_info_dict["temp"]}
            """
        )


def setup(client):
    client.add_cog(weather(client))
