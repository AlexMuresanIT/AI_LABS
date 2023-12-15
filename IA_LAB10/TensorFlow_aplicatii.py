import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

fashion_mnist=tf.keras.datasets.fashion_mnist

(train_images,train_labels),(test_images,test_labels)=fashion_mnist.load_data()

class_names=["T-shirt/top","Trouser","Pullover","Dress","Coat","Sandal","Shirt","Sneaker","Bag","Ankle boot"]

print("Setul de instruire",train_images.shape)
print("Numarul de imagini din setul de instruire",len(train_labels))
print("Cum arata etichetele din setul de instruire",train_labels)
print("Setul de testare",test_images.shape)
print("Numarul de imagini din setul de testare",len(test_labels))

plt.imshow(train_images[np.random.randint(0,60000)])
plt.show()

#Construim modelul de retea neuronala pentru invatare profunda
model=tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28,28)),
    tf.keras.layers.Dense(128,activation="relu"),
    tf.keras.layers.Dense(10)
])

#compilarea modelului
model.compile(optimizer="adam",
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=["accuracy"])

#antrenarea modelului
model.fit(train_images,train_labels,epochs=10)

#evaluare acuratete
test_loss,test_acc=model.evaluate(test_images,test_labels,verbose=2)
print("\nTest accuracy",test_acc)

#de aici modelul este antrenat si se poate folosi pentru predictii
probability_model=tf.keras.Sequential([
    model,
    tf.keras.layers.Softmax()
])

predictions=probability_model.predict(test_images)

print(predictions[0])
print(np.argmax(predictions[0]))
