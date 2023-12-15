import pandas as pd
import numpy as np

input_dim=3#numar de intrari
learning_rate=0.01
Weights = np.random.rand(input_dim)

Weights[0]=0.5
Weights[1]=0.5
Weights[2]=0.5

#importam fisier de tip excel
Training_Data = pd.read_csv("D:\\Scoala\\an3\\PYTHON\\LAB1\\SET_ANTRENARE.csv")


#cream matrici cu valori din excel
Expected_Output=Training_Data.output
Training_Data=Training_Data.drop(["output"],axis=1)
Training_Data=np.asarray(Training_Data)

training_count=len(Training_Data)

for epoch in range(0,5):
    for datum in range (0,training_count):
        Output_Sum=np.sum(np.multiply(Training_Data[datum,:],Weights))
        if Output_Sum < 0:
            Output_Value= 0
        else:
            Output_Value =1
        error = Expected_Output[datum]-Output_Value
        for n in range(0,input_dim):
            Weights[n]=Weights[n]+learning_rate*error*Training_Data[datum,n]

print("Numarul de elemente din lista este: ", training_count)
print("Numarul de epoci este: ", epoch+1)
print("w0: ",Weights[0])
print("w1: ",Weights[1])
print("w2: ",Weights[2])

def aplicare(intrare):
    element=0
    for i in range(0,input_dim):
        element= element+intrare[i]*Weights[i]
    if element>0:
        iesire=1
    else:
        iesire=0
    print("Pentru intrarea ", intrare, " iesirea este ", iesire)

intrare1=[2,-5,8]
intrare2=[-3,4,-2]
aplicare(intrare1)
aplicare(intrare2)
