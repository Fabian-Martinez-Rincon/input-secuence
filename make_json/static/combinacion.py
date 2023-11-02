import tkinter as tk
import json

with open('datos_filtrados.json', 'r') as archivo:
    datos = json.load(archivo)

campos = ['R1', 'R2', 'R3', 'R4', 'R5']
indice = 0

def mostrar_registro():
    global indice
    registro = datos[indice]
    valores = [registro[campo] for campo in campos]
    tk.Label(root, text='Ingresar').grid(row=0, column=0)
    valores_str = ''
    for i in enumerate(campos):
        valores_str += str(valores[i]) + '  '
    tk.Label(root, text=valores_str).grid(row=0, column=1)
    indice += 1
    if indice >= len(datos):
        boton.config(state=tk.DISABLED)

root = tk.Tk()
root.title('Datos filtrados')

boton = tk.Button(root, text='Siguiente', command=mostrar_registro)
boton.grid(row=1, column=0, columnspan=2)

mostrar_registro()

root.mainloop()