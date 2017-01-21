import json
import math

__author__ = "Anton Khartishov"
__license__ = "GPL"
__version__ = "0.1.3"
__maintainer__ = "Anton Khartishov"
__email__ = "night-fog@bk.ru"


def read_bars_data_from_file(file_path):
    try:
        with open(file_path, encoding='utf-8') as json_data:
            data = json.load(json_data)
    except FileNotFoundError:
            print("Caption or Id keys was not found in dataset")
            raise
    return data


def get_biggest_bar(data):
    biggest_bar = max(data, key=lambda x: x.get("SeatsCount"))
    return biggest_bar.get("Name")


def get_smallest_bar(data):
    smallest_bar = min(data, key=lambda x: x.get("SeatsCount"))
    return smallest_bar.get("Name")


def get_closest_bar(data, longitude, latitude):
    closest_bar = min(data, key=lambda k:
                      math.sqrt((k.get("geoData").get("coordinates")[0] -
                                 longitude) ** 2 +
                                (k.get("geoData").get("coordinates")[1] -
                                 latitude) ** 2))
    return closest_bar.get("Name")


bars = read_bars_data_from_file('moscowBars.json2')
print("Biggest bar is :" + get_biggest_bar(bars))
print("Smallest bar is :" + get_smallest_bar(bars))
current_location = [input("Enter your latitude: "),
                    input("Enter your longitude: ")]
try:
    nearest_bar_name = get_closest_bar(bars, float(current_location[0]),
                                       float(current_location[1]))
    print("Nearest bar is : " + nearest_bar_name)
except ValueError:
    print("Coordinates type mismatch")
    exit(1)
