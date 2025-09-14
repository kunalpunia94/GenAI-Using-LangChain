# from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.messages import SystemMessage, AIMessage, HumanMessage

# chat_template = ChatPromptTemplate([
#     SystemMessage(content="You are a helpful {domain} expert"),
#     HumanMessage(content="Tell me about {topic}")
# ])

# prompt = chat_template.invoke({'domain':'cricket','topic':'no ball'})

# print(prompt)

# PROBELM IN LANGCHAIN HOW TO DEFINE LITTLE WIERDLY(does not give value to that)
# (venv) PS D:\Data Science\GenAI Using LangChain\Day_2_LangChain Prompts> python 12_chat_prompt_templates.py
# messages=[SystemMessage(content='You are a helpful {domain} expert', additional_kwargs={}, response_metadata={}), HumanMessage(content='Tell me about {topic}', additional_kwargs={}, response_metadata={})]

#below problem solved
#Dynammic messages
from langchain_core.prompts import ChatPromptTemplate

# chat_template = ChatPromptTemplate.from_messages([
chat_template = ChatPromptTemplate([
    ('system','you are a helpful expert {domain}'),
    ('human','tell me {topic}')
])

prompt = chat_template.invoke({'domain':'cricket','topic':'no ball'})

print(prompt)

#now working fine