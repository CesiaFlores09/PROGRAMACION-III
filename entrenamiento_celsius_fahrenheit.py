
import tensorflow as tf
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#obtencion de los datos de entrenamiento
celsius_f = pd.read_csv("convertido de celsius a fahrenheit.csv", sep=";")
#print(celsius_f)

#datos de entrada y salida
c = celsius_f ['celsius']
f = celsius_f['fahrenheit']

#modelo de entrenamiento
modelo_c_f= tf.keras.Sequential()
modelo_c_f.add(tf.keras.layers.Dense(units=1, input_shape=[1]))

#compliar modelo
modelo_c_f.compile(optimizer=tf.keras.optimizers.Adam(1),loss='mean_squared_error')

hisotiral_c_f = modelo_c_f.fit(c,f, epochs=525, verbose=0)

#convertir de metros a yardas
f= modelo_c_f.predict([10])
print("Conversion de celsius a Farehrenheit: ",f)


