import pyautogui as p
import time as t
from diplomasauto import diplomas

esp1=0.9  #tempodeespera1
esp2=5    #tempodeespera2
esp3=10   #tempodeespera3
esp4=3.5  #tempodeespera4

v = 130 #diferença entre os butões
x = 1305 #valor fixo do ponto x
y1 = 160 #valor do ponto y do primeiro botão 
xml1 = (y1) #coordenada do primeiro botão
xml2 = (xml1 + v) #coordenada do Segundo botão
xml3 = (xml2 + v) #coordenada do terceiro botão
xml4 = (xml3 + v) #coordenada do quarto botão
xml5 = (xml4 + v) #coordenada do quinto botão

# #imprime o texto
# print("Qual a quantidade de alunos? ")

#recebe o valor referente a quantidade de alunos do devido processo
qt = 12

#valor de aluno por pagina
apl = 5 

#cálculo do numero inteiro referente a quantidade de páginas de 5 alunos
s = (qt//apl)

#cálculo da quantidade de alunos de uma página sem ser de 5 alunos
r =  (qt - apl*s)
    
if qt < apl:  #se a quantidade de alunos imprimida for menor ou igual a 5 alunos
    i = r       #o case receberá a quantidade de alunos de uma página sem ser 5 alunos
elif qt >= apl:  #se a quantidade de alunos for maior que 5 alunos
    i = apl     #o case receberá o case 5

p.hotkey('alt','tab')
t.sleep(esp4)
p.press('pagedown')
t.sleep(esp4)

match i:
 
    case 1:             #para caso de 1 registo de aluno  
         
        p.click(x, xml5)
        t.sleep(esp1)
        diplomas()
        
    case 2:             #para caso de 2 registo de aluno
        
        p.click(x, xml4)
        t.sleep(esp1)
        diplomas() 

        p.click(x, xml5)
        t.sleep(esp1)
        diplomas()  
        
    case 3:             #para caso de 3 registo de aluno
        
        p.click(x, xml3)
        t.sleep(esp1)
        diplomas()

        p.click(x, xml4)
        t.sleep(esp1)
        diplomas()

        p.click(x, xml5)
        t.sleep(esp1)
        diplomas()
        
    case 4:             #para caso de 4 registo de aluno
        
        p.click(x, xml2)
        t.sleep(esp1)
        diplomas()

        p.click(x, xml3)
        t.sleep(esp1)
        diplomas()

        p.click(x, xml4)
        t.sleep(esp1)
        diplomas()

        p.click(x, xml5)
        t.sleep(esp1)
        diplomas()
        
    case 5:             #para caso de 5 registo de aluno       
        #loop para um caso de mais de uma pagina de alunos 
        for n in range(s):         
            
            p.click(x, xml1)
            t.sleep(esp1)
            diplomas()

            p.click(x, xml2)
            t.sleep(esp1)
            diplomas()

            p.click(x, xml3)
            t.sleep(esp1)
            diplomas()

            p.click(x, xml4)
            t.sleep(esp1)
            diplomas()

            p.click(x, xml5)
            t.sleep(esp1)
            diplomas()
    
        # match r:        #caso seja um valor com menos de 5 alunos numa pagina
        #     case 1:     #para caso de 1 registo de aluno 
        #         diplomas()
        #     case 2:     #para caso de 2 registo de aluno 
        #         diplomas()
        #     case 3:     #para caso de 3 registo de aluno 
        #         diplomas()
        #     case 4:     #para caso de 4 registo de aluno 
        #         diplomas()      

#para caso onde o número digitado seja 0 ou qualquer número sem ser inteiro
    case _:
        print("Digite um número maior que 0 e inteiro")