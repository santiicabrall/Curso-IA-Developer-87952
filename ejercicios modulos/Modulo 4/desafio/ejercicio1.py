'''Escribe una función que sirva para multiplicar
cada elemento de una lista numérica por un
valor (ambos deben ser parámetros de función);
y devuelva la nueva lista con cada elemento en
su respectiva posición, pero ya multiplicado. '''

def mult_list(lista : list, valor : int):

    lista_multiplicada = []

    for num in lista:
        result = num * valor
        lista_multiplicada.append(result)

    return lista_multiplicada


lista = [1,2,3,4,5]
print(mult_list(lista, 2))