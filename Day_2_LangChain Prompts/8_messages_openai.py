from langchain_core.messages import HumanMessage,AIMessage,SystemMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

# STATIC MESSAGES
# humanmessage->sent by user
# aimessage->sent by the ai
# systemmessage-> you sent in starting like you are a helpful assiment etc -> in the starting of conversation

messages = [
    SystemMessage(content='You are a helpful assisten'),
    HumanMessage(content='Tell me about langchain')
]

result = model.invoke(messages)

messages.append(AIMessage(content=result.content))

print(messages)

#now we will import the messages/use in our chatbot