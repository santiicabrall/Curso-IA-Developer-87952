'''Ejercicio 1
Crea un programa para estudiantes que cumpla con
esta tarea: cada alumno debe ingresar su nota y, de
acuerdo con eso, el sistema debe mostrar un mensaje
que diga:
● “Excelente” si la nota es un 10.
● “Muy bien” si está entre 7 y 9.
● “Bien” si está entre un 4 y un 6.
● “Mal” si está entre 0 y 3.
● Si la nota no corresponde a ninguno de estos
valores, mostrar “La nota ingresada es incorrecta”.'''

def calificar(nota):
    
    calificacion = ''

    if nota == 10:

        calificacion = 'Excelente'

    elif nota >= 7 and nota <= 9:

        calificacion = 'Muy bien'

    elif nota >= 4 and nota <= 6:

        calificacion = 'Bien'

    elif nota >= 0 and nota <= 3:

        calificacion = 'Mal'

    else:

        calificacion = 'La nota es incorrecta'

    return calificacion


nota_alumno = int(input("Ingrese su nota: "))

calificacion = calificar(nota_alumno)

print(calificacion)


