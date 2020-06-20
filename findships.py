import csv
feilds=[]
maxFeildLength=0
with open('Reference Coordinates.csv', mode='r') as csv_file :
	csv_reader = csv.DictReader(csv_file)
	line1=0
	k=0
	for rowref in csv_reader:
		feilds.append([])
		if line1==0:
		    #print(f'Column names are {", ".join(row)}')
			line1+=1
			continue
		# 	k=0
		line_count=0
		l=open('AIS_Old3.csv',mode='r')
		csv_ships = csv.DictReader(l)
		for row in csv_ships:
			if line_count==0:
	           # print(f'Column names are {", ".join(row)}')
				line_count+=1
				continue
			#print([row["LAT"],row["LON"]])
			if float(row["LAT"])-float("0")>=float(rowref["LATITUDE"])-float("0")-0.5 and float(row["LAT"])-float("0")<=(float(rowref["LATITUDE"])-float("0")+0.5) and float(row["LON"])-float("0")<=float(rowref["LONGITUDE"])-float("0")+0.5 and float(row["LON"])>=float(float(rowref["LONGITUDE"])-0.5):
				feilds[line1].append(line_count)
			line_count+=1
		if len(feilds[line1])!=0:
			print(feilds[line1])
		l.close()
		maxFeildLength=max(maxFeildLength,len(feilds[line1]))
		k+=line_count
		line1+=1

with open('Book1.csv', mode='w',newline="") as csv_file :
    writer = csv.writer(csv_file)
    for i in range(len(feilds)):
    	writer.writerow(feilds[i])
