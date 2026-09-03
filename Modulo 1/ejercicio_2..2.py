
'''2. Dada esta situación:
Una juguetería tiene mucho éxito en la venta de
dos de sus productos: payasos y muñecas. Suele
hacer ventas por correo y la empresa de logística
les cobra por el peso de cada paquete, por lo que
necesitan calcular el peso de los payasos y
muñecas que saldrán en cada paquete a
demanda. Cada payaso pesa 112 g y cada
muñeca, 75 g.
Ejercicio 2
Escribe un programa que:
● Solicite al usuario el número de payasos y
muñecas vendidos en el último pedido.
● Calcule el peso total del paquete que será
enviado'''



payaso = 112
muñeca = 75

nro_payasos = int(input("Ingrese el numero de payasos vendidos en el ultimo pedido: "))
nro_muñecas = int(input("Ingrese el numero de muñecas vendidas en el ultimo pedido: "))

peso_del_paquete = (nro_muñecas * 75) + (nro_payasos * 112)

print(f"El paquete pesa {peso_del_paquete} gr.")