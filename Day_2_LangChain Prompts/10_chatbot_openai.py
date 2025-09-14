# here we are integrating messages
#what message is sent by whom and solves that problem

from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from dotenv import load_dotenv

load_dotenv()
 
model = ChatOpenAI()

chat_history = [
    SystemMessage(content='You are a helpful assistant')
]

while True:
    user_input = input("you: ")
    chat_history.append(HumanMessage(user_input))
    if user_input == "Exit":
        break
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(result))
    print("AI: ",result.content)

print(chat_history)