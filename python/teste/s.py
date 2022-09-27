from conf import * 
servico = Service(ChromeDriverManager().install())
nave = webdriver.Chrome(service=servico)


nave.get("https://fvj-diploma.educat.net.br/signin")
t.sleep(4)
#abrir pagina do educat
p.hotkey('win','up')
nave.find_element(By.ID, 'rcc-confirm-button').click()
t.sleep(0.9)
#aceitar cokkies 
nave.find_element(By.ID, 'email').send_keys("admin")
t.sleep(2)
#adcionar email
nave.find_element(By.ID, 'password').send_keys("Educat@2022")
t.sleep(2)
#adcionar senha
p.press('enter')
t.sleep(5)
#apertar enter
for n in range(0,7):
    p.hotkey("ctrl" ,"-")
    t.sleep(0.5)
#minimizar tela
nave.find_element(By.XPATH, '//*[@id="root"]/div/div/div[2]/div[2]/div/div[2]/div/div[4]/div/div[1]/div[2]').click()
t.sleep(3)
#botao curso

nave.find_element(By.XPATH, '//*[@id="root"]/div/div/div[4]/div[2]/div/div[2]/div/div[3]/button').click()
t.sleep(3)
#botao proximo

for n in range(0,3):
    
    nave.find_element(By.XPATH, '//*[@id="root"]/div/div/div[4]/div[2]/div/div[2]/div/div[3]/button[2]').click()
    t.sleep(3)
#botao proximo 

for n in range(0,3):
    nave.find_element(By.XPATH, '//*[@id="root"]/div/div/div[4]/div[2]/div/div[2]/div/div[6]/nav/ul/li[6]').click()
    t.sleep(3)


