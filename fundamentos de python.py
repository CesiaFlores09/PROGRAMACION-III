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
