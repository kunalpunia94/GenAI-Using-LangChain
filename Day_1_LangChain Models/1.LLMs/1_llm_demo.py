#this lib tells that we are going to work with openai
from langchain_openai import OpenAI
#this laods key from .env file to main file
from dotenv import load_dotenv

#load the functiona and now we can access the varible of api key
load_dotenv()

llm = OpenAI(model='gpt-3.5-turbo-instruct')

#using invoke fun we will communicate and give prompt to model and get output and we store in result
## and we gave only one string as an input and also we will get the string only in the output   
result = llm.invoke("What is the capital of India?")

print(result)

#basically these model are not being used now, mostly all are using the chat models we will see next


