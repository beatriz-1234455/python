from tkinter import*

root = Tk()
img = PhotoImage(file="sample\azul.png")

label_imagem = Label(root, image=img).pack()

root.mainloop()