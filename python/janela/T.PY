from tkinter import *

root = Tk()
root.geometry("700x500") 
bg = PhotoImage(file = "janela/gato.png")
label1 = Label( root, image = bg) 
label1.place(x = 0, y = 0) 
root.mainloop()