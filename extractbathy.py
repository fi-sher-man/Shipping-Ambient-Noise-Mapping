import numpy as np 
import pandas as pd 
from haversine import haversine

bathy = pd.read_excel("area.xlsx")
#df = pd.read_csv("data.csv")

def nearest(array1, array2, value1, value2):
    #find the nearest lat long present in the speeds df for both the tx and rx

    array1 = np.asarray(array1)
    array2 = np.asarray(array2)
    idx = np.argmin(np.abs(array1 - value1) + np.abs(array2 - value2))

    return idx  

def extract_bathy(tx_lat, tx_long, rx_lat, rx_long):
    #extract the depths pertaining to tx and rx
    #for rbzb

    m = nearest(bathy["LATITUDE"], bathy["LONGITUDE"], tx_lat, tx_long)
    n = nearest(bathy["LATITUDE"], bathy["LONGITUDE"], rx_lat, rx_long)

    a = np.zeros((2, 2))
    a[0,0] = 0
    a[1, 0] = haversine((tx_lat, tx_long), (rx_lat, rx_lat))
    a[0, 1] = bathy["Dmax"][m]
    a[1, 1] = bathy["Dmax"][n]
    a[:, 1] = np.abs(a[:, 1])
        

    return a

#print(extract_bathy(df["Tx lat"][0], df["Tx long"][0], df["Rx lat"][0], df["Rx long"][0]))