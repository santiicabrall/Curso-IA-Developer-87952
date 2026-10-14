'''Generar un rango con una función
Crea una función rango (desde, hasta, intervalo)
que retorne una lista de números, tal como la
función incorporada range(), aunque según el
intervalo especificado.
'''
def rango(desde = 0, hasta = None, intervalo = 1):

    if hasta == None:

        return ValueError("Este campo no puede estar vacio")
    
    elif desde == '':

        desde = 0

    i = desde
    numeros = []
    

    while i < hasta:

        numeros.append(i)

        if intervalo == 0 or intervalo == '':
            i += 1
        else:
            i += intervalo

        

    return numeros

lista_nums = rango(hasta = 5)
print(lista_nums)
