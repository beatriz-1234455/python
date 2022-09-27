import pyautogui
import time
    #abrir windows
pyautogui.press('win')
time.sleep(1.9)
    #pesquisar na barra
pyautogui.write("remot")
time.sleep(0.9)
    #logar 
pyautogui.press('enter')
time.sleep(1.9)

pyautogui.press('enter')
time.sleep(0.9)

    #colocar senha 
pyautogui.write("masterFVJFVJ@%$&")
time.sleep(1.9)
    #entrar no servidor
pyautogui.press('enter')
time.sleep(0.9)
#fechar servidpr
pyautogui.click(1042,12)
time.sleep(1.9)
#fechar vereficação
pyautogui.click(780,514)
time.sleep(1.9)
#fechar 
pyautogui.click(1144,443)
time.sleep(0.9)
