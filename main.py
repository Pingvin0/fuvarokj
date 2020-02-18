#﻿taxi_id;indulas;idotartam;tavolsag;viteldij;borravalo;fizetes_modja
#   0      1         2        3         4        5          6
fuvarok = [i.rstrip().replace(",",".").split(";") for i in [x for x in open("fuvar.csv", "r")][1:]]


print("3.feladat",len(fuvarok))


tfuvarok = [i for i in fuvarok if i[0] == "6185"]
dollar = sum([float(i[4])+float(i[5]) for i in tfuvarok])
print("4.feladat", len(tfuvarok), "fuvar alatt", str(dollar)+"$")

fizetesek = dict()

for i in fuvarok:
	if i[6] not in fizetesek:
		fizetesek[i[6]] = 0
	fizetesek[i[6]] += 1
print("5.feladat")
for i in fizetesek:
	val = fizetesek[i]
	print(i,val)
	
	
print("6.feladat", round(sum([float(i[3])*1.6 for i in fuvarok]), 2) ,"km")
lht = 0
def setlht(num, fullind):
	global lht
	if(num > lht):
		lht = num
		return [num,fullind]


lh = [setlht(int(i[2]), i) for i in fuvarok if int(i[2]) > lht]
lh = lh[len(lh)-1][1]
print("7.feladat")
print("	Fuvar hossza:",lh[2],"másodperc")
print("	Taxi azonosító:",lh[0])
print("	Megtett távolság:",lh[3],"km")
print("	Viteldíj:",lh[4],"$")
hibak = open("hibak.txt", "w", encoding="UTF-8")
hibak.write("﻿taxi_id;indulas;idotartam;tavolsag;viteldij;borravalo;fizetes_modja\n")
[hibak.write(";".join(i)+"\n") for i in fuvarok if float(i[4]) > 0 and float(i[2]) > 0 and float(i[3]) == 0]
hibak.close()
print("8.feladat hibak.txt")