import csv

director=("D:\\Scoala\\an3\\PYTHON_IA\\FISIERE_DE_LUCRU")
fisier="\data_banknote.csv"
cale=director+fisier

file=open(cale)
print(file)
print(type(file))

cititor=csv.reader(file)
print(cititor,"\n")

header=next(file)
print(header)

linii=[]
i=0
for x in cititor:
    linii.append(x)
    i+=1
    if i<=3:
        print(linii)
print(i)
print(len(linii))
print(linii[0])
print(linii[1000])
