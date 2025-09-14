#CLOSED SOURCE

from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

emdedding = OpenAIEmbeddings(model='text-embedding-3-large',dimensions=32)

result = emdedding.embed_query("Dellhi is the capital of india")

# prints the contextual meaning of the sentence
print(str(result))