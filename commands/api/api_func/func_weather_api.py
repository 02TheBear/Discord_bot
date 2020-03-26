from urllib import request
import json
from cmds.api.api_func.api_setting_and_keys.api_keys import weather_api_key
from cmds.api.api_func.api_setting_and_keys.weather_api_settings import (
    setting_city,
    setting_countries_code,
)
from list_and_dicts.countries_codes import countries_list


def weather():

    url = f"https://api.openweathermap.org/data/2.5/weather?q={setting_city.lower()},{setting_countries_code.lower()}&appid={weather_api_key}"

    json_dict_list = request.urlopen(url)
    dict_list = json.load(json_dict_list)
    zero_degrees = 273.15

    # Reformating
    dict_list["main"]["temp"] -= zero_degrees
    dict_list["main"]["temp"] = round(dict_list["main"]["temp"], 1)

    wind_dict = {
        "NE": {"min_deg": 23, "max_deg": 68, "direction": "nordöstlig"},
        "E": {"min_deg": 68, "max_deg": 113, "direction": "östlig"},
        "SE": {"min_deg": 113, "max_deg": 158, "direction": "sydöstlig"},
        "S": {"min_deg": 158, "max_deg": 203, "direction": "sydlig"},
        "SW": {"min_deg": 203, "max_deg": 248, "direction": "sydvästlig"},
        "W": {"min_deg": 248, "max_deg": 293, "direction": "västlig"},
        "NW": {"min_deg": 293, "max_deg": 338, "direction": "nordvästlig"},
    }
    temporary_wind_direction = "nordlig"
    for wind_direction in wind_dict:
        if (
            int(dict_list["wind"]["deg"]) < wind_dict[wind_direction]["min_deg"]
            and int(dict_list["wind"]["deg"]) < wind_dict[wind_direction]["max_deg"]
        ):
            temporary_wind_direction = wind_dict["wind"]["direction"]

    dict_list["wind"]["deg"] = temporary_wind_direction

    if dict_list["clouds"]["all"] < 100:
        temporary_cloud_amount = "mycket målnigt"
    elif dict_list["clouds"]["all"] < 75:
        temporary_cloud_amount = "måtligt målnigt"
    elif dict_list["clouds"]["all"] < 50:
        temporary_cloud_amount = "något målnigt"
    elif dict_list["clouds"]["all"] < 25:
        temporary_cloud_amount = "lätt målnigt"

    dict_list["clouds"]["all"] = temporary_cloud_amount

    return dict_list
