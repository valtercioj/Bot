import os
import sys
import subprocess as s

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