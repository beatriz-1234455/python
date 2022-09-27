from msilib.schema import Feature
from winreg import REG_LINK
from config import *

def janela():
    options = {'padx': 60, 'pady': 40}
    janela= Tk()
    #janela 
    janela.title("Assinatura dos certificados")
    janela.geometry("700x400")
    janela.resizable(False,False)
    bg = PhotoImage(file = "janela/gato.png")
    label1 = Label( janela, image = bg)   
    label1.place(x = 0, y = 0) 
    
    #comando para centralizar a tela
 
    larg = 700
    hig = 400
    largura = janela.winfo_screenwidth()
    altura = janela.winfo_screenheight()
    x = largura/2 - larg/2
    y = altura/2.5 - hig/2
    janela.geometry("%dx%d+%d+%d" %(larg, hig, x, y))
    
    #combo box da pesquisa dos cursos
    curso = Label(janela, text="Qual o Curso?\n")
    curso.grid(column=6, row=3, sticky=tk.W, **options)
    pes = Entry(janela, width = 15)
    pes.grid(column=7, row=3, sticky=tk.W, **options)
    
    #cursos
    def pesq():
        global psq
        psq = pes.get()    
    #combo box da quatidade dos alunos    
    label = Label(janela, text="Qual a quantidade \nde alunos?\n", background="white")
    label.grid(column=6, row=4, sticky=tk.W, **options)
    
    #label1 = Label (janela, text="centro?", font="Arial 20",background="black", anchor=tk.CENTER)
    
    
    
    quant = Entry(janela, width = 15) #tamanho da linha de envio
    quant.grid(column=2, row=2, sticky=tk.W, **options)
    
    #quantidade de alunos
    def qat():
        global qt
        qt = quant.get()
        
    
            
    
    b = Button(janela, text="Enviar", command=lambda :[pesq(), qat(), janela.destroy()]) #função do botão envio e fechar
    b.grid(column=2, row=3, sticky=tk.W, **options) #tamnho do botão
    
   
    janela.mainloop() #manter janela aberta
    
janela()
    
    
    
def pesq():
    print(psq)
    return psq #envio da pesquisa dos diplo

def enviar():
    print(qt)
    return int(qt) #envio da quantidade de alunos

    
    
