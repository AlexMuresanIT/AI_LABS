import pandas as pd
from sklearn import linear_model
from sklearn.model_selection import train_test_split


DF=pd.read_csv("D:\\Scoala\\an3\\PYTHON_IA\\Fisiere_de_lucru2\\LUCRARI_5\\case_preturi.csv")

X=DF[["condition","grade","yr_built","floors","sqft_living"]]
y=DF[["price"]]

print("Media conditiei este:",DF[["condition"]].mean(axis=0))
print("Media gradului este:",DF[["grade"]].mean(axis=0))
print("Media anului in care a fost construit este:",DF[["yr_built"]].mean(axis=0))
print("Media etajelor este:",DF[["floors"]].mean(axis=0))
print("Media suprafetei este:",DF[["sqft_living"]].mean(axis=0))

print()
print("Predictia asupra pretului unui apartament:")
regr=linear_model.LinearRegression()
regr.fit(X.values,y.values)
price_prev=regr.predict([[3,7,1971,1.5,2079]])
print(int(price_prev),"euro")

print()
train_x,train_y,test_x,test_y=list(train_test_split(X.values,y.values,test_size=50,random_state=50))
print("VALORI ANTRENANTE")
print("1",train_x)
print("2",train_y)
print("VALORI TESTATE")
print("3",test_x)
print("4",test_y)












