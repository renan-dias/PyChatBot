#Create a chatbot with python using chatterbot library

import random
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

bot = ChatBot('Bot')
bot.set_trainer(ListTrainer)

for _file in os.listdir('C:/Users/hp/Desktop/Python/chatterbot-corpus-master/chatterbot_corpus/data/english/'):
    lines = open('C:/Users/hp/Desktop/Python/chatterbot-corpus-master/chatterbot_corpus/data/english/' + _file, 'r').readlines()
    bot.train(lines)

while True:
    message = input('You:')
    if message.strip() != 'Bye':
        reply = bot.get_response(message)
        print('ChatBot :',reply)
    if message.strip() == 'Bye':
        print('ChatBot : Bye')
        break