#but there is a problem that it forgets do not contain memory like
# you : which is bigger 2 or 0
# AI : 2
# you : multiply bigger number by 10
# AI : let's say bigger number is x
#      multipy x by 10m we get : 10x  ->>>>>this is the problem here

#THIS PROBLEM SOLVED BY MAINTAINING THE HISTORY

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()
 
model = ChatOpenAI()

chat_history = []

while True:
    user_input = input("you: ")
    chat_history.append(user_input)
    if user_input == "Exit":
        break
    result = model.invoke(chat_history)
    chat_history.append(result)
    print("AI: ",result.content)

print(chat_history)


#now the problem is again that when we get chat history it is not given like which chat is sent by whom so when chat becomes big this also 
# leads to a problem so we shoudl maintain like this chat sent by AI or you and then stote in the chat_history

