from cProfile import label
from sqlite3 import Row
from tkinter.tix import COLUMN
import pyautogui
import time
from tkinter import *

def funcao ():

timeesp1 = 0.9
timeesp2 = 2.0
time.sleep(5)
#iniciar

pyautogui.click (89,899)
time.sleep (timeesp1)

pyautogui.typewrite('paint')
pyautogui.press ('enter')
time.sleep (timeesp1)
#abrir paint
pyautogui.click(670,165)
time.sleep (timeesp1)
#selecionar quadrado
pyautogui.mouseDown(566,557)
time.sleep (timeesp1)

pyautogui.mouseUp(857,424)
time.sleep (timeesp1)
pyautogui.moveTo (421,568)
pyautogui.moveTo (421,568)
pyautogui.moveTo 

pyautogui.typewrite('teste teste')
pyautogui.hotkey('ctrl','s')

pyautogui.rightClick(456,247)
time.sleep (timeesp1)

pyautogui.click(496,803)
time.sleep (timeesp1)

pyautogui.click(797,820)
time.sleep (timeesp1)

pyautogui.press(['t','e','s','t','e','enter',])
time.sleep (timeesp2)

pyautogui.doubleClick(291,432)
time.sleep (timeesp1)

pyautogui.click(344,607)


janela = Tk()

janela.title("titulo")
#titulo da janelaff
text1 = Label(janela, text="test test test test test test ")
text1.grid(column=0, row=0)
#texto na janela, column = coluna, row = linha, grid = posição
text2 =  Label(janela, text="isso é apenas um teste. ")
text2.grid(column= 0, row=2 )

botao1 = Button(janela, text="iniciar", command = funcao)
botao1.grid(column=2, row = 4)

iniciar_funcao = label(janela, text= "")
iniciar_funcao.grid(column = 0, Row =6 )
 
janela.mainloop()