'''Desarrolla una función que reciba una lista con
números enteros y devuelva en una matriz:
● Como primer elemento, una lista con los
números pares.
● Como segundo elemento, una lista de los
números impares de la lista recibida.
'''

def separador(lista : list):

    pares = []
    impares = []

    for num in lista:
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)

    return [pares, impares]

lista = [1,2,3,4,5,6,7,8,9,10]
print(separador(lista))
    
        

