import tkinter as tk
import json
import pygetwindow as gw
import pyautogui
import os

indice = 0
#TITULO_BASE = 'Command Prompt'
#TITULO_BASE = 'Command Prompt'
TITULO_BASE = input("Por favor, ingrese una cadena: ")
CAMPOS = ['SIMBOLO', 'SIMBOLO.1', 'SIMBOLO.2', 'SIMBOLO.3', 'SIMBOLO.4', 'R1', 'R2', 'R3', 'R4', 'R5']
ARCHIVO_DATOS = 'data_example.json'

def activar_ventana():
    """Espera a que se abra la ventana y la activa"""
    while True:
        ventana = gw.getWindowsWithTitle(TITULO_BASE)
        if ventana:
            break  
        else:
            pyautogui.sleep(1)
    ventana[0].activate()


def mostrar_registro(datos, boton):
    os.system('cls')

    activar_ventana()

    global indice
    registro = datos[indice]
    valores = [
        registro[campo] 
        for campo in CAMPOS
        ]

    r_valores_text = ", ".join([
        str(valores[i]) 
        for i, campo in enumerate(CAMPOS) 
        if campo.startswith('R')
    ])

    simbolo_valores_text = ", ".join([
        str(valores[i]) 
        for i, campo in enumerate(CAMPOS) 
        if campo.startswith('SIMBOLO')
    ])

    print('Nro:' + str(indice + 1))
    print(r_valores_text)
    print(simbolo_valores_text)
    pyautogui.write(str(r_valores_text))
    pyautogui.press('enter')
    
    indice += 1
    if indice >= len(datos):
        boton.config(state=tk.DISABLED)

def main():
    with open(ARCHIVO_DATOS, 'r') as archivo:
        datos = json.load(archivo)

    root = tk.Tk()
    boton = tk.Button(root, text='Siguiente', command=lambda: mostrar_registro(datos, boton))
    boton.grid(row=1, column=0, columnspan=2)

    mostrar_registro(datos, boton)

    root.mainloop()

if __name__ == '__main__':
    main()