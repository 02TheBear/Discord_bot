from urllib import request
import json


from api_settings_and_keys.api_keys import *
from weather_api_settings import *
from countries_codes import *


def weather():
    url = f"https://api.openweathermap.org/data/2.5/weather?q={setting_city.lower()},{setting_countries_code.lower()}&appid={weather_api_key}"

    json_dict_list = request.urlopen(url)
    dict_list = json.load(json_dict_list)
    print(dict_list)
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
            temporary = wind_dict["wind"]["direction"]

    dict_list["wind"]["deg"] = temporary

    if dict_list["clouds"]["all"] < 100:
        dict_list["wind"]["all"] = "mycket målnigt"
    elif dict_list["clouds"]["all"] < 75:
        dict_list["wind"]["all"] = "måtligt målnigt"
    elif dict_list["clouds"]["all"] < 50:
        dict_list["wind"]["all"] = "något målnigt"
    elif dict_list["clouds"]["all"] < 25:
        dict_list["wind"]["all"] = "lätt målnigt"

    print(
        f"""I {dict_list["name"]},{dict_list["sys"]["country"]} är det {dict_list["main"]["temp"]} grader och en {dict_list["wind"]["speed"]}m/s vind i en {dict_list["wind"]["deg"]} riktning, det är också {dict_list["wind"]["all"]}."""
    )


def weather_city(city, countries):

    if countries:
        pass
    elif len(countries) == 2:
        code = countries
    else:
        code = countries_list[countries]

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city.lower()},{countries_code.lower()}&appid={weather_api_key}"

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
            temporary = wind_dict["wind"]["direction"]

    dict_list["wind"]["deg"] = temporary

    if dict_list["clouds"]["all"] < 100:
        dict_list["wind"]["all"] = "mycket målnigt"
    elif dict_list["clouds"]["all"] < 75:
        dict_list["wind"]["all"] = "måtligt målnigt"
    elif dict_list["clouds"]["all"] < 50:
        dict_list["wind"]["all"] = "något målnigt"
    elif dict_list["clouds"]["all"] < 25:
        dict_list["wind"]["all"] = "lätt målnigt"

    print(
        f"""I {dict_list["name"]},{dict_list["sys"]["country"]} är det {dict_list["main"]["temp"]} grader och en {dict_list["wind"]["speed"]}m/s vind i en {dict_list["wind"]["deg"]} riktning, det är också {dict_list["wind"]["all"]}."""
    )


weather()
