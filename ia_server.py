#IMPORTAR LAS LIBRERIAS 
from urllib import parse
from http.server import BaseHTTPRequestHandler, HTTPServer
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
import math
import tensorflow_datasets as tfds
import pandas as pd

#Codigo de entrenamiento de IA
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

#servidor en Python
class servidorBasico(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Peticion recibida por GET")
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write("Hola Mundo desde Python, GRUPO 8".encode())

    def do_POST(self):
        print("Peticion recibida por POST")
        #obtenemos los datos enviados por AJAX => Asincrono JavaScript y XML
        content_length = int(self.headers['Content-Length'])
        data = self.rfile.read(content_length)
        data = data.decode('utf-8')
        print(data)
 
       
print("Iniciando el servidor de Python")
servidor = HTTPServer(("localhost", 3008), servidorBasico)
servidor.serve_forever()