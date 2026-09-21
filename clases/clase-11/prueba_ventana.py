import tkinter as tk

# Crear ventana
ventana = tk.Tk()
ventana.title("Mi ventana")
ventana.geometry("640x480")

# Crear Label
texto = tk.Label(ventana, text="Hola, esta es mi ventana")
texto.pack(pady=20)

# Crear botón Salir
boton_salir = tk.Button(ventana, text="Salir", command=ventana.destroy)
boton_salir.pack()

# Mantener la ventana abierta
ventana.mainloop()