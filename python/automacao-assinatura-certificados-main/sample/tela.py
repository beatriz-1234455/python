from ctypes.wintypes import SIZE
from webbrowser import BackgroundBrowser
from config import *

def janela():
    options = {'padx': 10, 'pady': 10}
    janela= Tk()
    #janela 
    janela.title("Assinatura dos certificados")
    janela.geometry("280x150")
    janela.resizable(False,False)
    

    #comando para centralizar a tela
    larg = 600
    hig = 500
    largura = janela.winfo_screenwidth()
    altura = janela.winfo_screenheight()
    x = largura/2 - larg/2
    y = altura/2.5 - hig/2
    janela.geometry("%dx%d+%d+%d" %(larg, hig, x, y))
    janela.configure(bg='#87CEEB') 
 
    
    #combo box da pesquisa dos cursos
    curso = Label(janela, text="informe o curso:\n",font="YuGothicUISemibold" ,
                  background='#87CEEB', foreground='#4169E1')
    curso.grid(column=5, row=6, sticky=tk.W, **options)
    pes = Entry(janela, width = 40,background='#B0E0E6')
    pes.grid(column=6, row=6, sticky=tk.W, **options)
    
    #cursos
    def pesq():
        global psq
        psq = pes.get()    
    #combo box da quatidade dos alunos    
    label = Label(janela, text="informe a quantidade \nde alunos:\n",font="CenturyGothic",
                  background='#87CEEB', foreground='#4682B4')
    label.grid(column=5, row=9, sticky=tk.W, **options)
    quant = Entry(janela, width = 40,background='#B0E0E6') #tamanho da linha de envio
    quant.grid(column=6, row=9, sticky=tk.W, **options)
    
    #quantidade de alunos
    def qat():
        global qt
        qt = quant.get()
        
    
            
    
    b = Button(janela, text="Enviar", command=lambda :[pesq(), qat(), janela.destroy()]) #função do botão envio e fechar
    b.grid(column=2, row=10, sticky=tk.W, **options) #tamnho do botão
    
   
    janela.mainloop() #manter janela aberta
    
janela()
    
    
    
def pesq():
    print(psq)
    return psq #envio da pesquisa dos diplo0

def enviar():
    print(qt)
    return int(qt) #envio da quantidade de alunos

    
    
