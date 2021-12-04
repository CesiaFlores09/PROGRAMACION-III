from matplotlib import image
import matplotlib.pyplot as plt
from mtcnn.mtcnn import MTCNN
import numpy as np
import cv2
import os

class manejarRostros():
    def guardarRostro(self, ruta, imagen, id):
        ruta = ruta + "rostro1.jpg"
        print(ruta, type(ruta))
        cv2.imwrite('icon/pacientes/rostros/rostro1.jpg', imagen)

        self.detectarRostros("icon/pacientes/rostros/rostro1.jpg")

    def dibujarRostro(self, imagen, rostros):
        print(rostros)
        img = plt.imread(imagen)

        print(len(rostros))
        for i in range(len(rostros)):
            x, y, w, h = rostros[i]['box']
            X, Y = x + w, y + h

            plt.subplot(1, len(rostros), i+1)
            plt.axis('off')
            cara = img[y:Y, x:X]
            cara = cv2.resize(cara, (200, 200), interpolation = cv2.INTER_CUBIC)
            cv2.imwrite("icon/pacientes/rostros/rostro1.jpg", cara)
            plt.imshow(img[y:Y, x:X])

        plt.show()

    def detectarRostros(self, imagen):
        pixeles = plt.imread(imagen)
        detector = MTCNN()
        rostros = detector.detect_faces(pixeles)
        self.dibujarRostro(imagen, rostros)

    def guardarComparacion(self, ruta, imagen, id):
        # cv2.imwrite(ruta+str(id)+'.jpg', imagen)
        # ruta = ruta + "rostro1.jpg"
        # print(ruta, type(ruta))
        cv2.imwrite('icon/pacientes/rostros/rostroTemp1.jpg', imagen)

        self.detectarRostros2("icon/pacientes/rostros/rostroTemp1.jpg")
        # img1 = plt.imread('icon/pacientes/rostros/rostroTemp1.jpg')
        # img2 = plt.imread('icon/pacientes/rostros/rostro1.jpg')
        # # self.compararRostros(img1, img2)

    def validarCara(self, imagen, rostros):
        print(rostros)
        img = plt.imread(imagen)

        print(len(rostros))
        for i in range(len(rostros)):
            x, y, w, h = rostros[i]['box']
            X, Y = x + w, y + h
            print('ROSTRO', rostros[i])
            plt.subplot(1, len(rostros), i+1)
            plt.axis('off')
            cara = img[y:Y, x:X]
            cara = cv2.resize(cara, (200, 200), interpolation = cv2.INTER_CUBIC)
            cv2.imwrite("icon/pacientes/rostros/rostroTemp1.jpg", cara)
            plt.imshow(img[y:Y, x:X])

        plt.show()
        self.archivosParacomparar('icon/pacientes/rostros/rostroTemp1.jpg')

    def detectarRostros2(self, imagen):
        print('IMAGFEN',imagen)
        pixeles = plt.imread(imagen)
        detector = MTCNN()
        rostros = detector.detect_faces(pixeles)
        self.validarCara(imagen, rostros)

    def compararRostros(self, imagen1, imagen2):
        print('COMPARANDO')
        obj = cv2.ORB_create()

        kp1, des1 = obj.detectAndCompute(imagen1, None)
        kp2, des2 = obj.detectAndCompute(imagen2, None)

        comp = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

        matches = comp.match(des1, des2)

        plt.imshow(cv2.drawMatches(imagen1, kp1, imagen2, kp2, matches, None))
        plt.show()

        similaridad = [i for i in matches if i.distance < 70]
        if len(similaridad) == 0:
            return 0
        return len(similaridad) / len(matches)

    def archivosParacomparar(self, ruta):
        archivos = os.listdir('icon/pacientes/rostros')
        print('ARCHIVOS',archivos)

        if 'rostro1.jpg' in archivos:
            print('HAY ROSTROS')
            rostro = cv2.imread('icon/pacientes/rostros/rostro1.jpg', 0)
            rostroLOG = cv2.imread('icon/pacientes/rostros/rostroTemp1.jpg', 0)
            similaridad = self.compararRostros(rostro, rostroLOG)
            if similaridad > 0.9:
                print('Rostro identificado')
                return True
            else:
                print('Rostro no identificado')
                return False
        else:
            print('No hay rostros para comparar')
            return False