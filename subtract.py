import csv
nl=["NL"]
finalappend=[]
with open("Reference _Coordinates.csv",mode='r') as read:
	reader =csv.DictReader(read)
	for row in reader:
		nl.append(float(row["SL"])-float(row["Total Loss"]))
with open("Reference _Coordinates.csv",mode='r') as read:
	i=0
	getter=csv.reader(read)
	for row in getter:
		finalappend.append(row)
		finalappend[i].append(nl[i])
		i+=1
with open("Reference _Coordinates.csv",mode='w') as write:
	writer=csv.writer(write)
	writer.writerows(finalappend)