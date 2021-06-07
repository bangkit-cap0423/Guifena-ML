import label_split
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Convolution2D, Conv2D, MaxPooling2D, GlobalAveragePooling2D

#Convolution Neural Network Model
model = Sequential()
model.add(Conv2D(filters=32, kernel_size=(3, 3), input_shape=(100, 100, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=2))
model.add(Conv2D(filters=64, kernel_size=(3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=2))
model.add(Conv2D(filters=128, kernel_size=(3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=2))
model.add(Conv2D(filters=128, kernel_size=(3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=2))
model.add(Dropout(0.5))
model.add(Flatten())
tf.keras.layers.Dense(512, activation='relu'),
model.add(Dense(1, activation='sigmoid'))
print(model.summary())
model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])
history = model.fit(x_train, y_train, batch_size=20, epochs=150,
          validation_data=(x_test, y_test),
         verbose=1)
model.save('model/')

#Plotting the result
import matplotlib.pyplot as plt

acc = history.history['accuracy']
val_acc = history.history['val_accuracy']

loss = history.history['loss']
val_loss = history.history['val_loss']

epochs = range(len(acc))

plt.plot(epochs, acc)
plt.plot(epochs, val_acc)
plt.title('Training and Validation Accuracy')

plt.figure()

plt.plot(epochs, loss)
plt.plot(epochs, val_loss)
plt.title('Training and Validation Loss')

print('Training Accuracy \t: {}'.format(acc[-1]))
print('Validation Accuracy \t: {}'.format(val_acc[-1]))
print('Training Loss \t\t: {}'.format(loss[-1]))
print('Validation Loss \t: {}'.format(val_loss[-1]))