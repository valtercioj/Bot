from random import randint
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os
def conv():
	##########################################################################################
	# ChatterBot
	bot = ChatBot("Test") #read_only=True) # <- read to stop training the bot
	

	trainer = ListTrainer(bot) # training
	for arq in os.listdir('arq'):
		chats = open('arq/' + arq, 'r').readlines()

		trainer.train(chats) # training with the chats
	####################################################################################


	piada = ['Por que o pinheiro não se perde na floresta? R: Porque ele tem uma pinha', 'o que o pagodeiro foi fazer na igreja? R: Foi cantar pá God.','Voce conhece a piada do pônei? R: Pô nei eu kkkkkkkkkk','Qual a semelhança entre um pastor e um martelo?  R: Ambos pregam.','Por que o peixe come muito?  R: Porque anda sempre com água  na boca.']

	n = int(randint(0,4)) # escolha de numeros aleatorios
	while True:
		quest = input('You: ') 
		response = bot.get_response(quest) # bot response
		print('Bot: ', response)
		if quest == 'conte uma piada':
		        print('bot: ',piada[n])
		elif quest == 'tchau':break
		

