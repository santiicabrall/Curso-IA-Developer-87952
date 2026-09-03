'''Escribe un programa que permita crear una lista
de nombres.
Para ello, el programa debe pedir un número y
luego solicitar esa cantidad de nombres para
crear la lista. Por último, el programa tiene que
mostrar la lista creada.'''

nombres = []
i = 0

cant_nombres = int(input("Enter a number of names: "))

while i < cant_nombres:

    nombres.append(input(f"Enter the name number {i + 1}: "))
    
    i += 1

print("The names that you entered are: ")

for nombre in nombres:

    print(nombre)
    

