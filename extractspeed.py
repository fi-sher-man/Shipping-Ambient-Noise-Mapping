import numpy as np 
import pandas as pd 
from haversine import haversine

#df = pd.read_csv("data.csv")
speeds = pd.read_excel("speed/done2007-17_apr_jun_output.xlsx")

def nearest(array1, array2, value1, value2):
    #find the nearest lat long present in the speeds df for both the tx and rx

    array1 = np.asarray(array1)
    array2 = np.asarray(array2)
    idx = np.argmin(np.abs(array1 - value1) + np.abs(array2 - value2))

    return idx



def depths():
    #for z_ss
    return np.arange(0, 5600, 500)

def extract_speeds(tx_lat, tx_long, rx_lat, rx_long):
    #extract the rows pertaining to the tx and rx
    #for cw
    f = depths()
    m = nearest(speeds["LATITUDE"], speeds["LONGITUDE"], tx_lat, tx_long)
    n = nearest(speeds["LATITUDE"], speeds["LONGITUDE"], rx_lat, rx_long)

    a = np.zeros((f.shape[0], 2))

    for i in range(f.shape[0]):
        a[i, 0] = speeds.iloc[m][f[i]]
        a[i, 1] = speeds.iloc[n][f[i]]
    
    return a

def update_speeds(tx_lat, tx_long, rx_lat, rx_long):
    #update just once
    #for rp_ss

    return np.array([0, haversine((tx_lat, tx_long), (rx_lat, rx_long))])

#print(extract_speeds(df["Tx lat"][0], df["Tx long"][0], df["Rx lat"][0], df["Rx long"][0]))