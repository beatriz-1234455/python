from config import *
from Viewass import pesq
# servico = Service(ChromeDriverManager().install())
# nave = webdriver.Chrome(service=servico)


tesp1=1
tesp2=2
tesp3=3
tesp4=4
tesp5=5
psq= pesq()
print(psq)
# def abrir_navegador():
#     nave.get("https://fvj-diploma.educat.net.br/processos/3005/assinatura") #entrar no site EDUCAT
#     t.sleep(tesp2)
#     p.hotkey('win','up')
#     nave.find_element(By.XPATH,'/html/body/div/div/div/main/div/form/div[1]/div/input').send_keys("Admin") #user
#     t.sleep(tesp2)
#     nave.find_element(By.XPATH,'//*[@id="rcc-confirm-button"]').click() #ACEITAR COOKIES    
#     t.sleep(tesp2)
#     nave.find_element(By.ID,'password').send_keys("Educat@2022") # senha
#     t.sleep(tesp2)
#     nave.find_element(By.XPATH,'//*[@id="root"]/div/div/main/div/form/button').click() #entrar
#     t.sleep(tesp5)
#     # nave.find_element(By.XPATH,'//*[@id="root"]/div/div/div[2]/div[2]/div/div[2]/div/div[3]/div/div[1]/div[2]').click()
#     # t.sleep(tesp5)
#     #fazer a pesquisa
#     nave.find_element(By.XPATH,'/html/body/div/div/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[2]/input').send_keys(psq)#variável da pesquisa
# abrir_navegador()