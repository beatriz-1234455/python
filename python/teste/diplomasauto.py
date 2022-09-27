import pyautogui as p
import time 

esp1=0.9
esp2=7.7
esp3=12.7
esp4=1.5

def diplomas():
   
    #clicar no jonatha
    p.click(649, 505) 
    time.sleep(esp1)

    #clicar no token jonathan
    p.click(578, 478)
    time.sleep(esp1)

    #assinar diploma
    p.click(637, 546)
    time.sleep(esp2)

    #senha do 123456
    
    p.write("1234")
    time.sleep(esp4)
    p.press('enter')
    time.sleep(esp3)

    #assinatura unijaguaribe
    p.click(803, 500)
    time.sleep(esp1)

    #click no token unijb
    p.click(646, 516)
    time.sleep(esp1)

    #assinar diploma
    p.click(637, 546)
    time.sleep(esp2)

    #senha unijb
    p.write("123456")
    time.sleep(esp4)
    p.press('enter')
    time.sleep(esp3)

    #assinatura unijaguaribe2
    p.click(1063, 497)
    time.sleep(esp1)

    #click no token unijb2
    p.click(646, 516)
    time.sleep(esp1)

    #assinar diploma2
    p.click(637, 546)
    time.sleep(esp2)

    #senha unijb2
    p.write("123456")
    time.sleep(esp4)
    p.press('enter')
    time.sleep(esp3)
    #atualizar pagina
    # p.press('f5')
    # time.sleep(esp2)
    #fechar pagina
    p.click(1152, 364)
    time.sleep(esp4)