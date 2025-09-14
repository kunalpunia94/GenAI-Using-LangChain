#but there is a problem that it forgets do not contain memory like
# you : which is bigger 2 or 0
# AI : 2
# you : multiply bigger number by 10
# AI : let's say bigger number is x
#      multipy x by 10m we get : 10x  ->>>>>this is the problem here------>no context, forgets previous chat, so need to maintain chat history
#      then that history we will send to llm so that it will understand whats going on


###----PROBLEM-----###
# (venv) PS D:\Data Science\GenAI Using LangChain\Day_2_LangChain Prompts> python 5_chatbot_hf.py
# You: which is bigger 10 or 2
# AI:  10 is bigger than 2.
# You: multiply bigger number by 2
# AI:  You can specify the bigger number, and I'll multiply it by 2. What's the number?
# You: don't you remember?
# AI:  I'm a large language model, I don't have personal memories or the ability to recall specific conversations or interactions. Each time you interact with me, it's a new conversation and I don't retain any information from previous chats.

# However, I can try to help you recall something if you provide more context or details about what you're trying to remember. What's on your mind?
# You: Exit
# (venv) PS D:\Data Science\GenAI Using LangChain\Day_2_LangChain Prompts> 


####----THIS PROBLEM SOLVED BY MAINTAINIG THE HISTORY------

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm_model = HuggingFaceEndpoint(
    model='meta-llama/Llama-3.1-8B-Instruct',
    task='text-generation'
)

model = ChatHuggingFace(llm = llm_model)

chat_history = []

while True:
    user_input = input("You: ")
    chat_history.append(user_input)
    if user_input == "Exit":
        break
    result = model.invoke(chat_history)
    chat_history.append(result)
    print("AI: ",result.content)

print(chat_history)




#now the problem is again that when we get chat history it is not given like which chat is sent by whom so when chat becomes big this also 
# leads to a problem so we shoudl maintain like this chat sent by AI or you and then stote in the chat_history

#so now we need to overcome that so instead of list we need to store in dictoniray
# but this problem we get so langchain identified and giving before itself


