import os
import sys
import subprocess as s
plat = sys.platform
if plat == 'win32':
	try:
		from googlesearch import search
	except:
		os.system('pip install google')
elif plat == 'linux':
	try:
		from googlesearch import search
	except:
		os.system('pip3 install google')
def site(): # funcao para abrir sites
    from googlesearch import search
    
    plataforma = sys.platform # ve o SO que sera rodado 
    if plataforma == 'win32': # para windows

        opcao = str(input('Qual site deseja abrir? = ')) # escolha do site

##################################################################################
    
        p = str(input('onde deseja buscar, se for link direto so aperte enter: '))
        for url in search(opcao+p, stop=1):
	        os.startfile(url)
######################################################################################       
        print()
        print('+=+'*20)
        print('              comando executado. Até a proxima.')
        print('+=+'*20)

    elif plataforma == 'linux': # para lixus
        opcao = str(input('Qual site deseja abrir? = ')) # entrada do site
##################################################################################
      
        p = str(input('onde deseja buscar, se for link direto so aperte enter: '))
        for url in search(opcao+p, stop=1):
	        s.Popen(['xdg-open',url])
######################################################################################        
        print()
        print('+=+'*20)
        print('              comando executado. Até a proxima.')
        print('+=+'*20)
