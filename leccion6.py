#Random: es una funcion de python para la selección aleatoria entre valores y/o secuencias.

#from random import *

#Metodos de random: randint,uniform,random,choice, shuffle

from random import *

aleatorio = randint(1,10)
print(f"tu numero es {aleatorio}")

Alea = random()
print(Alea)

lista = ["Carlos", "Emanuel", "Abel"]
sorteo = choice(lista)
print(f"El ganador es {sorteo}")

#Comprension de listas:
# nueva_lista = [expresion for item in iterable if condicion == true]

nueva_lista = [num**2 for num in range(10) if num < 5]
print(nueva_lista)

valores = [1,2,3,4,5,6,9.5]
#valores_cuadrados = [valor**2 for valor in valores]
valores_cuadrados = [valor for valor in valores if valor %2 == 0]
print(valores_cuadrados)

