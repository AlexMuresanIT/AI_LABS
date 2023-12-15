import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from scipy.special import expit

#setul
xmin=-5
xmax=5
n_samples=100
np.random.seed(0)

X=np.random.normal(size=n_samples)
y=(X>0).astype(np.float)
X[X>0]*=4
X+=0.3*np.random.normal(size=n_samples)
X=X[:,np.newaxis]


#modelul
clf=linear_model.LogisticRegression(C=1e5)
clf.fit(X,y)

#afisare grafica
plt.figure(1,figsize=(10,5))
plt.clf()

plt.scatter(X.ravel(),y,color="blue",zorder=20,label="Date")
X_test=np.linspace(-5,10,300)
plt.plot(X.ravel(),y,"b",markersize=12)

loss=expit(X_test*clf.coef_+clf.intercept_).ravel()
plt.plot(X_test,loss,color="red",linewidth=3)

ols=linear_model.LinearRegression()
ols.fit(X,y)
plt.plot(X_test,ols.coef_*X_test+ols.intercept_,linewidth=1,color="yellowgreen")
plt.axhline(0.5,color="0.5")

plt.xlabel("X")
plt.ylabel("y")
plt.xticks(range(-5,10))
plt.yticks([0,0.5,1])
plt.ylim(-0.25,1.25)
plt.xlim(-4,10)
plt.legend(("Date","Model regresie logistica","Model regresie liniara"),
           loc="lower right",fontsize="small")
plt.tight_layout()
plt.show()
