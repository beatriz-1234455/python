from tkinter import*


app=Tk()
app.title("imagem quero desistir")
app.geometry("500x500")
app.configure(Background="#4169E1")

# n= norte, s= sul, e = leste, w = oeste
#ne= noroeste, se =sudeste, so= sudoeste, no = nordeste
 
Label(app,text="nome",Background="#4169E1",foregroud="#4169E1",anchor=W).place(x=10, y=10, width=100,height=20)

app.mainloop()