import pandas as pd
import numpy as np


input_dim=3
learning_rate=0.01
Weights = [0 for x in range(input_dim)]
Weights[0]=0.5
Weights[0]=0.5
Weights[0]=0.5

Training_Data = pd.read_csv("D:\\Scoala\\an3\\PYTHON\\LAB1\\SET_ANTRENARE.csv")
Expected_Output = Training_Data.output
Training_Data = Training_Data.drop(["output"], axis =1)
Training_Data = np.asarray(Training_Data)
Training_Count = len(Training_Data)
print("Numarul de elemenente din lista: ", Training_Count)

e=2.7#from the sigmoid formula

for epoch in range (0,5):
    for datum in range(0,Training_Count):
        Output_Sum= np.sum(np.multiply(Training_Data[datum], Weights))
        Output_Value = 1/(1+e**(-Output_Sum))
        error= Expected_Output[datum]-Output_Value
        for n in range(0,input_dim):
            Weights[n] = Weights[n]+learning_rate*error*Training_Data[datum, n]

print("w0 = ", Weights[0])
print("w1 = ", Weights[1])
print("w2 = ", Weights[2])

def aplicare(intrare):
    element=0
    for i in range(0,input_dim):
        element = element+intrare[i]*Weights[i]
    iesire = 1/(1+e**(-element))
    print("Pentru intrarea ", intrare , "iesirea este ", iesire)



intrare1 = [2,-5,8]
intrare2 = [-3,4,-2]


aplicare(intrare1)
aplicare(intrare2)
