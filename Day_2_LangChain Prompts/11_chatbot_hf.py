# here we are integrating messages
#what message is sent by whom and solves that problem


from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

llm_model = HuggingFaceEndpoint(
    model='meta-llama/Llama-3.1-8B-Instruct',
    task='text-generation'
)

model = ChatHuggingFace(llm = llm_model)

chat_history = [
    SystemMessage('You are helpful assistant')
]

while True:
    user_input = input("You: ")
    chat_history.append(HumanMessage(user_input))
    if user_input == "Exit":
        break
    result = model.invoke(chat_history)
    chat_history.append(result)
    
    print("AI: ",result.content)

print(chat_history)