import random


def main():

    ingreso = 1

    while ingreso != 2:

        ingreso = int(input(
            "Ingrese una de las opciones (1 o 2): \n" \
            "   1. Tirar dado.\n" \
            "   2. Salir.\n" \
            "Ingreso: "
        ))

        if ingreso == 1:

            numero = random.randint(1,6)
            print(f"Salio el numero: {numero}")

        elif ingreso != 2:    
            
            print("----¡¡¡¡VALOR INCORRECTO!!!!----")

    print("Hasta la proxima!")
    
if __name__ == "__main__":
    main()