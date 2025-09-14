from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# create chat history
chat_template = ChatPromptTemplate([
    # system message
    ('system','You are a helpful customer support agent'),
    # here we place our chat history(whatever they speak comes here)
    MessagesPlaceholder(variable_name='chat_history'),
    # human message
    ('human','{query}')
])

# load chat history
chat_history =[]
with open('13_chat_history.txt') as f:
    # appending into the chat history
    chat_history.extend(f.readlines())
print(chat_history)

# create your prompt
prompt = chat_template.invoke({'chat_history':chat_history,'query':'Where is my refund'})

print(prompt)