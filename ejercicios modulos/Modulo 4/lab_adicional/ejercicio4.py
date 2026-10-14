'''Crea una aplicación de escritorio con dos cajas
de texto y un botón, de modo que al presionarlo
se imprima en pantalla la suma de los dos
números ingresados en las primeras.
La disposición de los controles y el tamaño de la
ventana quedan a tu criterio.'''

import tkinter as tk

def sumar(numero1, numero2):
    return numero1 + numero2

def obtener_numeros():
    numero1 = float(entrada1.get())
    numero2 = float(entrada2.get())

    resultado = sumar(numero1, numero2)

    #config() sirve para modificar las propiedades de un elemento de Tkinter después de haberlo creado.
    label_numero.config(text=resultado)

ventana = tk.Tk()

ventana.title("Suma de numeros")
ventana.geometry("500x500")

label1 = tk.Label(
    ventana,
    text = "Primer numero:"
    )
label1.pack()

entrada1 = tk.Entry(ventana)
entrada1.pack()

mas = tk.Label(
    ventana, 
    text = "+",
    font=("Arial", 20, "bold")
    )
mas.pack()

label2 = tk.Label(
    ventana,
    text= "Segundo numero:"
    )
label2.pack()

entrada2 = tk.Entry(ventana)
entrada2.pack()

boton = tk.Button(
    
    ventana,
    text="Sumar",
    command=obtener_numeros,
    
    )
boton.pack()

label_resultado = tk.Label(
    ventana,
    text="RESULTADO"
    )
label_resultado.pack()

flecha = tk.Label(
    ventana,
    text="||\n" \
    "\/"
    )
flecha.pack()

label_numero = tk.Label(
    ventana,
    text="",
    relief="solid",
    width=10
)
label_numero.pack()

ventana.mainloop()