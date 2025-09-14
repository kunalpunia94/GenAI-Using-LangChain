#CLOSED SOURCE

# claude ai by anthrophic company
#so import that library
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

model = ChatAnthropic(model="claude-opus-4-20250514")

result = model.invoke("What is the capital of India")

print(result)