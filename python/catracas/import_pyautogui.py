import pyautogui
import time
from alertafinalizado import alerta_finalizado
from alertainicio import alerta_inicio
# variaveis
timeesp1 = 0.9
timeesp2 = 1.9
timeesp3 = 3
timeesp4 = 300
timeesp5 = 20

def automacao():
    
    #abrir windows
    pyautogui.press('win')
    time.sleep(timeesp2)
    #pesquisar na barra
    pyautogui.write("conexao de area de trabalho remot")
    time.sleep(timeesp1)
    #logar 
    pyautogui.press('enter')
    time.sleep(timeesp2)
    #colocar senha 
    pyautogui.white(" ")
    time.sleep(timeesp2)
    #entrar no servidor
    pyautogui.press('enter')
    time.sleep(timeesp1)
    
    
    time.sleep(timeesp2)
    alerta_inicio()
    time.sleep(5)
    
    
    #abrir programa barra
    pyautogui.click(329,879)
    time.sleep(timeesp2)
    #fechar programa
    pyautogui.click(1570, 9)
    time.sleep(timeesp2)
    #começo
    pyautogui.doubleClick(73, 791)
    time.sleep(timeesp3)
    # inner join
    pyautogui.click(130, 29)
    time.sleep(timeesp1)
    pyautogui.click(174, 54)
    time.sleep(timeesp2)
    # conexão
    pyautogui.click(903, 211)
    time.sleep(timeesp1)
    pyautogui.click(896, 256)
    # tipo de leitor
    pyautogui.click(1078, 214)
    time.sleep(timeesp2)
    pyautogui.click(1046, 297)
    # tipo de equipamento
    pyautogui.click(907, 258)
    time.sleep(timeesp1)
    pyautogui.click(865, 332)
    time.sleep(timeesp1)
    # teclado
    pyautogui.click(520, 315)
    time.sleep(timeesp1)
    # catraca direta
    pyautogui.click(933, 306)
    time.sleep(timeesp1)
    # incluir na lista
    pyautogui.click(572, 385)
    time.sleep(timeesp1)
    # passo 2
    # mudar catraca
    pyautogui.click(598, 210) 
    time.sleep(timeesp1)
    # biometria
    pyautogui.click(660, 284)
    time.sleep(timeesp1)
    pyautogui.click(675, 333)
    time.sleep(timeesp1)
    # incluir na lista
    pyautogui.click(572, 385)
    time.sleep(timeesp1)
    # iniciar
    pyautogui.click(1079, 751)
    time.sleep(timeesp2)
    # innerbio
    pyautogui.click(208, 35)
    time.sleep(timeesp2)
    #innerbio de baixo
    pyautogui.click(222, 60)
    time.sleep(timeesp3)
    #
    # usar talvez while
    # numero  inner --LOOP 4 vezes

    for n in range(0,4):
        # configuracoes bio
        pyautogui.click(853, 362)
        time.sleep(timeesp2)
        # manutenção dig
        pyautogui.click(527, 232)
        time.sleep(timeesp2)
        # atualizar
        pyautogui.click(1131, 283)
        time.sleep(timeesp5)
        # enviar digitais
        pyautogui.click(847, 629)
        time.sleep(timeesp4)
        # configuracoes bio
        pyautogui.click(444, 226)
        time.sleep(timeesp1)
        #
    # fechar inner bio
    pyautogui.click(1191, 207)
    time.sleep(timeesp1)
    # parar
    pyautogui.click(1002, 749)
    time.sleep(timeesp1)

    # part 3 remover lista --loop 4 vezes
    for r in range(0,4):
        pyautogui.click(523, 447)
        time.sleep(timeesp1)
        # remover da lista
        pyautogui.click(656, 386)
        time.sleep(timeesp2)
        # click em ok na notificação que aparece as vezes
        pyautogui.click(969, 510)
        time.sleep(timeesp2)

    # iniciar programa
    pyautogui.click(1079, 751)
    time.sleep(timeesp2)
    
    #
    pyautogui.hotkey('win', 'd')
    
    # enviar email
    alerta_finalizado()
    pyautogui.alert("Acabou a verificação")
automacao()
import pyautogui
import time
from alertafinalizado import alerta_finalizado
from alertainicio import alerta_inicio
# variaveis
timeesp1 = 0.9
timeesp2 = 1.9
timeesp3 = 3
timeesp4 = 300
timeesp5 = 20

def automacao():
    
    pyautogui.press('win')
    
    time.sleep(timeesp2)
    alerta_inicio()
    time.sleep(5)
    
    
    #abrir programa barra
    pyautogui.click(329,879)
    time.sleep(timeesp2)
    #fechar programa
    pyautogui.click(1570, 9)
    time.sleep(timeesp2)
    #começo
    pyautogui.doubleClick(73, 791)
    time.sleep(timeesp3)
    # inner join
    pyautogui.click(130, 29)
    time.sleep(timeesp1)
    pyautogui.click(174, 54)
    time.sleep(timeesp2)
    # conexão
    pyautogui.click(903, 211)
    time.sleep(timeesp1)
    pyautogui.click(896, 256)
    # tipo de leitor
    pyautogui.click(1078, 214)
    time.sleep(timeesp2)
    pyautogui.click(1046, 297)
    # tipo de equipamento
    pyautogui.click(907, 258)
    time.sleep(timeesp1)
    pyautogui.click(865, 332)
    time.sleep(timeesp1)
    # teclado
    pyautogui.click(520, 315)
    time.sleep(timeesp1)
    # catraca direta
    pyautogui.click(933, 306)
    time.sleep(timeesp1)
    # incluir na lista
    pyautogui.click(572, 385)
    time.sleep(timeesp1)
    # passo 2
    # mudar catraca
    pyautogui.click(598, 210) 
    time.sleep(timeesp1)
    # biometria
    pyautogui.click(660, 284)
    time.sleep(timeesp1)
    pyautogui.click(675, 333)
    time.sleep(timeesp1)
    # incluir na lista
    pyautogui.click(572, 385)
    time.sleep(timeesp1)
    # iniciar
    pyautogui.click(1079, 751)
    time.sleep(timeesp2)
    # innerbio
    pyautogui.click(208, 35)
    time.sleep(timeesp2)
    #innerbio de baixo
    pyautogui.click(222, 60)
    time.sleep(timeesp3)
    #
    # usar talvez while
    # numero  inner --LOOP 4 vezes

    for n in range(0,4):
        # configuracoes bio
        pyautogui.click(853, 362)
        time.sleep(timeesp2)
        # manutenção dig
        pyautogui.click(527, 232)
        time.sleep(timeesp2)
        # atualizar
        pyautogui.click(1131, 283)
        time.sleep(timeesp5)
        # enviar digitais
        pyautogui.click(847, 629)
        time.sleep(timeesp4)
        # configuracoes bio
        pyautogui.click(444, 226)
        time.sleep(timeesp1)
        #
    # fechar inner bio
    pyautogui.click(1191, 207)
    time.sleep(timeesp1)
    # parar
    pyautogui.click(1002, 749)
    time.sleep(timeesp1)

    # part 3 remover lista --loop 4 vezes
    for r in range(0,4):
        pyautogui.click(523, 447)
        time.sleep(timeesp1)
        # remover da lista
        pyautogui.click(656, 386)
        time.sleep(timeesp2)
        # click em ok na notificação que aparece as vezes
        pyautogui.click(969, 510)
        time.sleep(timeesp2)

    # iniciar programa
    pyautogui.click(1079, 751)
    time.sleep(timeesp2)
    
    #
    pyautogui.hotkey('win', 'd')
    
    # enviar email
    alerta_finalizado()
    pyautogui.alert("Acabou a verificação")
automacao()
import pyautogui
import time
from alertafinalizado import alerta_finalizado
from alertainicio import alerta_inicio
# variaveis
timeesp1 = 0.9
timeesp2 = 1.9
timeesp3 = 3
timeesp4 = 300
timeesp5 = 20

def automacao():
    
    pyautogui.press('win')
    
    time.sleep(timeesp2)
    alerta_inicio()
    time.sleep(5)
    
    
    #abrir programa barra
    pyautogui.click(329,879)
    time.sleep(timeesp2)
    #fechar programa
    pyautogui.click(1570, 9)
    time.sleep(timeesp2)
    #começo
    pyautogui.doubleClick(73, 791)
    time.sleep(timeesp3)
    # inner join
    pyautogui.click(130, 29)
    time.sleep(timeesp1)
    pyautogui.click(174, 54)
    time.sleep(timeesp2)
    # conexão
    pyautogui.click(903, 211)
    time.sleep(timeesp1)
    pyautogui.click(896, 256)
    # tipo de leitor
    pyautogui.click(1078, 214)
    time.sleep(timeesp2)
    pyautogui.click(1046, 297)
    # tipo de equipamento
    pyautogui.click(907, 258)
    time.sleep(timeesp1)
    pyautogui.click(865, 332)
    time.sleep(timeesp1)
    # teclado
    pyautogui.click(520, 315)
    time.sleep(timeesp1)
    # catraca direta
    pyautogui.click(933, 306)
    time.sleep(timeesp1)
    # incluir na lista
    pyautogui.click(572, 385)
    time.sleep(timeesp1)
    # passo 2
    # mudar catraca
    pyautogui.click(598, 210) 
    time.sleep(timeesp1)
    # biometria
    pyautogui.click(660, 284)
    time.sleep(timeesp1)
    pyautogui.click(675, 333)
    time.sleep(timeesp1)
    # incluir na lista
    pyautogui.click(572, 385)
    time.sleep(timeesp1)
    # iniciar
    pyautogui.click(1079, 751)
    time.sleep(timeesp2)
    # innerbio
    pyautogui.click(208, 35)
    time.sleep(timeesp2)
    #innerbio de baixo
    pyautogui.click(222, 60)
    time.sleep(timeesp3)
    #
    # usar talvez while
    # numero  inner --LOOP 4 vezes

    for n in range(0,4):
        # configuracoes bio
        pyautogui.click(853, 362)
        time.sleep(timeesp2)
        # manutenção dig
        pyautogui.click(527, 232)
        time.sleep(timeesp2)
        # atualizar
        pyautogui.click(1131, 283)
        time.sleep(timeesp5)
        # enviar digitais
        pyautogui.click(847, 629)
        time.sleep(timeesp4)
        # configuracoes bio
        pyautogui.click(444, 226)
        time.sleep(timeesp1)
        #
    # fechar inner bio
    pyautogui.click(1191, 207)
    time.sleep(timeesp1)
    # parar
    pyautogui.click(1002, 749)
    time.sleep(timeesp1)

    # part 3 remover lista --loop 4 vezes
    for r in range(0,4):
        pyautogui.click(523, 447)
        time.sleep(timeesp1)
        # remover da lista
        pyautogui.click(656, 386)
        time.sleep(timeesp2)
        # click em ok na notificação que aparece as vezes
        pyautogui.click(969, 510)
        time.sleep(timeesp2)

    # iniciar programa
    pyautogui.click(1079, 751)
    time.sleep(timeesp2)
    
    #
    pyautogui.hotkey('win', 'd')
    
    # enviar email
    alerta_finalizado()
    pyautogui.alert("Acabou a verificação")
automacao()
import pyautogui
import time
from alertafinalizado import alerta_finalizado
from alertainicio import alerta_inicio
# variaveis
timeesp1 = 0.9
timeesp2 = 1.9
timeesp3 = 3
timeesp4 = 300
timeesp5 = 20

def automacao():
    
    pyautogui.press('win')
    
    time.sleep(timeesp2)
    alerta_inicio()
    time.sleep(5)
    
    
    #abrir programa barra
    pyautogui.click(329,879)
    time.sleep(timeesp2)
    #fechar programa
    pyautogui.click(1570, 9)
    time.sleep(timeesp2)
    #começo
    pyautogui.doubleClick(73, 791)
    time.sleep(timeesp3)
    # inner join
    pyautogui.click(130, 29)
    time.sleep(timeesp1)
    pyautogui.click(174, 54)
    time.sleep(timeesp2)
    # conexão
    pyautogui.click(903, 211)
    time.sleep(timeesp1)
    pyautogui.click(896, 256)
    # tipo de leitor
    pyautogui.click(1078, 214)
    time.sleep(timeesp2)
    pyautogui.click(1046, 297)
    # tipo de equipamento
    pyautogui.click(907, 258)
    time.sleep(timeesp1)
    pyautogui.click(865, 332)
    time.sleep(timeesp1)
    # teclado
    pyautogui.click(520, 315)
    time.sleep(timeesp1)
    # catraca direta
    pyautogui.click(933, 306)
    time.sleep(timeesp1)
    # incluir na lista
    pyautogui.click(572, 385)
    time.sleep(timeesp1)
    # passo 2
    # mudar catraca
    pyautogui.click(598, 210) 
    time.sleep(timeesp1)
    # biometria
    pyautogui.click(660, 284)
    time.sleep(timeesp1)
    pyautogui.click(675, 333)
    time.sleep(timeesp1)
    # incluir na lista
    pyautogui.click(572, 385)
    time.sleep(timeesp1)
    # iniciar
    pyautogui.click(1079, 751)
    time.sleep(timeesp2)
    # innerbio
    pyautogui.click(208, 35)
    time.sleep(timeesp2)
    #innerbio de baixo
    pyautogui.click(222, 60)
    time.sleep(timeesp3)
    #
    # usar talvez while
    # numero  inner --LOOP 4 vezes

    for n in range(0,4):
        # configuracoes bio
        pyautogui.click(853, 362)
        time.sleep(timeesp2)
        # manutenção dig
        pyautogui.click(527, 232)
        time.sleep(timeesp2)
        # atualizar
        pyautogui.click(1131, 283)
        time.sleep(timeesp5)
        # enviar digitais
        pyautogui.click(847, 629)
        time.sleep(timeesp4)
        # configuracoes bio
        pyautogui.click(444, 226)
        time.sleep(timeesp1)
        #
    # fechar inner bio
    pyautogui.click(1191, 207)
    time.sleep(timeesp1)
    # parar
    pyautogui.click(1002, 749)
    time.sleep(timeesp1)

    # part 3 remover lista --loop 4 vezes
    for r in range(0,4):
        pyautogui.click(523, 447)
        time.sleep(timeesp1)
        # remover da lista
        pyautogui.click(656, 386)
        time.sleep(timeesp2)
        # click em ok na notificação que aparece as vezes
        pyautogui.click(969, 510)
        time.sleep(timeesp2)

    # iniciar programa
    pyautogui.click(1079, 751)
    time.sleep(timeesp2)
    
    #
    pyautogui.hotkey('win', 'd')
    
    # enviar email
    alerta_finalizado()
    pyautogui.alert("Acabou a verificação")
automacao()