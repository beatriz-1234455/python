from config import *

def janela():
    options = {'padx': 5, 'pady': 5}
    janela= Tk()
    #janela 
    janela.title("Assinatura dos certificados")
    janela.geometry("280x150")
    janela.resizable(False,False)
    
    #comando para centralizar a tela
    larg = 280
    hig = 150
    largura = janela.winfo_screenwidth()
    altura = janela.winfo_screenheight()
    x = largura/2 - larg/2
    y = altura/2.5 - hig/2
    janela.geometry("%dx%d+%d+%d" %(larg, hig, x, y))
    
    #combo box da pesquisa dos cursos
    curso = Label(janela, text="Qual o Curso?\n")
    curso.grid(column=0, row=0, sticky=tk.W, **options)
    pes = Entry(janela, width = 15)
    pes.grid(column=2, row=0, sticky=tk.W, **options)
    
    #cursos
    def pesq():
        global psq
        psq = pes.get()    
    #combo box da quatidade dos alunos    
    label = Label(janela, text="Qual a quantidade \nde alunos?\n")
    label.grid(column=0, row=2, sticky=tk.W, **options)
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

    
    
