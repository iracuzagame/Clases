#Funciones: utilizar la palabra clave def()

def saludar():
    print("Hola mundo")

saludar()

nombre = "Emanuel"
def salu(nombre):
    print(f"Hola {nombre}, Bienvenido!")

salu(nombre)

#num = 5
#def suma(num):
 #   print(num + 2)

#suma(num)

#return 
# def m_funcion():
    #return[algo]
#variable = m_funcion

#def potencia(num1 , num2):
#    return num1**num2

#print(potencia)

dolar = 1200
def usd_eur(dolar):
    return dolar*0,90

print(usd_eur(dolar))

palabra = "Curso de Python"
def invertir_palabra(palabra):
    palabra = palabra[::-1]
    palabra = palabra.upper()
    return palabra

print(invertir_palabra(palabra))

#FUnciones dinámicas: funciones flexibles para utilizar lopp for y while

#def mi_funcion(argumento):
    #for item in iterable:
        #if a == b:
            #...
        #else
            #...
    #return

lista_numeros = [1,2,-4,5,-6,7,8]
def todo_positivo(lista_numeros):
    for numero in lista_numeros:
        if numero < 0:
            return False
        else:
            pass
    return True

lista_numero = [1,2,4,5,6,7,8]
def suma_menores(lista_numero):
    suma = 0
    for num in lista_numero:
        if num in range(0,5):
            suma += num
        else:
            pass
    return suma

print(suma_menores(lista_numeros))