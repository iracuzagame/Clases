#Iteracciones entre funciones:  son las salidas de una determinada funcion quye pueden convertirse en entradas de otras funciones
# def funcion 1():
#   return a
# def funcion_2(a):
#   return b
# def funcion_3(b):
#   return c

import random

def lanzar_dados():
    return random.randint(1,6), random.randint(1,6)

def evaluar_jugada(dado1, dado2):
    suma_dados = dado1 + dado2
    if suma_dados <= 6:
        return (f"La suma de tus dados es {suma_dados}. Lamentable")
    elif suma_dados > 6 and suma_dados < 10:
        return (f"la suma de tus dados es {suma_dados}. Tienes oportunidad")
    else:
        return(f"{suma_dados} Parece una jugada ganadora")
    
print(evaluar_jugada(dado1=6, dado2=6))


def reducir_lista(lista):
    lista = list(set(lista))
    lista.sort()
    lista.pop(-1)
    return lista

def promedio(lista):
    valor_promedio = sum(lista)/len(lista)
    return valor_promedio

print(promedio(lista=[1,12,7,5]))

lista_numeros = [1,12,7,15,2,8]

def lanzar_moneda():
    resultado = random.choice(["Cara","Sello"])
    return resultado

def probar_suerte(moneda,lista):
    if moneda == "Cara":
        print("La lista se autodestruirá")
        return []
    elif moneda == "Sello":
        print("La lista se salvará")
        return lista

print(probar_suerte(moneda="Cara", lista=lista_numeros))

# *args :son los casos en los cuales no se conoce el número de argumentos,
# Se escriben despues de los parametros obligatorios 

# def funcion(variable_1, variable_2, *args)
# def funcion(nombre, edad, 40, 50 ,60)

def suma_cuadrados(*args):
    suma = 0
    for args in args:
        suma *= args**2
    return suma

print(suma_cuadrados())

def numero_persona(nombre, *args):
    suma_numeros = sum(args)
    return (f"{nombre}, la suma de tus numeros es {suma_numeros}")

print(numero_persona(nombre="Abel"))

# **kwargs

def cantidad_atributos(**kwargs):
    cantidad = 0
    for clave in kwargs.items():
        cantidad += 1
    return cantidad

def lista_atributos(**kwargs):
    lista = []
    for valor in kwargs.values():
        lista.append(valor)
    return lista