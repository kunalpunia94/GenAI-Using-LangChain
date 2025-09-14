from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict

load_dotenv()

model = ChatOpenAI()

#creating the typeddic schema
class Review(TypedDict):
    summary : str
    sentiment : str

#  Model automatically understands that it need to give summary and sentiment

structured_model = model.with_structured_output(Review)

result = structured_model.invoke("""To handle sentiment-based conversations effectively, it's important to maintain a structured chat history using HumanMessage and AIMessage. This allows you to track the flow of dialogue clearly and extract sentiments from specific messages using their .content. With this structure, you can easily analyze emotional tone, detect shifts in mood, and build more responsive, sentiment-aware chatbots.
""")

print(result)
print(result['summary'])
print(result['sentiment'])