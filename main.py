#﻿taxi_id;indulas;idotartam;tavolsag;viteldij;borravalo;fizetes_modja
#   0      1         2        3         4        5          6
fuvarok = [i.rstrip().replace(",",".").split(";") for i in [x for x in open("fuvar.csv", "r")][1:]]
print("3.feladat",len(fuvarok))
tfuvarok = [i for i in fuvarok if i[0] == "6185"]
dollar = sum([float(i[4])+float(i[5]) for i in tfuvarok])
print("4. feladat", len(tfuvarok), "alatt", str(dollar)+"$")
fizetesek = dict()
fizetesek["bankkártya"] = 0
fizetesek["készpénz"] = 0
fizetesek["vitatott"] = 0
fizetesek["ingyenes"] = 0
fizetesek["ismeretlen"] = 0

for i in fuvarok:
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
