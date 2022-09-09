import re
import random
import time

print("Hello! My name is Chatbot. I'm here to talk to you.")

human_pattern = re.compile(r'(.)')

while True:
    message = input(">>> ")
    if message == "goodbye":
        print("Goodbye! Have a nice day.")
        break
    elif message == "":
        print("Please say something to me.")
    else:
        time.sleep(random.random())
        print(human_pattern.sub(r'\1\1', message))