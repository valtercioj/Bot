import wikipedia

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

		arq.write(texto+'\r\n') # gravando o arquivo
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