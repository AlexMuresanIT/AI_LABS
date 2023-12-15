import tensorflow as tf
import numpy as np

a = tf.constant([[1, 2],
                 [2, 3]])
b = tf.constant([[1, 1],
                 [1, 1]])
c = tf.constant([1, 2, 3, 4, 1, 6])

print(tf.add(a, b))
print(tf.multiply(a, b))
print(tf.matmul(a, b))

rank_4_tensor = tf.constant([1, 4, 6, 2, 0, 9, 12, 11])
print(rank_4_tensor)
print(rank_4_tensor.numpy())

rank_2_tensor = tf.constant([[1, 2],
                             [4, 5],
                             [8, 9]])

print(rank_2_tensor[0, 0].numpy())
print(rank_2_tensor[2, 1].numpy())
print()

a = tf.Variable([2, 3])
b = tf.Variable(a)
a.assign([5, 6])
print(a.numpy())
print()
print(b.numpy())
print()
print(a.assign_add([2, 6]).numpy())
print()

a = tf.Variable([[1, 2, 3],
                 [4, 5, 6]])
print(a)
b = tf.constant([[1, 2],
                 [3, 4],
                 [5, 6]])
print(b)
c = tf.matmul(a, b)
print(c)
print()


def ABC(n):
    counter=tf.constant(0)
    n=tf.convert_to_tensor(n)
    for i in range(1,n.numpy()+1):
        i=tf.constant(i)
        if int(i%3)==0:
            print(i)
            counter+=1
    print(counter)

print(ABC(12))