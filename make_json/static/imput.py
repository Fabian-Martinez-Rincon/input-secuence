import pygetwindow as gw
import pyautogui

titulo_base = "Command Prompt"  


for numero in range(1, 11):

    while True:
        ventana = gw.getWindowsWithTitle(titulo_base)
        if ventana:
            break  
        else:
            pyautogui.sleep(1)

    ventana[0].activate()

    pyautogui.write(str(numero))

    pyautogui.press('enter')
    
    pyautogui.sleep(1)

    continue