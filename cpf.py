import webbrowser
def cpf():
	b = str(input('digite seu cpf sem pontos e acentos: '))			
	cpf = ('https://tudosobretodos.se/')
	pesq = (cpf + b)
	webbrowser.open(pesq)
