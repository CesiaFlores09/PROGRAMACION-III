print("Hola Mundo")

print("Bienvenidos  progra III")

myname = "Cesia Flores"
print("Mi nombre es: ", myname)


Num1 = 5
Num2 = 10
resp= Num1 +  Num2
print("La respues es: ", resp)

nombre = input("Como te llamas: ")
print("Hola "+nombre, "Tu letra inicial es: ", nombre[0], "Tu nombre tiene: ", nombre.__len__(), " caracteres" )

num1=5
num2=6
resp = num1 + num2
print("La suma es : ", resp)

num1= input("Num1: ")
num2= input ("Num2: ")
resp = float(num1) + float(num2)
print("La suma es : ", resp)

num1= input("Num1: ")
num1= float(num1)
num2= float(input("Num2: "))
resp = num1 + num2
print("La suma es : ", resp)

print("Hola nuevamente", nombre)

gustapython = True
print("hola ", nombre, " te gusta python ", gustapython)

print( "nombre: ", type(nombre), "num1: ",type(num1), "num2: ", type(num2), "resp: ", type(resp), "gustapython: ", type(gustapython), "1", type(1))

print("resp: "+ str(resp))

def suma(num1, num2):
     resp= num1 + num2
     return resp
num1 = float(input("Num1: "))
num2 = float(input("Num2: "))
resp= suma(num1, num2)
print(resp)

num1 = int(input("Num1: "))
num2 = int(input("Num2: "))
print("Los numero", str(num1), ",", str(num2), " son iguales: ", str(num1==num2) )

def convertirFC(f):
     c = (f-32)*5/9
     return c

f = float(input("F: "))
print("F: ", str(f), " a celsius: ", str( convertirFC(f) ))

numHrs = int(input("Num. de Hrs trabajadas: "))
valorHr = float(input("Valor por hr: "))

sueldo = numHrs*valorHr*30
print("Sueldo: ", sueldo)

def calcularSueldo(numHrs, valorHr):
   hrsExtras = 0
   if( numHrs>8 ):
      hrsExtras = numHrs-8
   sueldo = (8*valorHr + hrsExtras*valorHr*2)*30
   return sueldo

numHrs = int(input("Num. hrs trabajadas: "))
valorHr = float(input("Valor x hr: "))
print("Sueldo: ", str(calcularSueldo(numHrs, valorHr)))

suma = lambda num1, num2: num1+num2
num1 = float(input("Ingrese el numero 1: "))
num2 = float(input("Ingrese el numero 2: "))
print("La suma es: ", suma(num1, num2))

conversion = lambda f:(f-32)*5/9
f = float(input("Grados Fahrenheit: "))
print("Grados Fahrenheit: ", f, "a Grados Celsius: ", conversion(f))

cuadrado = lambda n:n**2
n = int(input("N: "))
print("N: ", n, "al cuadrado es: ", cuadrado(n) )

cubo = lambda n:n**3
n = int(input("N: "))
print("N: ", n, "al cubo es: ", cubo(n) )

exp = lambda n,e:n**e
n = int(input("N: "))
e = int(input("Exponente: "))
print(n, " elevado al exp", e, "es: ", exp(n,e) )

lista = [5,7,10,2,1]
resp = list(map(lambda n:n*2, lista))
print(resp)

gfdepto = [85,58,105]
cdepto = list(map(conversion, gfdepto))
print("Los grados F: ", gfdepto, "en Celsius es: ", cdepto)

resp=list(map(cuadrado, lista))
print("La lista ", lista, "el cuadrado es: ", resp)

resp=list(map(cuadrado, lista))
print("La lista ", lista, "el cuadrado es: ", resp)

resp = list(filter(lambda n:n<=2,lista))
print("Los numeros <= 2 de la lista ", lista, "son: ", resp)

resp = list(filter(lambda n:n%2==0, lista))
print("Los numeros pares de la lista : ", lista, "son: ", resp )

resp = list(filter(lambda n:n%2!=0, lista))
print("Los numeros impares de la lista : ", lista, "son: ", resp )

from functools import reduce
resp = reduce(lambda x,y:x+y, lista)
print("La suma de la lsita ", lista,"es: ", resp, "la media es: ", resp/len(lista))

persona = "USIS002020", "Cesia Flores", "Zacatecoluca", "3421-2345", "florescsia@gmail.com"
print(persona)

nombre= "Cesia Flores"
print(nombre[0:5], nombre.count("e"))

name= ["C", "E", "S", "I", "A", "F", "L", "O", "R", "E", "S"]
print(name, name[0:5], name.count("E"), name.index("E"))

person= ["USIS002020", "Cesia Flores", "Direccion: Zacatecoluca", "3421-2345", "florescsia@gmail.com", 34, 78.8]
print(person)
person.append("python")
person.insert(2, "Depto: La paz")
person[6]=7.8
leng= person.pop()
print(person, leng)

nEnteros= [2,6,7,8,9]
nOrdenados=sorted(nEnteros, reverse=True)
numReverse=list(reversed(nEnteros))
print("Lista desordenada: ", nEnteros, "Lista Ordenada: ", nOrdenados, "numeros al reves: ", numReverse)

me=["USIS002020", "Cesia Flores", "Zacatecoluca",503,"7034-7835","usis00202@ugb.edu.sv",["Progra I", "Progra II",[6,8,9,4], "Progra III"]]
print( me[0][0:4], me[6][2][2], me[6][2][0])

matriz=[
        [1,2,3],
        [3,5,6],
        [5,7,6]
]
print(matriz)

matriz=[
        [1,5,3,5],
        [3,4,4],
        [5,4],
        [6,7,8,9,2],
        7
]
print(matriz)

lenguajes={"Progra I":"VB","Progra II":"JAVA","Progra III":"Python"}
print(lenguajes["Progra III"])

mi={
    "codigo":"USISOO2O20",
    "nombre":"Cesia Flores",
    "direccion":{
        "pais":{
            "codigo":"503",
            "nombre":"El Salvador",
            "codigoiso":"sv",
            "continente":{
                "nombre":"C.A"
                
            }
        },

    "departamento":"La Paz",
    "municipio":"Santiago Nonualco",
    },
    "tels":{
        "oficiona":"2345-689",
        "casa":"2349-0876",
        "celular":"5648-9847"
    }

}
print(mi["codigo"], mi["nombre"], mi["tels"], mi["direccion"]["pais"]["nombre"], mi["direccion"]["departamento"])

copia=mi.copy()
print(copia)

pais=copia.get("direccion")["pais"]["nombre"]
print(pais)
nombre= mi.get("direccion").get("pais").get("codigo")
esqueleto= dict.fromkeys(mi,"")
print(nombre, esqueleto)

items=list(mi.items())
print(items)

claves=list(mi.keys())
print(claves, claves[0])

edad= int(input("Ingrese su edad: "))
if edad<2:
  print("Eres un bebe")
elif edad<12:
  print("Eres un niño")
elif edad<18:
  print("Eres un adolescente")
elif edad<=55:
  print("Eres joven")
elif edad<=65:
  print("Eres un adulto, un señor")
elif edad<=80:
  print("Eres un adulto mayor")
elif edad<130:
  print("Larga vida")
else:
 print("Error en la edad")

 n= int(input("Tabla: "))
i=1
while i<=10:
  print(n,"X",i,"=",n*i)
  i+=1