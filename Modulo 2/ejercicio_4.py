
def es_bisiesto(año):

    if (año % 400 == 0):

        return "Es bisiesto"

    elif (año % 100 != 0) and (año % 4 == 0):

        return "Es bisiesto"

    else:

         return "No es bisiesto"



año = int(input("Ingrese un año: "))
print(es_bisiesto(año))


