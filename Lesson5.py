import tensorflow as tf 
from tensorflow.keras import layers, models
import matplotlib.pyplot as plt
(Xtrain, Ytrain), (Xtest, Ytest) = tf.keras.datasets.mnist.load_data()
Xtrain, Xtest = Xtrain / 255.0, Xtest / 255.0
Model = models.Sequential([layers.Flatten(input_shape=(28, 28)), layers.Dense(128, activation='relu'), layers.Dense(10, activation='softmax')])
Model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
Model.fit(Xtrain, Ytrain, epochs=5)
TestLoss, TestAccuracy = Model.evaluate(Xtest, Ytest)
print(f" Test Accuracy : {TestAccuracy} ")
Predictions = Model.predict(Xtest)
plt.imshow(Xtest[0], cmap=plt.cm.binary)
plt.title(f"Predicted Label: {Predictions[0].argmax()} | True Label: {Ytest[0]}")
plt.show()