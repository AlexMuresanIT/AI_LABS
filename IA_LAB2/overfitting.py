import numpy as np
import matplotlib.pyplot as plt
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score

#predefinim functia corecta ca sa aratam under si over fit
def true_fun(x):
    return np.cos(1.5*np.pi*x)

#generam numere aleatorii si le salvam ca sa operam cu ele la fiecare noua rulare a programului

np.random.seed(0)
#numarul de elemente
n_samples=30
#lista cu gradele polinoamelor utilizate
degrees = [1,4,15]
#generare set X
X=np.sort(np.random.rand((n_samples)))
#generare set Y in jurul functiei corecte
Y=true_fun(X)+np.random.randn(n_samples)*0.1
#definim marime figura
plt.figure(figsize=(14,6))
help(Pipeline)
for i in range(len(degrees)):
    #ordinea graficelor - subplot-uri
    ax=plt.subplot(1,len(degrees),i+1)
    plt.setp(ax,xticks=(),yticks=())
    #definim diverse modele i=1,4,15
    polynomial_features = PolynomialFeatures(degree=degrees[i],include_bias=False)
    linear_regression=LinearRegression()
    pipeline=Pipeline([("Caracteristici polinomiale",polynomial_features),("Regresie liniara",linear_regression)])
    print(pipeline)
    pipeline.fit(X[:,np.newaxis],Y)

    #evaluare cu validare in cruce
    scores = cross_val_score(pipeline,X[:,np.newaxis],Y,scoring="neg_mean_squared_error",cv=10)

    #afisam graficele
    X_test= np.linspace(0,1,100)
    plt.plot(X_test,pipeline.predict(X_test[:,np.newaxis]),color="blue",label="Model")
    plt.plot(X_test,true_fun(X_test),color="cyan",label="Functia corecta")
    plt.scatter(X,Y,edgecolors="yellow",s=20,label="Mostre")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.xlim((0,1))
    plt.ylim((-2,2))
    plt.legend(loc="best")
    plt.title("Polinom de grad {}\nMSE = {:.2e}(+/-{:.2e})".format(degrees[i],-scores.mean(),scores.std()))

plt.show()

