from funcao import conv
from funcao import google
from funcao import site
from funcao import wiki
from funcao import trend
print('''
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
     ola Valtercio bem vindo de volta. Estou a sua desposição.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

''')


perg = str(input('Voce: ')) # entrada com o nome jarvis
print()

jarvis = ''

if perg == 'não quero fazer nada': # comando para sair do Bot
    print()# para da espaços entre as linhas
    print('Ok senhor, até a proxima...')

if perg == 'jarvis': # comando para iniciar o Bot
    jarvis = str(input('ola senhor o que deseja? ')) # escolha das funções do Bot.

print() # para da espaços entre as linhas

if jarvis == 'faca uma busca' or jarvis == 'faça uma busca': # Bot faz uma busca no google ou youtube        
	google()
if jarvis == 'abra um site' or jarvis == 'quero abrir um site':  # Bot abrirá um site
        site() # funcao para abrir sites
if jarvis == 'quero conversar': # para conversar com o Bot
        conv() # funcao do chat
if jarvis == 'faca uma busca na wikipedia' or jarvis == 'faça uma busca na wikipedia': # Bot pesquisa na wikipedia
	wiki() # funcao da wikipedia
if jarvis == 'faca uma busca na trend':
	trend()
    
    
