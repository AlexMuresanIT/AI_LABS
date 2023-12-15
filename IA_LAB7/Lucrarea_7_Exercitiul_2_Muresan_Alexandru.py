#METODA K-NN
import pandas as pd
from numpy import mat
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn import neighbors
from sklearn.metrics import mean_squared_error
from math import sqrt
import matplotlib.pyplot as plt
import numpy as np

data=pd.read_csv("D:\\Scoala\\an3\\PYTHON_IA\\Fisiere_de_lucru2\\LUCRARI_7\\Crypto_currency.csv")
print(data.head())
print(len(data))
verificare=data.isnull().sum()
print(verificare)
data.drop(["Date"],axis=1,inplace=True)
data.drop(["Volume"],axis=1,inplace=True)
data=pd.get_dummies(data)

data.fillna(0)
train,test=train_test_split(data,test_size=0.3)

x_train=train.drop("Close",axis=1)
y_train=train["Close"]

x_test=test.drop("Close",axis=1)
y_test=test["Close"]

scaler=MinMaxScaler(feature_range=(0,1))

x_train_scaled=scaler.fit_transform(x_train)
x_train=pd.DataFrame(x_train_scaled)

x_test_scaled=scaler.fit_transform(x_test)
x_test=pd.DataFrame(x_test_scaled)

rmse_val=[]
for K in range(20):
    K=K+1
    model=neighbors.KNeighborsRegressor(n_neighbors=K)
    model.fit(x_test,y_test)
    pred=model.predict(x_test)
    error=sqrt(mean_squared_error(y_test,pred))
    rmse_val.append(error)
    print("RMSE value for k= ",K," is", error)

curve=pd.DataFrame(rmse_val)
curve.columns=["RMSE"]
grafic=curve.plot(color="red",title="K VERSUS RMSE")
grafic.set_xlabel("Numar K vecini",color="blue")
grafic.set_ylabel("RMSE",color="blue")
plt.show()