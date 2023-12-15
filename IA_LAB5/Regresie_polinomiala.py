import numpy as np
import matplotlib.pyplot as plt


x=[1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y=[100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

model=np.poly1d(np.polyfit(x,y,4))
print(model)

line=np.linspace(1,22,100)
print(line)

plt.scatter(x,y,color="green")
plt.plot(line,model(line),color="blue")
plt.show()

"""
e=pandas.read_csv("adresa folderului")
X=e[["Weight","Volume"]]
y=e["C02"]
regr=lm.LinearRegression()
regr.fit(X,y)"""