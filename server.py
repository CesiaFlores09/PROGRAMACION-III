#IMPORAR LAS LIBRERIAS
from urllib import parse
from http.server import BaseHTTPRequestHandler, HTTPServer

#Codigo de entrenamiento de IA
#IMPORAR LAS LIBRERIAS 
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
import math
import tensorflow_datasets as tfds

#cargamos nuestro dataset en variables
dataset, metadata = tfds.load('mnist', as_supervised=True, with_info=True)
datos_entrenamiento, datos_prueba = dataset["train"], dataset["test"]

numeros_letras = ["Cero", "Uno", "Dos", "Tres", "Cuatro", "Cinco", "Seis", "Siete", "Ocho", "Nueve"]

#pasar en variables los datos de entrenamiento y prueba
numeros_ejemplo_entrenamiento = metadata.splits["train"].num_examples
numeros_ejemplo_prueba = metadata.splits["test"].num_examples
print(numeros_ejemplo_entrenamiento, numeros_ejemplo_prueba)

#funcion normalizadora de los pixeles de 0 - 255 que sean de 0 - 1
def normalizacion(images, labels):
  images = tf.cast(images, tf.float32)
  images /= 255 # 150/255=0.588
  return images, labels

#llamamoas la funcion normalizadora en ambos dataset
datos_entrenamiento = datos_entrenamiento.map(normalizacion)
datos_prueba = datos_prueba.map(normalizacion)

#estruturamos nuestra red neuronal
modelo = tf.keras.Sequential([
        tf.keras.layers.Flatten(input_shape=(28,28,1)), #capa de entreda de 28*28 = 784 neuronas una para cada pixel
        tf.keras.layers.Dense(64, activation=tf.nn.relu), #capa oculta con 64 neuronas, funcion de activacion relu
        tf.keras.layers.Dense(64, activation=tf.nn.relu), #capa oculta con 64 neuronas, funcion de activacion relu
        tf.keras.layers.Dense(10, activation=tf.nn.softmax) #capa de salida con 10 neuronas una para cada numero, 
        #funcion de activacion softmax. esta funcion es requerida para clasificacion
])

#Compilamos el modelo de red neuronal e indicamos las funciones a utilizar 
modelo.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=['accuracy']
)

#Entrenamiento por lotes
batchsize = 32
datos_entrenamiento = datos_entrenamiento.repeat().shuffle(numeros_ejemplo_entrenamiento).batch(batchsize)
datos_prueba = datos_prueba.repeat().shuffle(numeros_ejemplo_prueba).batch(batchsize)

#entrenado nuetro modelo de datos
modelo.fit(datos_entrenamiento, epochs=5, 
           steps_per_epoch=math.ceil(numeros_ejemplo_entrenamiento/batchsize))

#evaluar el modelo con los datos de prueba
test_loss, test_accuracy = modelo.evaluate(datos_prueba, steps=math.ceil(numeros_ejemplo_prueba/batchsize))
print("Resultado de las pruebas", test_loss, test_accuracy)

#servidor en Python
class servidorBasico(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Peticion recibida por GET")
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write("Hola Mundo Chicos de Progra III".encode())
    
    def do_POST(self):
        print("Peticion recibida por POST")
        #obtenemos los datos enviados por AJAX => Asincrono JavaScript y XML
        content_length = int(self.headers['Content-Length'])
        data = self.rfile.read(content_length)
        data = data.decode()
        data = parse.unquote(data)
        
        matriz = np.fromstring(data, np.float32, sep=',')
        matriz = matriz.reshape(28,28)
        matriz = np.array(matriz)
        matriz = matriz.reshape(1,28,28,1)
        
        prediccion = modelo.predict(matriz,batch_size=1)
        prediccion = str(np.argmax(prediccion))
        print(prediccion)

        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin","*")
        self.end_headers()
        self.wfile.write(prediccion.encode())

print("Iniciando el servidor de Python")
servidor = HTTPServer(("localhost", 8000), servidorBasico)
servidor.serve_forever()