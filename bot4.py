#Python code for a chatbot that uses artificial intelligence to learn and be trained:

import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    ['my name is (.*)', ['hi %1']],
    ['(hi|hello|hey|holla)', ['hey there', 'hi there', 'haayyy']],
    ['(.*) in (.*) is fun', ['%1 in %2 is indeed fun']],
    ['(.*)(location|city) ?', 'Tokyo, Japan'],
    ['how is the weather in (.*)', ['the weather in %1 is amazing like always']],
    ['(.*) created you ?', ['I was created by a team of experts!']],
    ['how are you ?', ['I am good, thanks for asking', 'I am fine, thank you']],
    ['(.*) your name ?', ['My name is Chatbot and I am here to help you']],
    ['(quit|bye|exit)', ['Bye take care!', 'See you later!']]
]

def chatbot():
    print("Hi there, I am a chatbot. Please type 'quit' to exit our conversation.\n")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    chatbot()