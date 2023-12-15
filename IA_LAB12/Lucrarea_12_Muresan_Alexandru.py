import math

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error

#VIZUALIZARE DATE DE INTRARE
t_min=pd.read_csv("temperaturi_min.csv",header=0,index_col=0)
#print(t_min.head(5))
"""fix,ax=plt.subplots(1,1,figsize=(20,5))
plt.plot(t_min,color="red")
plt.title("Valori cu temperaturi minime")"""


t_max=pd.read_csv("temperaturi_max.csv",header=0,index_col=0)
#print(t_max.head(5))
"""fix1,ax1=plt.subplots(1,1,figsize=(20,5))
plt.plot(t_max,color="blue")
plt.title("Valori cu temperaturi minime")"""

#Vizualizare date de intrare de pe a doua coloana
t_min=pd.read_csv("temperaturi_min.csv",usecols=[1],engine="python")
t_max=pd.read_csv("temperaturi_max.csv",usecols=[1],engine="python")

plt.plot(t_min,color="red")
plt.plot(t_max,color="blue")
#plt.show()

def create_data(dataset,look_back=1):
    dataX,dataY=[],[]
    for i in range(len(dataset)-look_back-1):
        a=dataset[i:(i+look_back),0]
        dataX.append(a)
        dataY.append(dataset[i+look_back,0])
    return np.array(dataX),np.array(dataY)

np.random.seed(7)

#incarcam seturile de date
df1=pd.read_csv("temperaturi_min.csv",usecols=[1],engine="python")
dataset1=df1.values
dataset1=dataset1.astype("float32")

df2=pd.read_csv("temperaturi_max.csv",usecols=[1],engine="python")
dataset2=df2.values
dataset2=dataset2.astype("float32")

#normalizam seturile de data
scaler=MinMaxScaler(feature_range=(0,1))
dataset1=scaler.fit_transform((dataset1))

scaler=MinMaxScaler(feature_range=(0,1))
dataset2=scaler.fit_transform((dataset2))

#impartim datele pentru testare si antrenare
train_size1=int(len(dataset1)*0.70)
test_size1=len(dataset1)-train_size1

train_size2=int(len(dataset2)*0.70)
test_size2=len(dataset2)-train_size2

train1,test1=dataset1[0:train_size1,:],dataset1[train_size1:len(dataset1),:]
train2,test2=dataset2[0:train_size2,:],dataset2[train_size2:len(dataset2),:]

look_back=1
trainX1,trainY1=create_data(train1,look_back)
trainX2,trainY2=create_data(train2,look_back)

testX1,testY1=create_data(test1,look_back)
testX2,testY2=create_data(test2,look_back)

trainX1=np.reshape(trainX1,(trainX1.shape[0],1,trainX1.shape[1]))
testX1=np.reshape(testX1,(testX1.shape[0],1,testX1.shape[1]))

trainX2=np.reshape(trainX2,(trainX2.shape[0],1,trainX2.shape[1]))
testX2=np.reshape(testX2,(testX2.shape[0],1,testX2.shape[1]))

#creem modelul RNN cu LSTM
model=Sequential()
model.add(LSTM(4,input_shape=(1,look_back)))
model.add(Dense(1))
model.compile(loss="mean_squared_error",optimizer="adam")
model.fit(trainX1,trainY1,epochs=10,batch_size=1,verbose=2)
model.fit(trainX2,trainY2,epochs=10,batch_size=1,verbose=2)

#facem predictii
train1Predict=model.predict(trainX1)
test1Predict=model.predict(testX1)

train2Predict=model.predict(trainX2)
test2Predict=model.predict(testX2)

#inversam predictiile
train1Predict=scaler.inverse_transform(train1Predict)
train2Predict=scaler.inverse_transform(train2Predict)

trainY1=scaler.inverse_transform([trainY1])
trainY2=scaler.inverse_transform([trainY2])

test1Predict=scaler.inverse_transform(test1Predict)
test2Predict=scaler.inverse_transform(test2Predict)

#testY1=scaler.inverse_transform(testY1)
#testY2=scaler.inverse_transform(testY2)

"""train1Score=math.sqrt(mean_squared_error(trainY1[0],train1Predict[:,0]))
print("Scor antrenare pentru primul set",train1Score)
train2Score=math.sqrt(mean_squared_error(trainY2[0],train2Predict[:,0]))
print("Scor antrenare pentru al doilea set",train2Score)

test1Score=math.sqrt(mean_squared_error(testY1[0],test1Predict[:,0]))
print("Scor testare pentru primul set",test1Score)
test2Score=math.sqrt(mean_squared_error(testY2[0],test2Predict[:,0]))
print("Scor testare pentru primul set",test2Score)"""

train1PredictPlot=np.empty_like(dataset1)
train1PredictPlot[:,:]=np.nan
train1PredictPlot[look_back:len(train1Predict)+look_back,:]=train1Predict

train2PredictPlot=np.empty_like(dataset2)
train2PredictPlot[:,:]=np.nan
train2PredictPlot[look_back:len(train2Predict)+look_back,:]=train2Predict

test1PredictPlot=np.empty_like(dataset1)
test1PredictPlot[:,:]=np.nan
test1PredictPlot[len(train1Predict)+(look_back*2)+1:len(dataset1)-1,:]=test1Predict

test2PredictPlot=np.empty_like(dataset2)
test2PredictPlot[:,:]=np.nan
test2PredictPlot[len(train2Predict)+(look_back*2)+1:len(dataset2)-1,:]=test2Predict

#plotam predictiile
fix1,ax1=plt.subplots(1,1,figsize=(20,5))
plt.plot(scaler.inverse_transform(dataset1))
plt.plot(train1PredictPlot)
plt.plot(test1PredictPlot)
plt.title("Predictia temperaturilor minime")

fix2,ax2=plt.subplots(1,1,figsize=(20,5))
plt.plot(scaler.inverse_transform(dataset2))
plt.plot(train2PredictPlot)
plt.plot(test2PredictPlot)
plt.title("Predictia temperaturilor maxime")
plt.show()
