import matplotlib.pyplot as plt
from mtcnn.mtcnn import MTCNN
import cv2
import os

class manejarRostros():
    def guardar_rostro(self, ruta, img, id):
        if ruta == 'icon/pacientes/':
            img_ruta = f"{ruta}perfil{id}.jpg"
        elif ruta == 'icon/personal/':
            img_ruta = f"{ruta}personal{id}.jpg"
        else:
            print('No se encontro la ruta')
            return False
        print(img_ruta)
        cv2.imwrite(img_ruta, img)

        detector = self.detectar_rostros(img_ruta, ruta+'rostros/rostro', id)

        if detector == True:
            print('Se guardo el rostro')
            return True
        else:
            print('No se pudo guardar el rostro')
            os.remove(img_ruta)
            # os.remove(f"{ruta}rostros/rostro{id}.jpg")
            return False

    def detectar_rostros(self, img, ruta, id):
        pixeles = plt.imread(img)
        detector = MTCNN()
        rostros = detector.detect_faces(pixeles)
        return self.dibujar_rostro(img, rostros, ruta, id)

    def dibujar_rostro(self, img, rostros, ruta, id):
        img = plt.imread(img)

        print(len(rostros), id, ruta)

        if len(rostros) == 0:
            print('No se encontraron rostros')
            return False

        elif len(rostros) == 1:
            try:
                x, y, w, h = rostros[0]['box']
                X, Y = x + w, y + h

                plt.subplot(1, len(rostros), 1)
                plt.axis('off')
                rostro = img[y:Y, x:X]
                rostro = cv2.resize(rostro, (200, 200), interpolation = cv2.INTER_CUBIC)
                cv2.imwrite(f"{ruta}{id}.jpg", rostro)
                plt.imshow(img[y:Y, x:X])
                plt.show()

                print('Se encontro un rostro')
                return True
            except Exception as e:
                print('No se encontro un rostro, error', e)
                return False

        else:
            print('Asegurate de que solo hay un rostro en la imagen')
            return False

    def iniciar_sesion(self, ruta, img, id):
        if ruta == 'icon/pacientes/':
            img_ruta = f'{ruta}temp/temp{id}.jpg'
        elif ruta == 'icon/personal/':
            img_ruta = f'{ruta}temp/temp{id}.jpg'
        else:
            print('No se encontro la ruta')
            return False
        
        cv2.imwrite(img_ruta, img)

        detector = self.detectar_rostros(img_ruta, ruta+'temp/temp', id)
        if detector == True:
            similitud = self.comparar_rostros(ruta, id)
            if similitud == True:
                return True
            else:
                return False
        else:
            print('No se pudo guardar el rostro')
            # os.remove(img_ruta)
            return False

    def comparar_rostros(self, ruta, id):
        archivos = os.listdir(ruta+'rostros/')

        if f'rostro{id}.jpg' in archivos:
            img1 = plt.imread(f'{ruta}rostros/rostro{id}.jpg')
            img2 = plt.imread(f'{ruta}temp/temp{id}.jpg')
            similitud = self.similitud_rostros(img1, img2)
            print('Similitud:', similitud)
            if similitud > 0.98:
                print('Bienvenido')
                return True
            else:
                print('No hay coincidencias')
                return False
        else:
            print('No existe el usuario')
            return False

    def similitud_rostros(self, img1, img2):
        orb = cv2.ORB_create()

        kp1, des1 = orb.detectAndCompute(img1, None)
        kp2, des2 = orb.detectAndCompute(img2, None)

        bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

        matches = bf.match(des1, des2)

        plt.imshow(cv2.drawMatches(img1, kp1, img2, kp2, matches, None))
        plt.show()

        similitud = [i for i in matches if i.distance < 80]
        if len(similitud) == 0:
            return 0
        return len(similitud) / len(matches)
        # img1 = img1.flatten()
        # img2 = img2.flatten()

        # distancia = np.linalg.norm(img1 - img2)
        # return distancia