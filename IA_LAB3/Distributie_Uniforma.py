import numpy as np
import matplotlib.pyplot as plt

v=np.random.uniform(0,6,100000)
print(v)
print(max(v))
print(len(v))

plt.hist(v,100,color="blue")
plt.show()