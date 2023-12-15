import pandas as pd
import numpy as np

input_dim=3
learning_rate=0.01
Weights = [0 for x in range(0,input_dim)]
Weights[0]=0.5
Weights[1]=0.5
Weights[2]=0.5

Training_Data = pd.read_csv("D:\\Scoala\\an3\\PYTHON\\LAB1\\SET_ANTRENARE.csv")
Expected_Output=Training_Data.output
Training_Data=Training_Data.drop(["output"],axis=1)
Training_Data = np.asarray(Training_Data)
Training_Count= len(Training_Data)
print("Numarul de elemente din lista: ",Training_Count)

#calculam ponderile
for epoch in range(0,5):
    for datum in range(0,Training_Count):
        Output_Sum=np.sum(np.multiply(Training_Data[datum],Weights))
        if Output_Sum < 0:
            Output_Value = 0
        else:
            Output_Value = 1
        error = Expected_Output[datum]-Output_Value
        for n in range(0, input_dim):
            Weights[n]=Weights[n]+learning_rate*error*Training_Data[datum,n]

print("w0 = %.3f" %(Weights[0]))
print("w1 = %.3f" %(Weights[1]))
print("w2 = %.3f" %(Weights[2]))


def aplicare(intrare):
    element = 0
    for i in range(0,input_dim):
        element= element+intrare[i]*Weights[i]
    if element < 0:
        iesire = 0
    else:
        iesire = element
    print("Pentru intrarea ", intrare , " iesirea este ", iesire)


intrare1=[2,-5,8]
intrare2=[-3,4,-2]
intrare3=[30,3,3]

aplicare(intrare1)
aplicare(intrare2)
aplicare(intrare3)
