import json
import math

__author__ = "Anton Khartishov"
__license__ = "GPL"
__version__ = "0.1.4"
__maintainer__ = "Anton Khartishov"
__email__ = "night-fog@bk.ru"


def read_bars_data_from_file(file_path):
    try:
        with open(file_path, encoding='windows-1251') as json_data:
            data = json.load(json_data)
    except FileNotFoundError:
        print("File " + file_path + " not found")
        exit(1)
    except UnicodeDecodeError:
        print("Wrong file encoding. Use windows-1251.")
        exit(1)
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

moscow_bars_json = input("Enter json file path: ")
bars = read_bars_data_from_file(moscow_bars_json)

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
