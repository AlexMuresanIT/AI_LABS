
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import recall_score
from sklearn.metrics import precision_score
from sklearn.metrics import f1_score
from sklearn.metrics import classification_report

y_pred=[0,1,0,0,0,1,0,1,0,0,1,0]
y_true=[0,1,0,0,1,1,0,0,0,0,0,0]

confuzia=confusion_matrix(y_true,y_pred)
print("Matricea de confuzie:\n",confuzia)
acuratetea=accuracy_score(y_true,y_pred)
print("Acuratetea= ",acuratetea)
rechemarea= recall_score(y_true,y_pred)
print("Rechemarea= ",rechemarea)
precizia=precision_score(y_true,y_pred)
print("Precizia= ",precizia)
factorul_F1=f1_score(y_true,y_pred)
print("Factorul F1= ",factorul_F1)

matrix = classification_report(y_true,y_pred)
print("Report: \n", matrix)




