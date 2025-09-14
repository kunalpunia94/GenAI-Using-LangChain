#CLOSED SOURCE

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.0-flash',max_tokens=1000)

result = model.invoke("Suggest good places to visit in summar vacation")

# print(result)

print(result.content)