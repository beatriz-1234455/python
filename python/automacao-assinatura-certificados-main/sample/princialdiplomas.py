from config import *  
from Viewass import enviar, pesq ,janela

esp2=5
esp3=10
esp4=3.5

#p.hotkey('alt','tab')
#time.sleep(esp1 )
#p.hotkey('f5')
#time.sleep(esp2)
#p.press('pagedown')
#time.sleep(esp2)

v = 130 #diferença entre os butões
x = 1305 #valor fixo do ponto x
y1 = 160 #valor do ponto y do primeiro botão 
xml1 = (y1) #coordenada do primeiro botão
xml2 = (xml1 + v) #coordenada do Segundo botão
xml3 = (xml2 + v) #coordenada do terceiro botão
xml4 = (xml3 + v) #coordenada do quarto botão
xml5 = (xml4 + v) #coordenada do quinto botão



janela() ##dar um jeito de importar o qt pra cá
qt = enviar()
#valor de aluno por pagina
apl = 5 

#cálculo do numero inteiro referente a quantidade de páginas de 5 alunos
s = (qt//apl)

#cálculo da quantidade de alunos de uma página sem ser de 5 alunos
r =  ( qt - apl*s)
    

if qt <=  apl:  #se a quantidade de alunos imprimida for menor ou igual a 5 alunos
    i = r       #o case receberá a quantidade de alunos de uma página sem ser 5 alunos
elif qt > apl:  #se a quantidade de alunos for maior que 5 alunos
    i = apl     #o case receberá o case 5

match i:
 
    case 1:             #para caso de 1 registo de aluno   
        print("caso1")
    case 2:             #para caso de 2 registo de aluno
        print("caso2")  
    case 3:             #para caso de 3 registo de aluno
        print("caso3")
        ###acho que a seta de passar pagina vai dentro desses aqui###
    case 4:             #para caso de 4 registo de aluno
        print("caso4")
    case 5:             #para caso de 5 registo de aluno       
        #loop para um caso de mais de uma pagina de alunos 
        for n in range(s):         
            
            print("caso5")
    
        match r:        #caso seja um valor com menos de 5 alunos numa pagina
            case 1:     #para caso de 1 registo de aluno 
                print("caso1")
            case 2:     #para caso de 2 registo de aluno 
                print("caso2")
            case 3:     #para caso de 3 registo de aluno 
                print("caso3")
            case 4:     #para caso de 4 registo de aluno 
                print("caso 4")       

#para caso onde o número digitado seja 0 ou qualquer número sem ser inteiro
    case _:
        print("Digite um número maior que 0 e inteiro")