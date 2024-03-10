#Loops for 
# for item in iterable (sring, lista,dicionario, entre otros)

alumnos_clases=["Emanuel", "Abel", "Elisa", "Alirio"]

    # Items: puede ser de cualquier valor string
for apellidos in alumnos_clases:
    print(f"Hola {apellidos}")

lista_numeros= [1,2,3,4,5,6,7]
suma_numeros = 0

for numero in lista_numeros:
    suma_numeros= suma_numeros + numero
    print(suma_numeros)


lista_de_numeros= [1,2,3,4,5,6,7,8,2,9,4,5]
suma_pares = 0
suma_impares = 0

for numeros in lista_de_numeros:
    if numeros % 2 == 0:
        suma_pares = suma_pares + numeros
    else:
        suma_impares = suma_impares + numeros

print(f"Tus numeros pares son: {suma_pares} y los impares son: {suma_impares}")

#Loops while

#n = 10
#while n >= 0:
#    if n % 5 ==0:
#        print(n)
#        n -= 1
#    else:
#        n -= 1
#        impares = n
#        print(impares)

num_lista = [4,6,9,-4,7,-5,5,-6,-7,8]
for num in num_lista:
    if num >= 0:
        print(num)
    else:
        break
