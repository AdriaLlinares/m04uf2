#!/bin/bash/python3

version = 0.5

title = "Playlist v"+str(version)

def saluda() : 
	print("Hola")



def suma(num1, num2):
	return num1 + num2

def despide (quien="Jacinto"):
	print ("Estas despedido", quien)

def return_multiple ():
	uno = 1 
	dos = 2

	return uno,dos

print ("-"*len(title))

primero = 4
segundo = 4


if primero > segundo:
	print ("El primero es mayor que el segundo")
elif primero < segundo:
	print ("El segundo es mayor que el primero")
else:
	print ("Son iguales")

contador = 10

while contador > 0:
	print (contador)
	contador -= 1

personas =["jacinto", "xavi", "juan"]

for dato in personas:
	print (">", dato) 

array = ["adria", "1", "alex"]

print (array[0])

personaje = {
	"nombre": "paco",
	"edad": 31,
	"peso": "100"+str("kg")

}
for dato in personaje:
	print (">>", personaje[dato])


for dato, clave in personaje.items():
	print (">>>", dato, clave)


saluda()

resultado = suma (3, 6)
print (resultado)

despide()
despide("adria") 

valor1, valor2 = return_multiple()

print ("Valores:", valor1, valor2)



nombre = input("¿Como te llamas?: ")
print (nombre)
