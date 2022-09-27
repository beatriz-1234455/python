from cProfile import label
from cgitb import text
from turtle import width
from tkinter import *

def test():
    
    janela= Tk()
    janela.title("certificados")
    janela.geometry("200x150")
    label = Label(janela, text="Qual a quantidade de alunos?\n")
    label.grid(row=0, column=0)
    qt = Entry(janela, width = 15)
    qt.grid(row=2, column=0)

    global qt1

    #global qt1
    #qt1= int (input())
    qt1 = qt.get() 

    b = Button(janela, text="clicar", command=test)
    b.grid(row=3, column=0)
    janela.mainloop()