'''Ejercicio 2
Desarrolla un programa que cumpla los
siguientes pasos:
1. Se preguntará el tipo de rol que desempeña
una persona en una institución por una
entrada del tipo input. Los valores posibles
son “admin” o “profesor”.
2. Luego, si la persona es “admin” o “profesor”,
se debería pedir la contraseña, siendo la única
válida “1234” (la contraseña se toma como
string).
3. Si la contraseña ingresada es válida, se
pedirá el nombre de la persona, y si no es
vacío, se la saludará.
Contemplar los casos donde no se cumple como
corresponde y mostrar un mensaje en pantalla.
'''

admin = 'admin'
profesor = 'profesor'
right_password = "1234"

rol = input("Enter your rol (admin/profesor): ")

if rol == admin or rol == profesor:

    password = input("Enter the password: ")

    if password == right_password:

        name = input("Enter your name: ")

        if name == "":

            print("Empty name!")

        else:

            print(f"Hello {name}!!")

    else:

        print("Wrong password!!")

else:

    print("This roll doesn't exist!")