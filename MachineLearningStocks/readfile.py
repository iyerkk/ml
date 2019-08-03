import csv
csvfile = open('SNP500.csv', 'rt')
csvReader = csv.reader(csvfile, delimiter=",")
csvreader = csv.reader(csvfile)
#d = dict()
l =  list()
for row in csvReader:
	#d[row[1]] = row[0]
	l.append((row[2]))
#print(d)
print(l)