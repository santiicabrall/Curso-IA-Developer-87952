import random


numero_oculto = random.randint(10, 40)

intentos = 5

while intentos > 0:

    numero = int(input("Adivina el número (entre 10 y 40): "))

    if numero == numero_oculto:
        print("¡Felicitaciones! Adivinaste el número")
        break

    elif numero < numero_oculto:
        print("El número oculto es mayor")

    else:
        print("El número oculto es menor")

    intentos -= 1
    print(f"Te quedan {intentos} intentos.")

if intentos == 0:
    print(f"Perdiste. El número oculto era {numero_oculto}")