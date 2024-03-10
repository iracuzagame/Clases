# range : La función range( ) devuelve una secuencia de números dados
# 3 parámetros.

print(list(range(1,14,3)))

mi_variable = list(range(2000,2560,10))
print(mi_variable)

suma = 0 
for v in range(1,16):
    suma += v**2
print(suma)

#Enumerate: Nos facilita llevar la cuenta de las iteraciones
# Enumerate()

print(list(enumerate("Hola")))

for indice, numero in enumerate ([5.55, 6 , 7.50]):
    print(indice, numero)

lista_Nombres = ["Emanuel", "Abel", "Elisa", "Ana"]
#for Buscar, nombres in enumerate(lista_Nombres):
#    print(f"{nombres} se encuentra en el indice {Buscar}")
for i, nombre in enumerate(lista_Nombres):
    if nombre[0] == "E":
        print(i)

#Zip ()
Letras = ["w", "a", "s"]
numeros = [50, 65, 90, 110, 135]
for letra, num in zip(Letras, numeros):
    print(f"letra: {letra}, y numeros: {num}")

Capitales = ["Berlin", "Tokio", "Paris", "Buenos Aires", "Caracas"]
Paises = ["Alemania", "Japon", "Francia", "Argentina", "Venezuela"]

for cap,pais in zip(Capitales,Paises):
    print(f"La capital de {pais} es {cap}")

Marcas = ["Adidas", "LG"]
Productos = ["Zapatos", "Electrodomestico"]
for m,p in zip(Marcas, Productos):
    print(f"La marca {m} se especializa en {p}")
print("\n")
#Min() y Max()
Ciudades_Habitantes = {"Caracas": 1808, "Venezuela": 2550}
lista_valor = [5**5, 2**2, 3050, 472*2]

print(min(Ciudades_Habitantes.keys()))
print(max(Ciudades_Habitantes.values()))
print(max(lista_valor))