#Las listas son secuencias ordenadas de objetos. Estos objetos
#pueden ser datos de cualquier tipo: strings, integers, floats,
#booleanos, listas, entre otros. Son tipos de datos mutables.
#Una lista se define con los []
#          0        1      2           3      4
lista = ["Html", "Css", "Python", "Javascript"]

print(lista)
print(len(lista))
print(lista[0:4])
print(f"Vamos aprender este lenguaje {lista[2:3]}")

lista.append("Lua")

lista_2 = ["Hola", "Mundo"]

concatenar = lista + lista_2
print(concatenar)
print(len(concatenar))

print(lista.pop(4))
print(lista)

lista_3 = ["g","a","d","b"]
lista_3.sort()
print(lista_3)

lista.sort()
print(lista)

lista.reverse()
print(lista)
print(lista[2:3])

#Los diccionarios son estructuras de datos que almacenan
#información en pares clave:valor. Son especialmente útiles
#para guardar y recuperar información a partir de los nombres
#de sus claves (no utilizan índices)

mi_diccionario = {"Curso":"Python" , "Clase":"diccionario"}

Datos_personales = {"Nombre": "Abel" " Jose", "Curso":"Python", "Profesion":"Programador"}
Datos_personales["Apellido"] = ["Serra"]
print(Datos_personales)
print(Datos_personales["Nombre"])

# Los tuples o tuplas, son estructuras de datos que almacenan
#múltiples elementos en una única variable. Se caracterizan por
#ser ordenadas e inmutables. Esta característica las hace más
#eficientes en memoria y a prueba de daños.

mi_tupla = (1,"dos", [3.33,"cuatro"], (5.0, 6))
print(mi_tupla[0:4])
a,b,c,d = mi_tupla
print(d)
Conversion = list(mi_tupla)
print(Conversion)