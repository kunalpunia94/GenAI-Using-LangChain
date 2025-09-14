#CLOSED SOURCE

#here we are import chatopenai
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

# model = ChatOpenAI(model='gpt-3.5-turbo')
#we can add some parameter into this like temperature->how creative response you need in your output #read about values for diff answers
# max_completion_tokens->how many tokens/words you need in the output
model = ChatOpenAI(model='gpt-3.5-turbo',temperature=0.5,max_completion_tokens=10)

result = model.invoke("What is the capital of India?")

# This is will print content and may other info also 
#and also we get many lines in the output
print(result)

# if we just want to print our content
print(result.content)