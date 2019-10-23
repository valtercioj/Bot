import chat
import google
import web
import wikipedia
import trend 


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
	google.google()
if jarvis == 'abra um site' or jarvis == 'quero abrir um site':  # Bot abrirá um site
        web.site() # funcao para abrir sites
if jarvis == 'quero conversar': # para conversar com o Bot
        chat.conv() # funcao do chat
if jarvis == 'faca uma busca na wikipedia' or jarvis == 'faça uma busca na wikipedia': # Bot pesquisa na wikipedia
	wikipedia.wiki() # funcao da wikipedia
if jarvis == 'faca uma busca na trend':
	trend.trend()
    
