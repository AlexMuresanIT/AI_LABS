from csv import writer
from csv import reader

def add_column_in_csv(cale_c,cale_s,transform_row):
    with open(cale_c,"r") as citire, \
        open(cale_s,"w",newline="") as scriere:

        csv_citire=reader(citire)
        csv_scriere=writer(scriere)

        for linie in csv_citire:
            transform_row(linie,csv_citire.line_num)
            csv_scriere.writerow(linie)

cale_c="D:\\Scoala\\an3\\PYTHON_IA\\IA_LAB3\\CITIRE.txt"
cale_s="D:\\Scoala\\an3\\PYTHON_IA\\IA_LAB3\\SCRIERE.txt"
header_col_noua="Adresa"
default_text="Confidential"

add_column_in_csv(cale_c,cale_s,lambda linie,line_num: linie.append(header_col_noua)\
                  if line_num==1 else linie.append(default_text))






