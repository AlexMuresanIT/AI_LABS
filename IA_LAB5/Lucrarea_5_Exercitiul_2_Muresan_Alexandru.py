import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures

DF=pd.read_csv("D:\\Scoala\\an3\\PYTHON_IA\\Fisiere_de_lucru2\\LUCRARI_5\\salarii_tabel.csv")

x=DF["Nivel"]
y=DF["Salariu"]

model=np.poly1d(np.polyfit(x,y,4))
line=np.linspace(1,10,1000000)

train_x,train_y,test_x,test_y=train_test_split(x.values,y.values,train_size=0.5,test_size=5)

print("Valori pentru antrenare:")
print(train_x)
print(train_y)

print("Valori pentru testare:")
print(test_x)
print(test_y)

#Afisare grafic
plt.title("Grafic salarii")
plt.scatter(x,y,color="blue")
plt.plot(line,model(line),color="green")
plt.xlabel("Pozitie")
plt.ylabel("Salariu")

plt.subplots()
plt.title("Valori antrenate")
plt.scatter(train_x,train_y,color="red")

plt.subplots()
plt.title("Valori testate")
plt.scatter(test_x,test_y,color="red")
plt.show()





