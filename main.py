import os
import subprocess
import sys
from gtts import gTTS
from sys import platform
from subprocess import call
from random import choice
from time import sleep

def exit():
    animation = ['[\033[1;33mi\033[m] Saindo em 3 segundos...','[\033[1;33mi\033[m] Saindo em 2 segundos...','[\033[1;33mi\033[m] Saindo em 1 segundos...','[\033[1;33mi\033[m] Saindo em 0 segundos...']
    for i in range(len(animation)):
        sleep(1)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()

def spin():
    animation = ['[▒▒▒▒▒▒▒▒▒▒]','[█▒▒▒▒▒▒▒▒▒]','[██▒▒▒▒▒▒▒▒]','[███▒▒▒▒▒▒▒]','[████▒▒▒▒▒▒]','[█████▒▒▒▒▒]','[██████▒▒▒▒]','[███████▒▒▒]','[████████▒▒]','[█████████▒]','[██████████]']
    for i in range(len(animation)):
        sleep(0.1)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()

def restart():
    python = sys.executable
    os.execl(python, python, *sys.argv)

def clear():
    os.system('clear')
    
vermelho = '\033[1;31m'
verde = '\033[1;32m'
a = '\033[m[\033[1;33mi\033[m]'
    
def gtts():
    clear()

    text = input('{} Digite o texto: '.format(a))
    ling = input('{} Digite o idioma,exemplo: pt,en,fr,etc: '.format(a))

    mytext = '{}'.format(text)

    language = '{}'.format(ling)

    myobj = gTTS(text=mytext, lang=language, slow=False)

    myobj.save("gtts.mp3")

    os.system("mpg123 gtts.mp3")

clear()

print('\033[1;33mAviso | \033[mEssa ferramenta está em versão ALPHA!\n')
print('{} Verificando atualizações...'.format(a))
update = subprocess.check_output('git pull', shell=True)
if 'Already up to date' not in update.decode():
    print('{} Atualizado com sucesso,iniciando...'.format(a))
    sleep(1)
    subprocess.run('clear')
    restart()
else:
    print('{} Nenhuma atualização disponível.'.format(a))
    sleep(1)
  
nome = input('{} Me diga como quer ser chamado: '.format(a))

senha = 'ByOneLost'

while True:
    tema = input('''{} Qual tema você quer usar na ferramenta?
    
[\033[1;33m1\033[m] - Vermelho
[\033[1;33m2\033[m] - Verde
    
>>> '''.format(a))
    if tema == '1':
        print('\nTema definido para {}vermelho!\n\033[m'.format(vermelho))
        print('\n')
        spin()
        print('\n')
        b = '\033[1;31m'
        c = '\033[m'
        sleep(1)
        break
    elif tema == '2':
        print('\nTema definido para {}verde!\n\033[m'.format(verde))
        print('\n')
        spin()
        print('\n')
        b = '\033[1;32m'
        c = '\033[m'
        sleep(1)
        break
    else:
        print('\nOpção inválida\n')

welcome = ['Bem vindo','Use com moderação','Use com consiência','Você é foda','Você é o mais brabo','Siga o lost no instagram']
kkk = choice(welcome)
erro = '\n{} Ops! Parece que você escolheu uma opção não definida\n'.format(a)
while True:
    clear()
    menu = input('''

{1} _          _____           _
| | ___  __|_   _|{0}__   ___ {1}| |
| |/ _ \/ __|| |{0}/ _ \ / _ \{1}| |
| | (_) \__ \| |{0} (_) | (_) {1}| |
|_|\___/|___/|_|{0}\___/ \___/{1}|_|
                          
Author: {0}@lostkkj_{1}
Version: {0}BETA{1}


{2} {0}{3}!{1}


{0}[{1}1{0}]{1} - Spam
{0}[{1}2{0}]{1} - Ataque DDoS
{0}[{1}3{0}]{1} - Puxar dados
{0}[{1}4{0}]{1} - Ferramentas hacker
{0}[{1}5{0}]{1} - Mùsicas
{0}[{1}6{0}]{1} - Chat Online no Termux
{0}[{1}7{0}]{1} - Jogos
{0}[{1}8{0}]{1} - GTTS - Texto para áudio

{0}[{1}01{0}]{1} - Chat do lost
{0}[{1}02{0}]{1} - Canal do lost
{0}[{1}03{0}]{1} - IG do lost
{0}[{1}04{0}]{1} - Reportar/Pedidos

{0}[{1}0{0}]{1} - Sair


{0}>>>{1} '''.format(b,c,kkk,nome))

    if menu == '1':
        clear()
        spam = input('''

{0} ____  ____   _    __  __
/ ___||  _ \ / \  |  \/  |
\___ \| |_) / _ \ | |\/| |
 ___) |  __/ ___ \| |  | |
|____/|_| /_/   \_\_|  |_|
{1}
{0}[{1}1{0}]{1} - Spam SMS
{0}[{1}2{0}]{1} - Voltar

{0}>>>{1} '''.format(b,c))

        if spam == '1':
            print('\n')
            spin()
            print('\n')
            os.system('node tools/spam.js')
            break
        elif spam == '2':
            print(menu)
    elif menu == '2':
        ddos = input('''
{0}
 ____  ____       ____
|  _ \|  _ \  ___/ ___|         
| | | | | | |/ _ \___ \
| |_| | |_| | (_) |__) |
|____/|____/ \___/____/{1}

{0}[{1}1{0}]{1} - Iniciar ataque DDoS
{0}[{1}2{0}]{1} - Voltar

{0}>>>{1}'''.format(b,c))

        if ddos == '1':
            ip = input('\n\n\033[mDigite o IP da vítima: \033[1;31m\n\n')
            os.system('python tools/hammer.py -s {} -p80 -t135')
            break
        else:
            print(menu)
            
    elif menu == '3':
        clear()
        painel = input('\n{} A senha do painel é: VirtualInsanity\nPress enter\n'.format(a))
        os.system('sh tools/painel.sh')
        
    elif menu == '6':
        clear()
        chat = input('\nCOMO ENTRAR NO {0}CHAT{1}\n\n{0}[{1}1{0}]{1} - /connect chat.freenode.net\n{0}[{1}2{0}]{1} - /nick (seu nick)\n{0}[{1}3{0}]{1} - /join #OneLost\n\nDivirta-se no chat! (Press enter) '.format(b,c))
        os.system('pkg install irssi && irssi')

    elif menu == '8':
         gtts()

    elif menu == '16':
        virus = input('Qual pasta você quer mover o virus? ')
        os.system('rm tools/.Whatsapp.apk /sdcard/{}'.format(virus))
        sleep(4)

    elif menu == '0':
        print('')
        exit()
        print('\n')
        break
    
    elif menu == '01':
        os.system('termux-open-url https://chat.whatsapp.com/IeYRyhvwkA61ljgjwK0wH4')
    elif menu == '02':
        os.system('termux-open-url https://youtube.com/channel/UCGI7eobXY2zsLib_3Clq_DQ')
    elif menu == '03':
        os.system('termux-open-url https://www.instagram.com/invites/contact/?i=6ufp6gxb2azy&utm_content=jt3qoto')
    elif menu == '04':
        os.system('termux-open-url https://api.whatsapp.com/send?phone=5511994677319&text=Eaekkkk')
    else:
        print(erro)
        sleep(2)
        print(menu)
