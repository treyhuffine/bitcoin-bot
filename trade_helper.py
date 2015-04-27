from numpy import *
import urllib2
import json

# portfolio value and current shares and unique
def get_price_history(asset_url):
    asset_json = json.load(urllib2.urlopen(asset_url))['values']
    #return asset_json
    times = []
    prices = []
    for i in range(0, len(asset_json)):
        times.append(asset_json[i]['x'])
        prices.append(asset_json[i]['y'])

    return array([prices, times])

# Get the current price by pulling the JSON
def get_current_price(asset_url):
    asset_json = json.load(urllib2.urlopen(asset_url))
    time = asset_json['values'][-1]['x']
    price = asset_json['values'][-1]['y']
    return array([price, time])

# Append the current price to the price time series
def append_prices(price_series, current_price):
    return column_stack([price_series, current_price])
