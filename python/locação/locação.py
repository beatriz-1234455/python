from tkinter import *
from tkinter import font
from tkinter.ttk import *
import tkinter.ttk as ttk
from config import *
from fonte import *

options = {'padx': 5, 'pady': 5}
janela= Tk()
style = ttk.Style() 
 
#titulo da janela
janela.title("locação de equipamento unijaguaribe")
#tamanho da janela 
janela.geometry("1000x700")

janela.resizable(False,False)
#background da janela 
janela.config(background="#1f3347")
#icone da janela 
janela.iconbitmap("img/brasão_colorido.ico")
#imagem background
#bg = PhotoImage(file = "janela/gato.png")
#label1 = Label( janela, image = bg)   
#label1.place(x = 0, y = 0) 

#centralizar janela 
larg = 1200
hig = 700
largura = janela.winfo_screenwidth()
altura = janela.winfo_screenheight()
x = largura/2 - larg/2
y = altura/2.5 - hig/2
janela.geometry("%dx%d+%d+%d" %(larg, hig, x, y))

#fonte da letra
fonte1 = tk.font.Font(family = "Consolas", size = 13)
fonte2 = tk.font.Font(family=  "Viner Hand ITC", size = 15)
#logo do canto
logo = PhotoImage(file = r"img\brasão_colorido.png") 

# x horizontal
# y vertical
# width lagura
# height altura

imagem =  Label(janela,image=logo).pack()
#Button(janela, text = 'Click Me !', image = logo).pack(side = TOP)


frame1 = tk.Frame(master=janela, width=1050, height=580, bg="#dddddd")
frame1.place(x=75, y=75)

label = Label(text="EQUIPAMENTOS DISPONIVEIS", font=fonte1, foreground="black", background="#dddddd")
label.place(x=500, y=90)

#frame2 = tk.Frame(master=janela, width=350, height=550, bg="#dddddd")
#frame2.place(x=800, y=75)

#frame3 = tk.Frame(master=janela, width=300, height=500, bg="black")
#frame3.place(x=820, y=100)

#frame3 = tk.Frame(master=janela, width=610, height=500, bg="#e6e6e6")
#frame3.place(x=100, y=108)

#,borderwidth=1, relief="solid"




janela.mainloop()

#https://programadoresbrasil.com.br/2021/05/layout-tkinter/
#borderwidth=1 (largura da borda)
# relief=" "(tipo de borda)
#   "solid" (solido acho q é auto explicativo/cor preta)
#   "flat" (aparentemente transparente)
#   "raised" (parece um botao levantando)
#   "sunken" (parece um botao abaixado)   
#   "ridge" (cor clara) 
#   "groove" (degradê)

# x horizontal
# y vertical
# width lagura
# height altura
