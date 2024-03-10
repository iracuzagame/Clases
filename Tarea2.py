poema = input("Hola, me podrias decir un poema por favor? ")
lista = []
poema = poema.lower()
lista.append(input("interesante... me podrias decir una letra? ".lower()))
lista.append(input("otra por favor ".lower()))
lista.append(input("una ultima... ".lower()))

#Primera parte
print("las letras que se encontraron: ")
letra1 = poema.count(lista[0])
letra2 = poema.count(lista[1])
letra3 = poema.count(lista[2])
print(f"{lista[0]} {letra1},{lista[1]} {letra2},{lista[2]} {letra3}")

#Segunda parte
inicio = poema[0]
fin = poema[-1]
print(f"esta fue la primera letra  '{inicio}' y ultima letra '{fin}'" ) 

#Tercera parte
frase = poema.split()
frase.reverse()
textoinvertido = " ".join(frase)
print(textoinvertido)

#Cuarta parte
mi_diccionario = {True:"Si" , False:"No"}
print("Buscando la palabra python...")
python = "python" in poema
print(f"python {mi_diccionario[python]} aparece")