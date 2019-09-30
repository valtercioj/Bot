from random import randint
def conv(): # funcao do chat
##################################################################################################################################
# chat
        pergunta = ['ola jarvis', 'tudo bem?', 'estou bem','qual linguagem de programação voce foi criado?','quem criou voce?','jarvis']
        pergunta1 = ['ola','bom dia','boa tarde','boa noite','como se chama?','estou indo embora','ja estou indo embora']
        resp = ['ola senhor','estou bem e voce?','muito bom saber','fui criado todo em python','meu criador foi Valtercio Junior','ola senhor o que deseja?']
        resp1 = ['ola senhor','bom dia','boa tarde','boa noite','me chamo Jarvis','está bem senhor. Até a proxima']
       	piada = ['Por que o pinheiro não se perde na floresta? R: Porque ele tem uma pinha', 'o que o pagodeiro foi fazer na igreja? R: Foi cantar pá God.','Voce conhece a piada do pônei? R: Pô nei eu kkkkkkkkkk','Qual a semelhança entre um pastor e um martelo?  R: Ambos pregam.','Por que o peixe come muito?  R: Porque anda sempre com água  na boca.']
        comp = ['ola','ola senhor','hello','iae boe','oi']
##################################################################################################################################
        n = int(randint(0,4)) # escolha de numeros aleatorios
        perg = ''
        while not perg == 'tchau': # laço que termina quando for digitado tchau
                if perg == pergunta[0]:
                    print(n)
                    print('bot: ',comp[n])
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