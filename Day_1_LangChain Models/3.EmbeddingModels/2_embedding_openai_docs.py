#CLOSED SOURCE

from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

emdedding = OpenAIEmbeddings(model='text-embedding-3-large',dimensions=32)

docs = [
    "Delhi is the capital of India",
    "Kolkata is the capital of west bengal",
    "Paris is the capital of france"
]

# here call embed_documents->will do on all documents
result = emdedding.embed_documents("Dellhi is the capital of india")

# prints the contextual meaning of the sentence
print(str(result))