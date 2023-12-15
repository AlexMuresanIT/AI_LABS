import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics
from sklearn.model_selection import train_test_split

headers=["pret achizitie","costuri de intretinere","numar usi","numar maxim pasageri","marime portbagaj","grad de siguranta","decizie"]

file=pd.read_csv("D:\\Scoala\\an3\\PYTHON_IA\\Fisiere_de_lucru2\\LUCRARI_6\\evaluare_masini.csv",header=None,names=headers)
#print(file.head())

d={"vhigh":0,"high":1,"med":2,"low":3}
file["pret achizitie"]=file["pret achizitie"].map(d)

d={"vhigh":0,"high":1,"med":2,"low":3}
file["costuri de intretinere"]=file["costuri de intretinere"].map(d)

d={"1":1,"2":2,"3":3,"4":4,"5more":5}
file["numar usi"]=file["numar usi"].map(d)

d={"1":1,"2":2,"3":3,"4":4,"more":5}
file["numar maxim pasageri"]=file["numar maxim pasageri"].map(d)

d={"big":0,"med":1,"small":2}
file["marime portbagaj"]=file["marime portbagaj"].map(d)

d={"high":0,"med":1,"low":2}
file["grad de siguranta"]=file["grad de siguranta"].map(d)

d={"unacc":3,"acc":2,"good":1,"vgood":0}
file["decizie"]=file["decizie"].map(d)

feature_cols=["pret achizitie","costuri de intretinere","numar usi","numar maxim pasageri","marime portbagaj","grad de siguranta"]
X=file[feature_cols]
y=file["decizie"]

clf=DecisionTreeClassifier()
clf=clf.fit(X,y)

a=clf.predict([[0,2,5,4,1,1]])
for i in d:
    if d[i]==a:
        print(i)
b=clf.predict([[0,0,4,5,1,1]])
for i in d:
    if d[i]==b:
        print(i)

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=1)
clf=DecisionTreeClassifier()
clf=clf.fit(X_train,y_train)

y_pred=clf.predict(X_test)
print("Acuratetea modelului: ",metrics.accuracy_score(y_test,y_pred)*100," %")











