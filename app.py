import tkinter as tk
import json
import pygetwindow as gw
import pyautogui
import os

indice = 0
TITULO_BASE = 'Command Prompt'
CAMPOS = ['SIMBOLO', 'SIMBOLO.1', 'SIMBOLO.2', 'SIMBOLO.3', 'SIMBOLO.4', 'R1', 'R2', 'R3', 'R4', 'R5']

def mostrar_registro(datos, boton):
    #os.system('cls')

    while True:
        ventana = gw.getWindowsWithTitle(TITULO_BASE)
        if ventana:
            break  
        else:
            pyautogui.sleep(1)
    ventana[0].activate()

    global indice
    registro = datos[indice]
    valores = [registro[campo] for campo in CAMPOS]
    r_valores = {campo: valores[i] for i, campo in enumerate(CAMPOS) if campo.startswith('R')}
    simbolo_valores = {campo: valores[i] for i, campo in enumerate(CAMPOS) if campo.startswith('SIMBOLO')}

    r_valores_text = ", ".join([f'{valor}' for campo, valor in r_valores.items()])
    simbolo_valores_text = ", ".join([f'{valor}' for campo, valor in simbolo_valores.items()])
    
    print(r_valores_text)
    print(simbolo_valores_text)

    pyautogui.write(str(r_valores_text))
    pyautogui.press('enter')
    
    indice += 1
    if indice >= len(datos):
        boton.config(state=tk.DISABLED)

def main():
    with open('./static/datos_filtrados.json', 'r') as archivo:
        datos = json.load(archivo)

    CAMPOS = ['SIMBOLO', 'SIMBOLO.1', 'SIMBOLO.2', 'SIMBOLO.3', 'SIMBOLO.4', 'R1', 'R2', 'R3', 'R4', 'R5']
    root = tk.Tk()
    root.title('Datos filtrados')
    root.geometry('100x250')

    boton = tk.Button(root, text='Siguiente', command=lambda: mostrar_registro(datos, boton))
    boton.grid(row=len(CAMPOS), column=0, columnspan=2)

    mostrar_registro(datos, boton)

    root.mainloop()

if __name__ == '__main__':
    main()