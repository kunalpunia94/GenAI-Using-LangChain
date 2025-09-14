from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()
 
model = ChatOpenAI()

while True:
    user_input = input("you: ")
    if user_input == "Exit":
        break
    result = model.invoke(user_input)
    print("AI: ",result.content)

#but there is a problem that it forgets do not contain memory like
# you : which is bigger 2 or 0
# AI : 2
# you : multiply bigger number by 10
# AI : let's say bigger number is x
#      multipy x by 10m we get : 10x  ->>>>>this is the problem here