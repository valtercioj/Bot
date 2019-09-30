import webbrowser
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