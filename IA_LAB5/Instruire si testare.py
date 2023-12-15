import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

#seed(2) 2 array-uri
np.random.seed(2)

#(3,1,100)- media aritmetica =3 , deviatia standard=1, numarul de date din array=100
x=np.random.normal(3,1,100)
y=np.random.normal(150,40,100)/x
print("x=",x)
print("y=",y)

#set de instruire
print("Set date de instruire:")
train_x=x[:80]
train_y=y[:80]
print(train_x)
print(train_y)

#set de testare
print("Set date de testare:")
test_x=x[80:]
test_y=y[80:]
print(test_x)
print(test_y)

#facem grafice
plt.subplots()
plt.title("Set creat")
plt.scatter(x,y,color="blue")

plt.subplots()
plt.title("Set selectat pentru instruire")
plt.scatter(train_x,train_y,color="green")

plt.subplots()
plt.title("Set selectat pentru testare")
plt.scatter(test_x,test_y,color="red")

#model polinomial
model=np.poly1d(np.polyfit(train_x,train_y,4))
orizontala=np.linspace(0,6,100)
plt.subplots()
plt.scatter(train_x,train_y,color="blue")
plt.plot(orizontala,model(orizontala),color="red")
plt.show()

#acuratetea modelului
r=r2_score(train_y,model(train_x))
print("relevanta modelului= ",r)

#verificam pe setul de testare
r_test=r2_score(test_y,model(test_x))
print("relevanta la testatre= ",r_test)
#predictie
intrare=5
pred_1=model(intrare)
print("Pentru intrarea ",intrare," predictia la iesire este ",pred_1)