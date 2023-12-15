import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from math import sqrt
import keras
from keras.models import Sequential
from keras.layers import Dense


dataset=pd.read_csv("clasificare_diabet_gen_F.csv")
col_names=["De cate ori a fost gravida",
           "Concentratia plasmatica a glucozei la 2 ore intr-un test oral de toleranta la glucoza",
           "Tensiunea arteriala diastolica in mm Hg",
           "Grosimea pliului cutanat al tricepsului in mm",
           "2 ore de insulina serica in mu U/ml",
           "Indicele de masa corporala masurat ca greutate in kg/(inaltime in m)^2",
           "Functia pedigree a diabetului",
           "Varsta in ani",
           "Clasa"]
dataset.to_csv("clasificare_diabet_gen_F.csv",header=col_names,index=False)
dataset=pd.read_csv("clasificare_diabet_gen_F.csv")

feature_cols=["De cate ori a fost gravida",
                "Concentratia plasmatica a glucozei la 2 ore intr-un test oral de toleranta la glucoza",
                "Tensiunea arteriala diastolica in mm Hg",
                "Grosimea pliului cutanat al tricepsului in mm",
                "2 ore de insulina serica in mu U/ml",
             "Indicele de masa corporala masurat ca greutate in kg/(inaltime in m)^2",
           "Functia pedigree a diabetului",
           "Varsta in ani"]

X=dataset[feature_cols].values
y=dataset["Clasa"].values

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=50)

model=Sequential()
model.add(Dense(12,input_dim=8,activation="relu"))
model.add(Dense(8,activation="relu"))
model.add(Dense(1,activation="sigmoid"))

model.compile(optimizer="adam",
              loss="binary_crossentropy",
              metrics=["accuracy"])

model.fit(X_train,y_train,epochs=20)

pred_train=model.predict(X_train)
scores=model.evaluate(X_train,y_train,verbose=0)
print("Accurary of the model:",scores[1])

pred_test=model.predict(X_test)
scores2=model.evaluate(X_test,y_test,verbose=0)
print("Accuracy on test data",scores2[1])

