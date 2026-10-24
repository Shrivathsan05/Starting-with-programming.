import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf
import random
from keras import layers, models
import matplotlib.pyplot as plt
from keras.preprocessing.image import ImageDataGenerator
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0
x_train = x_train.reshape(-1, 28, 28, 1)
x_test = x_test.reshape(-1, 28, 28, 1)
datagen = ImageDataGenerator(rotation_range=10, zoom_range=0.1, width_shift_range=0.1, height_shift_range=0.1)
datagen.fit(x_train)
model = models.Sequential([layers.Flatten(input_shape=(28, 28, 1)), layers.Dense(128, activation=tf.keras.layers.LeakyReLU(alpha=0.1)), layers.Dense(64, activation=tf.keras.layers.LeakyReLU(alpha=0.1)), layers.Dense(10, activation='softmax')])
model.compile(optimizer='rmsprop', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit(datagen.flow(x_train, y_train, batch_size=256), epochs=1)
test_loss, test_acc = model.evaluate(x_test, y_test)
print(f"Test accuracy: {test_acc}")
index = random.randint(0, len(x_test) - 1)
predictions = model.predict(x_test[index:index+1])
plt.imshow(x_test[index].reshape(28, 28), cmap='gray') 
plt.title(f"Predicted: {predictions[0].argmax()}") 
plt.show()