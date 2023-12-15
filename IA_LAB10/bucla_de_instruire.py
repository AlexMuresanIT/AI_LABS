import tensorflow as tf

A=3
B=2
nr_date=1000

#generam un numar de 1000 de valori aleatorii
x=tf.random.normal(shape=[nr_date])

zgomot=tf.random.normal(shape=[nr_date])

#generam perechi
for i in range(nr_date):
    if i%2==0:
        y=x*A+(B+zgomot)
    else:
        y=x*A+(B-2*zgomot)

import matplotlib.pyplot as plt

#plt.scatter(x,y,color="red")
#plt.show()

class Model_ML(tf.Module):
    def __int__(self):
        self.w=tf.Variable(7)
        self.b=tf.Variable(0.6)

    def __call__(self,x):
        return self.w*x+self.b

model1=Model_ML

test=14.6
assert model1(2)==test

