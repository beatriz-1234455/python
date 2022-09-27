from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

#   Installando o driver mais atual do navegador de forma automática
service = Service(ChromeDriverManager().install())

#   Criando a chamada de execução do navegador
navegador = webdriver.Chrome(service=service)

#   Chamando a página da UNIJAGUARIBE de forma automática
navegador.get('https://unijaguaribe.edu.br/')

#   Selecionando elementos da página via xpath
navegador.find_element('xpath', '//*[@id="menu-1-19bee0f5"]/li[6]/a')
