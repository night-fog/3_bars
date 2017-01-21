import json
import math
import argparse

__author__ = "Anton Khartishov"
__license__ = "GPL"
__version__ = "0.1.5"
__maintainer__ = "Anton Khartishov"
__email__ = "night-fog@bk.ru"


def read_bars_data_from_file(file_path):
    try:
        with open(file_path, encoding='windows-1251') as json_bars_data:
            bars_data = json.load(json_bars_data)
            return bars_data
    except FileNotFoundError:
        print("File " + file_path + " not found")
        exit(1)
    except UnicodeDecodeError:
        print("Wrong file encoding. Use windows-1251.")
        exit(1)


def get_biggest_bar(data):
    biggest_bar = max(data, key=lambda bar: bar.get("SeatsCount"))
    return biggest_bar.get("Name")


def get_smallest_bar(data):
    smallest_bar = min(data, key=lambda bar: bar.get("SeatsCount"))
    return smallest_bar.get("Name")


def get_closest_bar(data, longitude, latitude):
    closest_bar = min(data, key=lambda bar:
                      math.sqrt((bar.get("geoData").get("coordinates")[0] -
                                longitude) ** 2 +
                                (bar.get("geoData").get("coordinates")[1] -
                                latitude) ** 2))
    return closest_bar.get("Name")

parser = argparse.ArgumentParser(
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description='''\
    Read data from json file, set in first argument.
    Find the largest bar in data.
    Find the smallest bar in data.
    Find the nearest bar by latitude and longitude.''')
parser.add_argument('file_path', metavar='bars.json', type=str,
                    help='path to the json file with bars data')

args = parser.parse_args()
bars = read_bars_data_from_file(args.file_path)
print("Biggest bar is : " + get_biggest_bar(bars))
print("Smallest bar is : " + get_smallest_bar(bars))
try:
    current_location = [float(input("Enter your latitude: ")),
                        float(input("Enter your longitude: "))]
    nearest_bar_name = get_closest_bar(bars, current_location[0],
                                       current_location[1])
    print("Nearest bar is : " + nearest_bar_name)
except ValueError:
    print("Coordinates type mismatch")
    exit(1)
