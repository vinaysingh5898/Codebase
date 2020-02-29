import csv

with open('label.csv','w',newline='') as f:
	thewriter = csv.writer(f)

	for i in range(0,27):
		thewriter.writerow(["F_"+str(i),"F"])
	for i in range(0,26):
		thewriter.writerow(["MW_"+str(i),"MW"])