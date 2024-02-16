# Booleanos, operadores, if else y elif


Num1 = float(input("Dime un numero que se te venga en la cabeza: "))

Num2 = float(input("Otro numero por favor: "))

Num3 = float(input("Uno mas: "))

suma = Num1 + Num2 + Num3

if suma >= 7 and Num1 == 2:
    print(f"tu total es {suma}")
elif suma <= 0 and suma >=8:
    print(f"Haz ingresado los siguientes números: {int(Num1)}, {int(Num2)} y por ultimo {int(Num3)}")
else:
    print("Me gusta jugar contigo")


print(suma)

print(type(suma))

# Operadores

nivel_1 = 4.5456
nivel_2 = 200.000
nivel_3 = 10.1156
Pun_jugador = nivel_1 + nivel_2 + nivel_3
print(round(Pun_jugador,2))
print(f"Tus puntos como jugador son de {round(Pun_jugador,2)}pts")

#f es la abreviatura de Formatear, eso significa que puedes utilizar palabras con variables.

Potencia = 5**2
print(Potencia)

Doble_puntos = Pun_jugador**2
print(f"Hoy tus puntos son el doble {round(Doble_puntos,2)}pts")

# Booleanos (True y False)
Doble_puntos= False
print(Doble_puntos)

#Condicionales (If, else y elif)

#Condicional para doblar puntos
if nivel_1 > 5:
    Doble_puntos = nivel_1**2
    print(f"Tus puntos se han duplicado {round(Doble_puntos,2)}pts")
if nivel_1 >= 4 and nivel_3 >= 20:
    print("Estos dos niveles cumplen con doble puntos")
elif nivel_2 > 500:
    Doble_puntos = nivel_2**2
    print(f"Tus puntos se han duplicado {round(Doble_puntos,2)}pts")
else:
    print(f"Tus puntos son {round(Pun_jugador,2)}pts y no cumplen con el requirimiento mínimo para el doble de puntos")


if nivel_1 >= 4:
    print(True)
else:
    print(False)

#Listas, tuplas, diccionarios y si nos da tiempo vemos Bucles