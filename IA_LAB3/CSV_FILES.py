import requests
import csv

with open("C:/Users/oscar_age_female.csv")as csvfile:
    mpg=list(csv.DictReader(csvfile))

print(len(mpg))
#print(mpg[0].keys())
print(mpg[4].keys())

nume=set(d["Index"] for d in mpg)
"""print(nume)

nume = set(d[' "Year"'] for d in mpg)
print(nume)

nume= set(d[' "Age"'] for d in mpg)
print(nume)"""

print(mpg[:3])
print(mpg[0].keys())
x=sum(float(d[' "Age"']) for d in mpg)/len(mpg)
print("Varsta medie: ",x)

y=sum(float(d[' "Year"']) for d in mpg)/len(mpg)
print("Media an", y)



