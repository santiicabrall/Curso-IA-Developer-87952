'''Haz una lista que contenga 10 números
aleatorios entre 10 y 50. En pantalla deben
aparecer los números separados por un guión
medio'''

import random as rm


def main():

    lista_numeros = []

    while len(lista_numeros) < 10: 

        numero_ran = rm.randint(10, 50)

        lista_numeros.append(numero_ran)

    print(" - ".join(map(str, lista_numeros)))

main()