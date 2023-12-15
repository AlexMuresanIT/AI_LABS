from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score
from matplotlib import pyplot

#generam un set de date cu 2 clase
X,Y=make_classification(n_samples=1000,n_classes=2,random_state=1)

#impartim setul de date pentru instruire si testare (50-50 aici)
trainX,testX,trainY,testY=train_test_split(X,Y,test_size=0.5,random_state=2)

#generam clasa majoritara [FARA CUNOSTINE DE IA]
ns_probs=[0 for _ in range(len(testY))]

#alegem modelul de clasificare [CLASIFICATORUL]
model = LogisticRegression(solver='lbfgs')

#potrivim modelul pentru instruire
model.fit(trainX, trainY)

#estimam probabilitati
lr_probs=model.predict_proba(testX)

#pastram probabilitatile pentru iesirea pozitiva
lr_probs=lr_probs[:,1]

#calculam scorurile
ns_auc=roc_auc_score(testY,ns_probs)
lr_auc=roc_auc_score(testY,lr_probs)

#facem un rezumat al scorurilor
print("Fara cunostine in IA: ROC AUC: ",ns_auc)
print("Dupa finalizare curs: ROC AUC: ",lr_auc)

#calculam curba ROC
ns_fpr,ns_tpr,_=roc_curve(testY,ns_probs)
lr_fpr,lr_tpr,_=roc_curve(testY,lr_probs)

#afisam curba
pyplot.plot(ns_fpr,ns_tpr,linestyle="--",label="Fara cunostinte de IA")
pyplot.plot(lr_fpr,lr_tpr,marker=".",label="Cu aptitudini de IA")

#etichete axelor
pyplot.xlabel("FPR=False Positive Rate")
pyplot.ylabel("TPR=True Positive Rate")
pyplot.legend()
pyplot.show()

