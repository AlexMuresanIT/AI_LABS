import numpy as np
from numpy import random

x1=2
x2=20
a=[x*0.5 for x in range(2*x1,2*x2+1)]
print("len(a)= ",len(a))
print(a)


b=random.randint(100,size=37)
print("len(b)= ",len(b))
print(b)

r=0
for i in range(len(a)):
    r+=a[i]*b[i]
print("r=",r)

alfa=np.array(a)
beta=np.array(b)
new_r=alfa.dot(beta)
print("new r= ",new_r)