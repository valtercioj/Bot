from random import randint
def conv(): # funcao do chat
##################################################################################################################################
# chat
        pergunta = ['ola jarvis', 'tudo bem?', 'estou bem','qual linguagem de programação voce foi criado?','quem criou voce?','jarvis']
        
        resp = ['ola senhor','estou bem e voce?','muito bom saber','fui criado todo em python','meu criador foi Valtercio Junior','ola senhor o que deseja?']
        pergunta1 = ['ola','bom dia','boa tarde','boa noite','como se chama?','estou indo embora','ja estou indo embora']
        resp1 = ['ola senhor','bom dia','boa tarde','boa noite','me chamo Jarvis','está bem senhor. Até a proxima']
        piada = ['Por que o pinheiro não se perde na floresta? R: Porque ele tem uma pinha', 'o que o pagodeiro foi fazer na igreja? R: Foi cantar pá God.','Voce conhece a piada do pônei? R: Pô nei eu kkkkkkkkkk','Qual a semelhança entre um pastor e um martelo?  R: Ambos pregam.','Por que o peixe come muito?  R: Porque anda sempre com água  na boca.']
        comp = ['ola senhor','hello','iae boe','oi']
##################################################################################################################################
        n = int(randint(0,4)) # escolha de numeros aleatorios
        
        while True: # laço que termina quando for digitado tchau
            perg = str(input('You: '))
            if perg == 'tchau':break

            for i in range(0,len(pergunta)):
                if pergunta[i] == perg:
                    print('Bot: '+resp[i])
              
            for i in range(0,len(pergunta1)):
                if pergunta1[i] == perg:
                    print('Bot: '+resp1[i])
                
            for i in range(0,len(comp)):
                if comp[i] == perg:
                    print('Bot: '+resp[0])
            if perg == 'conte uma piada':
                print('bot: ',piada[n])
        print('Bot: tchau')
