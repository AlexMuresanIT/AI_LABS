from pandas import read_csv
import numpy as np
from keras.models import Sequential
from keras.layers import Dense,SimpleRNN
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
import math
import matplotlib.pyplot as plt

def clasic_RNN(hidden_units,dense_units,input_shape,activation):
    model=Sequential()
    model.add(SimpleRNN(hidden_units,input_shape=input_shape,
                        activation=activation[0]))
    model.add(Dense(units=dense_units,activation=activation[1]))
    model.compile(loss="mean_squared_error",optimizer="adam")
    return model

demo_model=clasic_RNN(2,1,(3,1),activation=["linear","linear"])
print(demo_model.summary())

wx=demo_model.get_weights()[0]
wh=demo_model.get_weights()[1]
bh=demo_model.get_weights()[2]
wy=demo_model.get_weights()[3]
by=demo_model.get_weights()[4]

print("wx=",wx,"wh=",wh,"bh=",bh,"wy=",wy,"by=",by)

x=np.array([1,2,3])
x_input=np.reshape(x,(1,3,1))
y_pred_model=demo_model.predict(x_input)

m=2
h0=np.zeros(m)
h1=np.dot(x[0],wx)+h0+bh
h2=np.dot(x[1],wx)+np.dot(h1,wh)+bh
h3=np.dot(x[2],wx)+np.dot(h2,wh)+bh
o3=np.dot(h3,wy)+by

print("h1=",h1,"h2=",h2,"h3=",h3)

print("Predictie retea",y_pred_model)
print("Predictie calcul",o3)

def date_train_test(url,split_percent=0.8):
    df=read_csv(url,usecols=[1],engine="python")
    data=np.array(df.values.astype("float32"))
    scaler=MinMaxScaler(feature_range=(0,1))
    data=scaler.fit_transform(data).flatten()
    n=len(data)

    split=int(n*split_percent)
    train_data=data[range(split)]
    test_data=data[split:]
    return train_data,test_data,data

sunspots_url="https://raw.githubusercontent.com/jbrownlee/Datasets/master/monthly-sunspots.csv"
train_data,test_data,data=date_train_test(sunspots_url)
print("total date:",len(data))
print("date instruire",len(train_data),"data testare:",len(test_data))
print(max(data),min(data))

def pachet_XY(dat,time_steps):
    Y_ind=np.arange(time_steps,len(dat),time_steps)
    Y=dat[Y_ind]

    rows_x=len(Y)
    X=dat[range(time_steps*rows_x)]
    X=np.reshape(X,(rows_x,time_steps,1))
    return X,Y

time_steps=24
trainX,trainY=pachet_XY(train_data,time_steps)
testX,testY=pachet_XY(test_data,time_steps)

model=clasic_RNN(hidden_units=10,dense_units=1,input_shape=(time_steps,1),
                 activation=["tanh","tanh"])
model.fit(trainX,trainY,epochs=20,batch_size=1,verbose=2)
print(model.summary())

def afisare_eroare(trainY,testY,train_predict,test_predict):
    train_rmse=math.sqrt(mean_squared_error(trainY,train_predict))
    test_rmse=math.sqrt(mean_squared_error(testY,test_predict))

    print("Train RMSE",train_rmse)
    print("Test RMSE", test_rmse)

train_predict=model.predict(trainX)
test_predict=model.predict(testX)

afisare_eroare(trainY,testY,train_predict,test_predict)

def grafic(trainY,testY,train_predict,test_predict,culoare_1,culoare_2,culoare_3):
    actual=np.append(trainY,testY)
    predictions=np.append(train_predict,test_predict)
    rows=len(actual)
    plt.figure(figsize=(15,6),dpi=80)
    plt.plot(range(rows),actual,color=culoare_1)
    plt.plot(range(rows), predictions, color=culoare_2)
    plt.axvline(x=len(trainY),color=culoare_3)
    plt.legend(["Actual","Predictie"])
    plt.xlabel("Observatii dupa time_steps dati")
    plt.ylabel("Spoturi solare (scalate)")
    plt.title("Valori efective si estimate. Linia verticala separa seturile de instruire si testare")
    plt.show()

grafic(trainY,testY,train_predict,test_predict,"green","red","blue")
