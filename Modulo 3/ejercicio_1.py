'''Ejercicio 1
Función para forzar el ingreso numérico
Crea una función que fuerce el ingreso de solo
números.
● Debe recibir un número por argumento y
verificar que este sea un número posible de
convertir a int.
● En caso contrario, volver a pedir el ingreso
dentro de la función.
● Deber de retornar el valor convertido a int.'''


def solo_numero():

    while True:

        try: 

            numero = int(input('Ingrese un numero: '))
            break

        except ValueError:

            print("¡Valor invalido!")


    print(f"Tu numero es: {numero}")


solo_numero()