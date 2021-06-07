import os
import tensorflow as tf
import numpy as np
samples = []
labels = []
images_folder = "images/"
for image in os.listdir(images_folder):
    samples.append(tf.keras.preprocessing.image.img_to_array(tf.keras.preprocessing.image.load_img(images_folder+image, target_size=(100, 100))))
    if "normal" in image:
        labels.append((0))
    else:
        labels.append((1))
samples = np.array(samples)
labels = np.array(labels)
eval_x, eval_y = samples[-100:], labels[-100:]
print(samples.shape, labels.shape)
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(samples[:-100], labels[:-100], test_size=0.2, random_state=123)