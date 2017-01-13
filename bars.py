# -*- coding: utf-8 -*-
import urllib2
import json

MOSCOW_BARS_DATA_INFO = "http://api.data.mos.ru/v1/datasets/1796"
API_ROWS_MAX = 500


def load_data(filepath):
    bars_info_url_resp = urllib2.urlopen(filepath)
    bars_data_info = json.loads(bars_info_url_resp.read())
    bars_count = bars_data_info["ItemsCount"]
    bars_list = []
    for i in range(bars_count//API_ROWS_MAX+1):
        get_bars_list_url = filepath + "/rows?$top=" + str(API_ROWS_MAX) + "&$skip=" + str((i+1)*API_ROWS_MAX)
        bars_data_req = urllib2.urlopen(get_bars_list_url)
        bars_data_dict = json.loads(bars_data_req.read())
        for j in range(len(bars_data_dict)):
            bars_list.append(bars_data_dict[j])
    return bars_list


def get_biggest_bar(data):
    biggest_bar_name = None
    biggest_bar_seats_count = 0
    for i in range(len(data)):
        bar_seats_count = data[i].get("Cells").get("SeatsCount")
        if bar_seats_count > biggest_bar_seats_count or biggest_bar_name is None:
            biggest_bar_seats_count = bar_seats_count
            biggest_bar_name = data[i].get("Cells").get("Name")
    return biggest_bar_name


def get_smallest_bar(data):
    smallest_bar_name = ""
    smallestbar_seats_count = None
    for i in range(len(data)):
        bar_seats_count = data[i].get("Cells").get("SeatsCount")
        if bar_seats_count < smallestbar_seats_count or smallestbar_seats_count is None:
            smallestbar_seats_count = bar_seats_count
            smallest_bar_name = data[i].get("Cells").get("Name")
    return smallest_bar_name


def get_closest_bar(data, longitude, latitude):
    nearest_bar_name = None
    nearest_bar_k = None
    for i in range(len(data)):
        bar_coord = data[i].get("Cells").get("geoData").get("coordinates")
        bar_k = abs(bar_coord[0]-longitude) + abs(bar_coord[1]-latitude)
        if nearest_bar_k is None or bar_k < nearest_bar_k:
            nearest_bar_name = data[i].get("Cells").get("Name")
            nearest_bar_k = abs(bar_coord[0]-longitude) + abs(bar_coord[1]-latitude)
    return nearest_bar_name

barsList = load_data(MOSCOW_BARS_DATA_INFO)
print ("Biggest bar is " + get_biggest_bar(barsList))
print ("Smallest bar is " + get_smallest_bar(barsList))
current_location = [input("Enter your latitude: "), input("Enter your longitude: ")]
print ("Nearest bar is " + get_closest_bar(barsList, current_location[0], current_location[1]))
