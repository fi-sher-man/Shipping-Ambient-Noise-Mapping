import csv
import numpy as np
import pandas as pd
from haversine import haversine
from pyram.PyRAM import PyRAM

from extractspeed import depths, extract_speeds, update_speeds
from extractbathy import extract_bathy

ref = pd.read_csv("Reference Coordinates.csv")


def run_pyram(freq, dist, z_ss, rp_ss, cw, attn, rbzb, dr = 500, dz = 500, c0 = 1600):
    """
    function to run the pyram model
    returns the transmission loss between tx and rx
    """
    zr = 15
    zs = 15
    z_sb=np.array([0])
    rp_sb=np.array([0])
    cb=np.array([[1700]])
    rhob=np.array([[1.5]])
    pyram = PyRAM(freq, zs, zr, z_ss, rp_ss, cw, z_sb, rp_sb, cb, rhob, attn, rbzb, dr = dr, dz = dz, c0 = c0)

    pyram.run()

    m = near(pyram.tll, 1000 * dist)

    return pyram.tll[m]


def last_el(array):
    """
    Extends the array by substituting the last element
    """
    for i in range(len(array)):
        if array[i] == 0:
            break
        a = array[i]
    return a

def near(array, value):
    """
    gets the nearest range for which tl is calculated to the actual distance
    """
    array= np.asarray(array)
    idx = np.argmin(np.abs(array - value))

    return idx


with open("Book1.csv") as f:
    lines = f.readlines()

trans_losses = []

freq = int(input())
for i in range(len(ref)):
    if len(lines[i]) == 1:
        #if there are no ships, total_tl is set to 0
        trans_losses.append(0)
        continue
    else:
        x = [int(j) for j in lines[i].split(",")]
        total_tl = 0

        rx_lat, rx_long = ref["LATITUDE"][i], ref["LONGITUDE"][i]
        #estimate the TL for rach ship present
        for index in x:
            tx_lat, tx_long = ref["LATITUDE"][index], ref["LONGITUDE"][index]
            dist = 1000 * haversine((tx_lat, tx_long), (rx_lat, rx_long))
            #get z_ss
            z_ss = depths()

            #get rp_ss
            rp_ss = update_speeds(tx_lat, rx_long, rx_lat, rx_long)

            #get cw
            cw = extract_speeds(tx_lat, tx_long, rx_lat, rx_long)
            cw[:, 0][np.where(cw[:, 0]==0)[0]] = last_el(cw[:, 0])
            cw[:, 1][np.where(cw[:, 1]==0)[0]] = last_el(cw[:, 1])
            #get rbzb
            rbzb = extract_bathy(tx_lat, tx_long, rx_lat, rx_long)

            #attn - source: Hamilton 1976
            if rbzb[0, 0] < 700:
                at = 0.15
            elif rbzb[0,0] < 1600:
                at = 0.047
            else:
                at = 0.016
            attn=np.array([[at]])
            tl = run_pyram(freq, dist, z_ss, rp_ss, cw, attn, rbzb)
            total_tl = 10 * np.log10((10**(total_tl/10)) + (10**(tl/10)))

        #appenfing the total_tl to a list
        trans_losses.append(total_tl)

        if i%100==0:
            print(i, "Done")

ref["Total Loss"] = trans_losses
ref.to_csv("Reference Coordinates.csv")
