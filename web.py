import os
import sys
import subprocess as s
plat = sys.platform
if plat == 'win32':
	try:
		from googlesearch import search
		import youtube_dl
	except:
		os.system('pip install google')
		os.system('pip install youtube-dl')
		import youtube_dl
elif plat == 'linux':
	try:
		from googlesearch import search
		import youtube_dl
	except:
		os.system('pip3 install google')
		os.system('pip3 install youtube-dl')
		import youtube_dl
def site(): # funcao para abrir sites
	from googlesearch import search

	plataforma = sys.platform # ve o SO que sera rodado 
	if plataforma == 'win32': # para windows
		opcao = str(input('Qual site deseja abrir? = ')) # escolha do site
		p = str(input('onde deseja buscar, se for link direto so aperte enter: '))
		if p == 'youtube':
			for url in search(opcao+p, stop=1):
				op = str(input('deseja abrir ou baixar? '))
			if op == 'abrir':
				os.startfile(url)
			elif op == 'baixar':
				op = str(input('audio ou video? '))
				if op == 'audio':
					os.system('youtube-dl -f 140 '+url)
				elif op == 'video':
					os.system('youtube-dl '+url)
		else:
			for url in search(opcao+p, stop=1):
				os.startfile(url)
	######################################################################################       
			print()
			print('+=+'*20)
			print('              comando executado. Até a proxima.')
			print('+=+'*20)
			
	elif plataforma == 'linux': # para lixus
		opcao = str(input('Qual site deseja abrir? = ')) # escolha do site
		p = str(input('onde deseja buscar, se for link direto so aperte enter: '))
		if p == 'youtube':
			for url in search(opcao+p, stop=1):
				op = str(input('deseja abrir ou baixar? '))
			if op == 'abrir':
				s.Popen(['xdg-open',url])
			elif op == 'baixar':
				op = str(input('audio ou video? '))
				if op == 'audio':
					os.system('youtube-dl -f 140 '+url)
				elif op == 'video':
					os.system('youtube-dl '+url)
		elif p != 'youtube':
			for url in search(opcao+p, stop=1):
				s.Popen(['xdg-open',url])
	######################################################################################       
			print()
			print('+=+'*20)
			print('              comando executado. Até a proxima.')
			print('+=+'*20)
