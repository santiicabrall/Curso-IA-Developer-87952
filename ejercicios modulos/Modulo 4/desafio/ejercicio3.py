import random
import tkinter as tk


    #numero = random.randint(1,6)

def girar_dado():
    pass


ventana = tk.Tk()

ventana.title("Tirar dado")
ventana.geometry("500x500")

boton = tk.Button(
    ventana,
    text="ARROJAR DADO",
    command=girar_dado
    )
boton.pack()

label_resultado = tk.Label(
    ventana,
    text="Salio:"
    )
label_resultado.pack()

caja = tk.Entry(
    ventana,
    
)




ventana.mainloop()