import os
import sys
import subprocess as s

####################################################################

plat = sys.platform
if plat == 'win32': # VERIFICACAO DOS PACOTES NO WINDOWS
	try:
		from googlesearch import search
		import youtube_dl
	except:
		os.system('pip install google')
		os.system('pip install youtube-dl')
		import youtube_dl
elif plat == 'linux': # VERIFICACAO DOS PACOTES NO LINUX
	try:
		from googlesearch import search
		import youtube_dl
	except:
		os.system('pip3 install google')
		os.system('pip3 install youtube-dl')
		from googlesearch import search		
		import youtube_dl
####################################################################
def site(): # funcao para abrir sites
	

	plataforma = sys.platform # ve o SO que sera rodado 
	if plataforma == 'win32': # para windows
		opcao = str(input('Qual site deseja abrir? = ')) # escolha do site
		parametro = str(input('onde deseja buscar, se for link direto so aperte enter: ')) # Variavel p vai verificar o parametro de busca. ex: google,youtube,wikipedia e outros
		
		if parametro == 'youtube': # opcao para abrir ou baixar do youtube
			for url in search(opcao+parametro, stop=1):
				operacao = str(input('deseja abrir ou baixar? ')) # vai fazer a busca a partir do que foi solicitado
			if operacao == 'abrir':
				os.startfile(url)
			elif op == 'baixar': # vai baixar a partir do modulo youtube-dl
				operacao = str(input('audio ou video? '))
				if operacao == 'audio':
					os.system('youtube-dl -f 140 '+url)
				elif operacao == 'video':
					os.system('youtube-dl '+url)
		elif parametro != 'youtube': # vai abrir o que foi solicitado
			for url in search(opcao+parametro, stop=1):
				os.startfile(url) # opcao para abrir um link no windows
	######################################################################################       
			print()
			print('+=+'*20)
			print('              comando executado. Até a proxima.')
			print('+=+'*20)
			
	elif plataforma == 'linux': # para lixus
		opcao = str(input('Qual site deseja abrir? = ')) # escolha do site
		parametro = str(input('onde deseja buscar, se for link direto so aperte enter: ')) # Variavel parametro vai verificar o parametro de busca. ex: google,youtube,wikipedia e outros
		
		if parametro == 'youtube':# opcao para abrir ou baixar do youtube

			for url in search(opcao+parametro, stop=1):
				operacao = str(input('deseja abrir ou baixar? '))
			if operacao == 'abrir':
				s.Popen(['xdg-open',url])
			elif operacao == 'baixar': # vai baixar a partir do modulo youtube-dl
				operacao = str(input('audio ou video? '))
				if operacao == 'audio':
					os.system('youtube-dl -f 140 '+url)
				elif operacao == 'video':
					os.system('youtube-dl '+url)

		elif parametro != 'youtube': # vai abrir o que foi solicitado
			for url in search(opcao+parametro, stop=1):
				s.Popen(['xdg-open',url]) # opcao para abrir um link no linux
	######################################################################################       
			print()
			print('+=+'*20)
			print('              comando executado. Até a proxima.')
			print('+=+'*20)
