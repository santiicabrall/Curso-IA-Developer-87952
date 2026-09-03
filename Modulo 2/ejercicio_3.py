'''Ejercicio 3
1. Lee la siguiente situación problemática:
Un empleado cobró 300 dólares por mes desde
enero a junio, 500 dólares de julio a octubre, y
700 dólares por mes en noviembre y en
diciembre.
2. Crea un programa que calcule el sueldo
promedio y que indique si este empleado está
cobrando un sueldo bajo, normal o mejor de lo
normal.
● Sueldo bajo: por debajo de 300 dólares.
● Sueldo normal: entre 300 a 900.
● Sueldo mejor de lo normal: más de 900
dólares.
'''

def calificador_sueldo(sueldo):

    if sueldo < 300:

        return "Sueldo bajo"

    elif sueldo >= 300 and sueldo <= 900: 

        return "Sueldo normal"
    
    elif sueldo > 900:

        return "Sueldo mejor de lo normal"
    
        


enero_junio = 6 * 300
julio_octubre = 4 * 500
nov_dic = 700 * 2 

sueldo_prom = float((enero_junio + julio_octubre + nov_dic) / 12)

print(calificador_sueldo(sueldo_prom))

