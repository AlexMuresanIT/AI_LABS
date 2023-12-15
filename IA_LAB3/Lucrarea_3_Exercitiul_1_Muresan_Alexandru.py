from csv import writer,DictReader

lista_date=["1","Alex","Muresan"]
director="D:\\Scoala\\an3\\PYTHON_IA\\FISIERE_DE_LUCRU"
file="\\SCRIERE.csv"
cale=director+file

"""with open(cale,"a",newline="") as f:
    w=writer(f)
    w.writerow(lista_date)
    f.close()

with open(cale,"w") as f:
    w=writer(f)
    w.writerow(lista_date)
    f.close()"""
#cele doua functii sunt asemanatoare. Ambele scriu in fisier

with open(cale,"w",newline="") as f:
    for i in range(0,4):
        w=writer(f)
        w.writerow(lista_date)
# scrie in fisier de 4 ori


cap_tabel=["Nr","Nume","Subiect"]
dict={"Nr":"7","Nume":"Alex Muresan","Subiect":"Robotica"}

with open(cale,"a",newline="") as f:
    dw=DictReader(f,fieldnames=cap_tabel)

# Dict Reader nu are functia write row


