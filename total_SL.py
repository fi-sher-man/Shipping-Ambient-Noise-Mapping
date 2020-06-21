from mywittekind import wittekind
import csv
import numpy as np
import pandas as pd
print("input the frequency again please:")
f=input()
sl=[0]
count=0
headers=[]
with open('Wittekind_Inputs.csv',mode="r") as inp:
	inpreader=csv.DictReader(inp)
	for row in inpreader:
		if count==0:
			count=1
			continue
		sl.append(wittekind(float(f),float(row["Vessel speed"]),float(row["Cavitation Speed"]),float(row["DWT"]),float(row["Block Coefficient"]),float(row["Engine Mass"]),float(row["no. of engines"]),float(row["Engine mounting parameter"])))
ans=[0]
count=0
#print(sl)
with open('book1.csv',mode="r") as indexes:
	ships=csv.reader(indexes)
	for row in ships:
		if count==0:
			count=1
			continue
		total_sl=0
		for ship in row:
			total_sl=10 * np.log10((10**(total_sl/10)) + (10**(sl[int(ship)]/10)))
		ans.append(total_sl)

with open('Wittekind_Inputs.csv',mode="r") as inp:
	inpreader=csv.DictReader(inp)
	for row in inpreader:
		if count==0:
			count=1
			continue

finalappend=[]
with open('Reference Coordinates.csv',mode='r') as read:
	reader=csv.reader(read)
	i=0
	for row in reader:
		finalappend.append([]) 
		finalappend[i]=(row)
		i+=1
#print(len(finalappend))

with open('Reference Coordinates.csv',mode='w',newline="") as write:
	writer=csv.writer(write)
	i=0
	for row in range(len(finalappend)):
		if i==0:
			finalappend[i].append("SL")
			i=1
			writer.writerow(finalappend[0])
			continue
		finalappend[i].append(ans[i])
		#print(finalappend[i])
		writer.writerow(finalappend[i])
		i+=1
