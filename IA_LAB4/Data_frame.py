import pandas as pd
#lista
lst=["a","b","c","d","e","f","g"]

df=pd.DataFrame(lst)
#print(df)

#dictionar de liste
data1={"Nume":["Toma","Nicu","Ion","George"],
       "Varsta":[20,21,19,18]}

df1=pd.DataFrame(data1)
#print(df1)

data2={"Nume":["Fanuc","UR","ABB","Kuka"],
       "Vechime":[27,24,22,32],
       "Adresa":["Japonia","Danemarca","Suedia","Gemania"],
        "Model":["A","B","C","D"]}

df3=pd.DataFrame(data2)
print(df3[["Nume","Adresa"]])
