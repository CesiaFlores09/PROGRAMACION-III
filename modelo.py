import math
from PIL import Image
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import cv2
from utils import *

from keras.models import Sequential
from keras.layers import Convolution2D, MaxPooling2D, Dropout
from keras.layers import Flatten, Dense

from tensorflow.keras.optimizers import SGD, RMSprop, Adagrad, Adadelta, Adam, Adamax, Nadam
from keras.callbacks import ModelCheckpoint, History

X_train, y_train = load_data()
print("X_train.shape == {}".format(X_train.shape))
print("Y_train.shape == {}; y_train_min == {:.3f}; y_train_max == {:.3f}".format(
    y_train.shape, y_train.min(), y_train.max()))

X_test, _ = load_data(test=True)
print("X_test.shape == {}".format(X_test.shape))

fig = plt.figure(figsize=(20, 20))
fig.subplots_adjust(left=0, right=1, bottom=0, top=1, hspace=0.05, wspace=0.05)
for i in range(9):
    ax = fig.add_subplot(3, 3, i + 1, xticks=[], yticks=[])
    plot_data(X_train[i], y_train[i], ax)


# El modelo debe aceptar imagenes en escala de 96x96 pixeles
# Debe tener una capa de salida totalmente conectada con 30 valores (2 para cada punto clave facial)
# Como funcion de activacion utilizamos relu que activa una neurona si su valor es mayor que 0
shape = (96, 96)
modelo = Sequential()
modelo.add(Convolution2D(16, (3, 3), padding='same', input_shape=(96, 96, 1), activation='relu'))
modelo.add(MaxPooling2D(pool_size=3, data_format='channels_first'))

modelo.add(Convolution2D(32, (3, 3), padding='same', activation='relu'))
modelo.add(MaxPooling2D(pool_size=3))
modelo.add(Dropout(0.2))

modelo.add(Convolution2D(64, (3, 3), padding='same', activation='relu'))
modelo.add(MaxPooling2D(pool_size=3))
modelo.add(Dropout(0.2))

modelo.add(Convolution2D(128, (3, 3), padding='same', activation='relu'))
modelo.add(MaxPooling2D(pool_size=3))
modelo.add(Dropout(0.2))

modelo.add(Flatten())
modelo.add(Dense(256, activation='relu'))
modelo.add(Dropout(0.2))

modelo.add(Dense(30))

# Summary of the model
modelo.summary()

iteraciones = 50
histo = History()

def compilarModelo(modelo, iteraciones):
    ruta = "modelo.h5"
    modelo.compile(loss='mean_squared_error', optimizer='adam', metrics=['accuracy'])

    checkpointer = ModelCheckpoint(filepath=ruta, 
                                    verbose=1, save_best_only=True)

    modelo.fit(X_train, y_train, batch_size=32, epochs=iteraciones, validation_split=0.2, callbacks=[checkpointer, histo])

    # hist = modelo.fit(X_train, y_train, validation_split=0.2,
    #                 epochs=iteraciones, batch_size=20, callbacks=[checkpointer, histo], verbose=1)

    modelo.save(ruta)

    return hist

def show_training_validation_loss(hist, epochs):
    plt.plot(range(epochs), hist.history[
             'val_loss'], 'g-', label='Val Loss')
    plt.plot(range(epochs), hist.history[
             'loss'], 'g--', label='Train Loss')
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.legend()
    plt.show() 

# TODO: Set True if you want to train the network. It will get a pretrained network values from a file.
entrenamiento = True

if entrenamiento == True:
    hist = compilarModelo(modelo, iteraciones)
else:
    modelo.load_weights("modelo.h5")

# Visualize the training and validation loss of the neural network
if entrenamiento is True:
    show_training_validation_loss(hist, iteraciones)