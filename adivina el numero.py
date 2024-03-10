from random import *

intentos = 0
estimado = 0
numero_secreto = randint(1,100)
nombre = input("Dime tu nombre: ")
print("\n")
print(f"Bueno {nombre}, he pensado un número entre el 1 y el 100")

while intentos < 8:
    estimado = int(input("Cuál es el número?: "))
    intentos +=1

    if estimado < numero_secreto:
        print("Mi numero es mas alto")
    elif estimado > numero_secreto:
        print("Mi numero es mas bajo")
    else:
        print(f"Felicitaciones {nombre}: Has adivinado el numero")
        break

if estimado != numero_secreto:
    print(f"Lo siento, se han agotado los intentos. Vuelve a intentarlo")