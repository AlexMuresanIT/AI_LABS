#Descendenta in gradient
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

col_names=["","metro","price","minutes","way","provider","fee_percent","views","storey","storeys","rooms","total_area","living_area","kitchen_area"]
data=pd.read_csv("D:\\Scoala\\an3\\PYTHON_IA\\Fisiere_de_lucru2\\LUCRARI_7\\moscow_real_estate_sale.csv",low_memory=False)

data["rooms"]=data["rooms"].str.replace("+","0",regex=True)
data["rooms"]=data["rooms"].astype(float)
data.drop("metro", inplace=True, axis=1)
data.drop("way", inplace=True, axis=1)
data.drop("provider", inplace=True, axis=1)
data.drop("fee_percent", inplace=True, axis=1)
print(data.head())
print(np.shape(data))

for k,v in data.items():
    q1=v.quantile(0.25)
    q3=v.quantile(0.75)
    irq=q3-q1
    v_col=v[(v<=q1-1.5*irq)|(v>=q3+1.5*irq)]
    perc=np.shape(v_col)[0]*100/np.shape(data)[0]
    print("Anomalii pe coloane %s=%.2f%%"%(k,perc))

data=data[~(data["price"]>35000000)]
print(np.shape(data))

"""fig,axs=plt.subplots(ncols=7,nrows=2,figsize=(15,10))
index=0
axs=axs.flatten()
culori=["blue","purple","blue","gray","green","red","magenta","gold","cyan",
        "orange","lightgreen","navy","pink","yellowgreen"]
for k,v in data.items():
    sns.histplot(v,ax=axs[index],color=culori[index])
    index+=1
plt.tight_layout(pad=0.4,w_pad=0.5,h_pad=5)

print("CORELATIA INTRE PERECHI")
plt.figure(figsize=(15,10))
sns.heatmap(data.corr().abs(), annot=True)"""


"""Din matricea de corelare, vedem ca <storey>, <storeys>, sunt caracteristici
puternic corelate <0.94>"""

col_selectate=["storey","storeys","rooms"]
from sklearn import preprocessing
min_max_scaler=preprocessing.MinMaxScaler()
x=data.loc[:,col_selectate]
y=data["price"]
x=pd.DataFrame(data=min_max_scaler.fit_transform(x),columns=col_selectate)

"""fig,axs=plt.subplots(nrows=1,ncols=3,figsize=(20,10))
index=0
axs=axs.flatten()
color_list=["red","orange","blue"]
for i,k in enumerate(col_selectate):
    sns.regplot(y=y,x=x[k],ax=axs[i],color=color_list[i])
plt.tight_layout(pad=0.4,w_pad=0.5,h_pad=5)
#plt.show()"""

#eliminam data asimetrice
y=np.log1p(y)
for col in x.columns:
    if np.abs(x[col].skew())>0.3:
        x[col]=np.log1p(x[col])

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import SGDRegressor
from sklearn.pipeline import  make_pipeline

X_train,X_test,y_train,y_test=train_test_split(x,y,test_size=0.33,random_state=42)
model=make_pipeline(StandardScaler(),SGDRegressor(max_iter=100,tol=1e-3))
model.fit(X_train,y_train)
predictii=model.predict(X_test)

print("Valoarea maxima predictii=",max(predictii))
print("Valoarea maxima efectiv=",max(y_test))
print("Nr. coloane=",X_test.shape[1])
print("Nr. linii=",X_test.shape[0])

plt.figure(figsize=(8,8))
plt.scatter(y_test,predictii,marker="o",color="red")
plt.title("Y_test versus Y_estimat",color="blue")
plt.xlabel("Date efective")
plt.ylabel("Date estimate")
#plt.show()

from sklearn import linear_model
from sklearn.metrics import mean_squared_error,r2_score

x1=y_test
print(type(x1))
print(type(predictii))


