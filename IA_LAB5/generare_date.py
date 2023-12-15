import numpy as np
import matplotlib.pyplot as plt

x=np.random.normal(5,1,1000)
y=np.random.normal(10,2,1000)
plt.title("Generare date")
plt.scatter(x,y,color="blue")
plt.show()