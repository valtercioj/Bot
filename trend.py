import webbrowser
def trend():
    pg = str(input('o que deseja perquisar: '))
    trend = ('https://trends.google.com.br/trends/explore?q=') # busca no youtube
    pesq = (trend + pg)
    webbrowser.open(pesq)