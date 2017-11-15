import json
import requests
import matplotlib.pyplot as plt
import datetime
import pandas as pd
import numpy as np
# URL: https://api.kraken.com/0/public/Ticker

# Send the request to the Kraken API  
def API_request(request):
    r = requests.get(request) 
    json_data = json.loads(r.text)  
    return json_data

# print tradable pair assets info
#print(API_request("https://api.kraken.com/0/public/AssetPairs"))

# list of tradable pairs
Asset_Pair_List = [
 'XETCXXBT'
,'XETHXXBT'
,'XICNXXBT'
,'XLTCXXBT'
,'XMLNXXBT'
,'XREPXXBT'
,'XXDGXXBT'
,'XXLMXXBT'
,'XXMRXXBT'
,'XXRPXXBT'
,'XZECXXBT']

"""
Pair Euro/bitcoin for portfolio valorisation
XXBTZEUR
"""


def ExtractDataFromJson(asset, interval, Date):
    uri = "https://api.kraken.com/0/public/OHLC"
    j_feed = uri + "?pair=" + asset + "&interval=" + interval
    r = requests.get(j_feed)
    json_data = json.loads(r.text)

    market_data = json_data["result"][asset]
  
    nb_element = len(market_data)
    price_list = []
    date_list = []
    scale = float(market_data[0][4])
        
    for i in range (0, nb_element):
        price_list.append(float(market_data[i][4])/scale)
        date_list.append(datetime.datetime.fromtimestamp(market_data[i][0]))  
    
    return [date_list,price_list,asset]

def GetMarketData(AssetList, Interval, Date):
    market_data =[]
    #print(len(AssetList))
    for i in range (0,len(AssetList)):
        market_data.append(ExtractDataFromJson(AssetList[i], Interval, Date))
    return market_data


def Main():
    Asset_Pair_List = ['XETCXXBT','XETHXXBT','XICNXXBT','XLTCXXBT','XMLNXXBT'
                      ,'XREPXXBT','XXDGXXBT','XXLMXXBT','XXMRXXBT','XXRPXXBT'
                      ,'XZECXXBT']
    data = GetMarketData(Asset_Pair_List,"15","1508778000")
    
    #Data = GetMarketData(Asset_Pair_List, "15")
    #print(Data[0])
    X_Axis = []
    for i in range (0,len(data[0])):
        X_Axis.append(i)
    plt.figure()
    for i in range (0, len(data)):
        plt.plot(data[i][0], data[i][1], label=data[i][2])
    plt.draw()
    plt.show()
    
Main()