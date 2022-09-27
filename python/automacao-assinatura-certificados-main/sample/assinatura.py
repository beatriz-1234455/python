from config import *
from WEBVIEW import nave
esp1=0.9
esp2=7.7
esp3=12.7
esp4=1.5

def privado():
   
    #clicar no Jhonnatha
    nave.find_element(By.XPATH,'')
    p.click(649, 505) 
    t.sleep(esp1)

    #clicar no token Jhonnatha
    nave.find_element(By.XPATH,'')
    p.click(578, 478)
    t.sleep(esp1)

    #assinar diploma
    nave.find_element(By.XPATH,'')
    p.click(637, 546)
    t.sleep(esp2)

    #senha do 123456
    
    p.write("1234")
    t.sleep(esp4)
    p.press('enter')
    t.sleep(esp3)

    #assinatura unijaguaribe
    nave.find_element(By.XPATH,'')
    p.click(803, 500)
    t.sleep(esp1)

    #click no token unijb
    nave.find_element(By.XPATH,'')
    p.click(646, 516)
    t.sleep(esp1)

    #assinar diploma
    nave.find_element(By.XPATH,'')
    p.click(637, 546)
    t.sleep(esp2)

    #senha unijb
    p.write("123456")
    t.sleep(esp4)
    p.press('enter')
    t.sleep(esp3)

    #assinatura unijaguaribe2
    nave.find_element(By.XPATH,'')
    p.click(1063, 497)
    t.sleep(esp1)

    #click no token unijb2
    nave.find_element(By.XPATH,'')
    p.click(646, 516)
    t.sleep(esp1)

    #assinar diploma2
    nave.find_element(By.XPATH,'')
    p.click(637, 546)
    t.sleep(esp2)

    #senha unijb2
    nave.find_element(By.XPATH,'')
    p.write("123456")
    t.sleep(esp4)
    p.press('enter')
    t.sleep(esp3)
    
    #fechar pagina
    nave.find_element(By.XPATH,'')
    p.click(1152, 364)
    t.sleep(esp4)
     
def publico():
    #clicar na segunda ass
    nave.find_element(By.XPATH,'')
    p.click(649, 505) 
    t.sleep(esp1)

    #clicar no token 
    nave.find_element(By.XPATH,'')
    p.click(578, 478)
    t.sleep(esp1)

    #assinar diploma
    nave.find_element(By.XPATH,'')
    p.click(637, 546)
    t.sleep(esp2)

    #senha do 
    
    p.write("fvj@1234")
    t.sleep(esp4)
    p.press('enter')
    t.sleep(esp3)
    
    #clicar no ass
    nave.find_element(By.XPATH,'')
    p.click(649, 505) 
    t.sleep(esp1)

    #clicar no token 
    nave.find_element(By.XPATH,'')
    p.click(578, 478)
    t.sleep(esp1)

    #assinar diploma
    nave.find_element(By.XPATH,'')
    p.click(637, 546)
    t.sleep(esp2)

    #senha do 
    
    p.write("1234")
    t.sleep(esp4)
    p.press('enter')
    t.sleep(esp3)