import pandas as pd
import numpy as np

data=pd.read_csv("D:\\Scoala\\an3\\PYTHON_IA\\Fisiere_de_lucru2\\LUCRARI_4\\baza_date_carti.csv",index_col="Identifier")
df=pd.DataFrame(data,columns=["Identifier","Place of Publication","Date of Publication","Publisher","Title","Author","Flickr URL"])
print(df)


df["Date of Publication"]=df["Date of Publication"].str.replace("[","")
df["Date of Publication"]=df["Date of Publication"].str.replace("]","")
df["Date of Publication"]=df["Date of Publication"].str.replace(",","")
df["Date of Publication"]=df["Date of Publication"].str.replace("-","")
df["Date of Publication"]=df["Date of Publication"].str.replace("?","")
print(df["Date of Publication"])

df["Author"]=df["Author"].str.replace(".","")
df["Author"]=df["Author"].str.replace(",","")
df["Author"]=df["Author"].str.replace("-","")
df["Author"]=df["Author"].str.replace("*","")
df["Author"]=df["Author"].str.replace("|","")
df["Author"]=df["Author"].str.replace("(","")
df["Author"]=df["Author"].str.replace(")","")
print(df["Author"])

cifre=("1234567890")

df["Place of Publication"]=df["Place of Publication"].str.replace("?","")
df["Place of Publication"]=df["Place of Publication"].str.replace("]","")
df["Place of Publication"]=df["Place of Publication"].str.replace("1234567890","")
df["Place of Publication"]=df["Place of Publication"].str.replace("'","")
df["Place of Publication"]=df["Place of Publication"].str.replace("[","")
df["Place of Publication"]=df["Place of Publication"].str.replace("'","")
print(df["Place of Publication"])


df["Title"]=df["Title"].str.replace("]","")
df["Title"]=df["Title"].str.replace("[","")
df["Title"]=df["Title"].str.replace(".","")
df["Title"]=df["Title"].str.replace("(","")
df["Title"]=df["Title"].str.replace(")","")
df["Title"]=df["Title"].str.replace(";","")
print(df["Title"])

df=df.replace(" ",np.nan)

df.to_csv("D:\\Scoala\\an3\\PYTHON_IA\\Fisiere_de_lucru2\\LUCRARI_4\\baza_date_carti_modificat.csv")


data=pd.read_csv("D:\\Scoala\\an3\\PYTHON_IA\\Fisiere_de_lucru2\\LUCRARI_4\\jocuri_olimpice.csv")
c=pd.DataFrame(data)
print(c.head())

dict={"NaN":"Tara","? Summer":"Jocuri Olimpice Vara","01 !":"Aur","02 !":"Argint","03 !":"Bronz","? Winter":"Jocuri Olimpice Iarna","01 !.1":"Aur","02 !.1":"Argint","03 !.1":"Bronz","? Games":"# Jocuri","01 !.2":"Aur","02 !.2":"Argint","03 !.2":"Bronz"}
c2=c.rename(columns=dict)
c2.to_csv("D:\\Scoala\\an3\\PYTHON_IA\\Fisiere_de_lucru2\\LUCRARI_4\\jocuri_olimpice.csv")
