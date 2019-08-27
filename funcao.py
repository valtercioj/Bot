import webbrowser
from random import randint
import os
import sys
import subprocess as s
import wikipedia

def google(): # funcao para pesquisa no google ou youtube
        while True:
                
                pg = str(input('o que deseja perquisar: ')) # entrada da pesquisa
                busca = str(input('onde deseja pesquisar: ')) # onde sera pesquisado
                if busca == 'youtube':
                        youtube = ('https://www.youtube.com/results?search_query=') # busca no youtube
                        pesq = (youtube + pg)
                        webbrowser.open(pesq) # abrindo a escolha
        
                if busca == 'google':
                        google = ('https://www.google.com/search?q=') # busca no google
                        pesq = (google + pg)
                        webbrowser.open(pesq) # abrindo a escolha
                break
        print('''
        +=++=++=++=++=++=++=++=++=++=++=++=++=++=++=++=++=++=++=++=+
              comando executado. Até a proxima.
        +=++=++=++=++=++=++=++=++=++=++=++=++=++=++=++=++=++=++=++=+
        ''')
def conv(): # funcao do chat
##################################################################################################################################
# chat
        pergunta = ['ola jarvis', 'tudo bem?', 'estou bem','qual linguagem de programação voce foi criado?','quem criou voce?','jarvis']
        pergunta1 = ['ola','bom dia','boa tarde','boa noite','como se chama?','estou indo embora','ja estou indo embora']
        resp = ['ola senhor','estou bem e voce?','muito bom saber','fui criado todo em python','meu criador foi Valtercio Junior','ola senhor o que deseja?']
        resp1 = ['ola senhor','bom dia','boa tarde','boa noite','me chamo Jarvis','está bem senhor. Até a proxima']
        piada = ['Por que o pinheiro não se perde na floresta? R: Porque ele tem uma pinha', 'o que o pagodeiro foi fazer na igreja? R: Foi cantar pá God.','Voce conhece a piada do pônei? R: Pô nei eu kkkkkkkkkk','Qual a semelhança entre um pastor e um martelo?  R: Ambos pregam.','Por que o peixe come muito?  R: Porque anda sempre com água  na boca.']
##################################################################################################################################
        n = int(randint(0,4)) # escolha de numeros aleatorios
        perg = ''
        while not perg == 'tchau': # laço que termina quando for digitado tchau
                if perg == pergunta[0]:
                    print('Bot: ',resp[0])
                perg = str(input('Voce: '))
                if perg == pergunta[1]:
                    print('Bot: ',resp[1])
                if perg == pergunta[2]:
                    print('Bot: ',resp[2])
                if perg == pergunta[3]:
                    print('Bot: ',resp[3])
                if perg == pergunta[4]:
                    print('Bot: ',resp[4])
                if perg == pergunta[5]:
                    print('Bot: ',resp[5])
                if perg == pergunta1[0]:
                    print('Bot: ',resp1[0])
                if perg == pergunta1[1]:
                    print('Bot: ',resp1[1])
                if perg == pergunta1[2]:
                    print('Bot: ',resp1[2])
                if perg == pergunta1[3]:
                    print('Bot: ',resp1[3])
                if perg == pergunta1[4]:
                    print('Bot: ',resp1[4])
                if perg == pergunta1[5]:
                    print('Bot: ',resp1[5])
                if perg == pergunta1[6]:
                    print('Bot: ',resp1[5])
                if perg == 'conte uma piada':
                    print('bot: ',piada[n])
        print('Bot: tchau') 
def site(): # funcao para abrir sites
    plataforma = sys.platform # ve o SO que sera rodado 
    if plataforma == 'win32': # para windows

        opcao = str(input('Qual site deseja abrir? = ')) # escolha do site

##################################################################################
# links de sites
        if opcao == 'moodle imd':
            os.startfile("https://moodle.imd.ufrn.br/login/index.php")
        if opcao == 'suap':
            os.startfile("https://suap.ifrn.edu.br")
        if opcao == 'sigaa':
            os.startfile("https://sigaa.ufrn.br/sigaa")
        if opcao == 'github':
            os.startfile("https://github.com/valtercioj")
        if opcao == 'facebook':
            os.startfile("https://pt-br.facebook.com")
        if opcao == 'udemy':
            os.startfile("https://www.udemy.com/")
        if opcao == 'youtube':
            os.startfile("https://www.youtube.com/")
        if opcao == 'google':
            os.startfile("https://www.google.com/")
        if opcao == 'materiais imd':
            os.startfile("https://materiais.imd.ufrn.br")
######################################################################################       
        print()
        print('+=+'*20)
        print('              comando executado. Até a proxima.')
        print('+=+'*20)

    elif plataforma == 'linux': # para lixus
        opcao = str(input('Qual site deseja abrir? = ')) # entrada do site
##################################################################################
# links de sites
        if opcao == 'moodle imd':
            s.Popen(["xdg-open","https://moodle.imd.ufrn.br/login/index.php"])
        if opcao == 'suap':
            s.Popen(["xdg-open","https://suap.ifrn.edu.br"])
        if opcao == 'sigaa':
            s.Popen(["xdg-open","https://sigaa.ufrn.br/sigaa"])
        if opcao == 'github':
            s.Popen(["xdg-open","https://github.com/valtercioj"])
        if opcao == 'facebook':
            s.Popen(["xdg-open","https://pt-br.facebook.com"])
        if opcao == 'udemy':
            s.Popen(["xdg-open","https://www.udemy.com/"])
        if opcao == 'youtube':
            s.Popen(["xdg-open","https://www.youtube.com/"])
        if opcao == 'google':
            s.Popen(["xdg-open","https://www.google.com/"])        
        if opcao == 'materiais imd':
            s.Popen(["xdg-open","https://materiais.imd.ufrn.br"])
######################################################################################        
        print()
        print('+=+'*20)
        print('              comando executado. Até a proxima.')
        print('+=+'*20)

def wiki(): # funcao para busca na wikipedia
	lin = str(input('Deseja em portugues ou ingles? (pt/en) ')) # linguagem que sera usada	
	if lin == 'pt':	# linguagem em portugues
		wikipedia.set_lang('pt')
	if lin == 'en': # linguagem em ingles
		wikipedia.set_lang('en')
	print() # espaco entre as linhas
	
	busca = str(input('O que o senhor deseja buscar: ')) # o que sera pesquisado

	print() # espaco entre as linhas

	txt = str(input('quer que eu salve em um arquivo ou mostre na tela? (salvar/mostrar): ')) # para salvar ou mostrar na tela
	print() # espaco entre as linhas
	if txt == 'salvar': # para salvar em arquivo
		arq = open('pesquisa.txt', 'w') # abrindo arquivo
		texto = wikipedia.summary(busca) # busca feita

		arq.write(texto) # gravando o arquivo
		arq.close() # fechando o arquivo		
	if txt == 'mostrar': # para imprimir a busca
		print('='*70)		
		print(wikipedia.summary(busca, sentences = 100)) # impressao da busca
		print('='*70)
			
	print('''

	+=++=++=++=++=++=++=++=++=++=++=++=++=++=++=++=++=++=++=++=+
              comando executado. Até a proxima.
        +=++=++=++=++=++=++=++=++=++=++=++=++=++=++=++=++=++=++=++=+
	''')






























