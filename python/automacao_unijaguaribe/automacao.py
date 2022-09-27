import pyautogui as p
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
    p.press('win')
    time.sleep(timeesp2)
    #pesquisar na barra
    p.write("remot")
    time.sleep(timeesp1)
    #logar 
    p.press('enter')
    time.sleep(timeesp2)
    p.press('enter')
    time.sleep(timeesp2)

    #colocar senha 
    p.write("masterFVJFVJ@%$&")
    time.sleep(timeesp3)
    
    #entrar no servidor
    p.press('enter')
    time.sleep(timeesp3)
    
    #começo do codigo no servidor
    alerta_inicio()
    time.sleep(5)
    #abrir programa barra
    p.click(329,879)
    time.sleep(timeesp2)
    #fechar programa
    p.click(1570, 9)
    time.sleep(timeesp2)
    #começo
    p.doubleClick(73, 791)
    time.sleep(timeesp3)
    # inner join
    p.click(130, 29)
    time.sleep(timeesp1)
    p.click(174, 54)
    time.sleep(timeesp2)
    # conexão
    p.click(903, 211)
    time.sleep(timeesp1)
    p.click(896, 256)
    # tipo de leitor
    p.click(1078, 214)
    time.sleep(timeesp2)
    p.click(1046, 297)
    # tipo de equipamento
    p.click(907, 258)
    time.sleep(timeesp1)
    p.click(865, 332)
    time.sleep(timeesp1)
    # teclado
    p.click(520, 315)
    time.sleep(timeesp1)
    # catraca direta
    p.click(933, 306)
    time.sleep(timeesp1)
    # incluir na lista
    p.click(572, 385)
    time.sleep(timeesp1)
    # passo 2
    # mudar catraca
    p.click(598, 210) 
    time.sleep(timeesp1)
    # biometria
    p.click(660, 284)
    time.sleep(timeesp1)
    p.click(675, 333)
    time.sleep(timeesp1)
    # incluir na lista
    p.click(572, 385)
    time.sleep(timeesp1)
    # iniciar
    p.click(1079, 751)
    time.sleep(timeesp2)
    # innerbio
    p.click(208, 35)
    time.sleep(timeesp2)
    #innerbio de baixo
    p.click(222, 60)
    time.sleep(timeesp3)
    #
    # usar talvez while
    # numero  inner --LOOP 4 vezes

    for n in range(0,4):
        # configuracoes bio
        p.click(853, 362)
        time.sleep(timeesp2)
        # manutenção dig
        p.click(527, 232)
        time.sleep(timeesp2)
        # atualizar
        p.click(1131, 283)
        time.sleep(timeesp5)
        # enviar digitais
        p.click(847, 629)
        time.sleep(timeesp4)
        # configuracoes bio
        p.click(444, 226)
        time.sleep(timeesp1)
        #
    # fechar inner bio
    p.click(1191, 207)
    time.sleep(timeesp1)
    # parar
    p.click(1002, 749)
    time.sleep(timeesp1)

    # part 3 remover lista --loop 4 vezes
    for r in range(0,4):
        p.click(523, 447)
        time.sleep(timeesp1)
        # remover da lista
        p.click(656, 386)
        time.sleep(timeesp2)
        # click em ok na notificação que aparece as vezes
        p.click(969, 510)
        time.sleep(timeesp2)

    # iniciar programa
    p.click(1079, 751)
    time.sleep(timeesp2)
    
    #
    p.hotkey('win', 'd')
    time.sleep(timeesp2)
    
    # enviar email
    alerta_finalizado()
    
    #fechar servidor
    p.click(1042, 12)
    p.alert("Acabou a verificação")
automacao()