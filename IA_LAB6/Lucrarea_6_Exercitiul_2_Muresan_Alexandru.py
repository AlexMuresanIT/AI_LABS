import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix,classification_report,accuracy_score

date_SVM=pd.read_csv("D:\\Scoala\\an3\\PYTHON_IA\\Fisiere_de_lucru2\\LUCRARI_6\\date_SVM.csv")
X=date_SVM.drop("Clasa",axis=1)
print(X)
y=date_SVM.Clasa
print(y)

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)
print("X_train=\n",X_train)
print("y_train=\n",y_train)

#linear
svclas=SVC(kernel="linear")
svclas.fit(X_train,y_train)
y_pred=svclas.predict(X_test)
print("LINEAR")
print("y_pred=\n",y_pred)
print("Matricea de confuzie este:\n",confusion_matrix(y_test,y_pred))
print("Raportul legat de model este:\n",classification_report(y_test,y_pred))

#polinomial
svclas=SVC(kernel="poly",degree=8)
svclas.fit(X_train,y_train)
y_pred=svclas.predict(X_test)
print("POLINOMIAL")
print("Matricea de confuzie este:\n",confusion_matrix(y_test,y_pred))
print("Raportul legat de model este:\n",classification_report(y_test,y_pred))

#gaussian
svclas=SVC(kernel="rbf")
svclas.fit(X_train,y_train)
y_pred=svclas.predict(X_test)
print("GAUSSIAN")
print("Matricea de confuzie este:\n",confusion_matrix(y_test,y_pred))
print("Raportul legat de model este:\n",classification_report(y_test,y_pred))
