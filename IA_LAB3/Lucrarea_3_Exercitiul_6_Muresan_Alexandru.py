import csv

#1
#deschidere si citire a fisier de tip csv
with open("D:\\Scoala\\an3\\PYTHON_IA\\IA_LAB3\\data_banknote.csv") as csvfile:
    reader=csv.DictReader(csvfile)
    mpg=list(reader)
print("Tipul fisierului: ",type(csvfile))

#2
print("Datele din fisier sunt: \n",mpg)

#3
print("Numarul de linii al fisierului este: ",len(mpg))

#4
print("Capul de tabel este: \n",mpg[0].keys())

#5
print("Prima linie din fisier: \n",mpg[1])
print("A doua linie din fisier: \n",mpg[2])

#ex6
#am facut la ex 1
nume = set(d['VE'] for d in mpg)
print("Primul element este de tipul: ",type(nume))
print("Primul element contine ",len(nume)," elemente")
nume = set(d['ST'] for d in mpg)
print("Al doilea element este de tipul: ",type(nume))
print("Al doilea element contine ",len(nume)," elemente")
nume = set(d['CU'] for d in mpg)
print("Al treilea element este de tipul: ",type(nume))
print("Al treilea element contine ",len(nume)," elemente")
nume = set(d['EN'] for d in mpg)
print("Al patrulea element este de tipul: ",type(nume))
print("Al patrulea element contine ",len(nume)," elemente")
nume = set(d['C'] for d in mpg)
print("Al cincelea element este de tipul: ",type(nume))
print("Al cincelea element contine ",len(nume)," elemente")

#ex7
print(mpg[1]['CU']>mpg[200]['C'])





