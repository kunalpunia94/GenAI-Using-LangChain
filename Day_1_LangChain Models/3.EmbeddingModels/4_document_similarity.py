# we are building the simple applicaiion -> document similarity document application
# we will use openai
# we will find the cosine between the input and output embeddings for all and the closest one we will take

from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-large',dimensions=300)

documents = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
]

query = "tell me about virat kohli" 

doc_embedding = embedding.embed_documents(documents)
query_embedding = embedding.embed_query(query)

# find the cosine similarity of query with all the documents
# print(cosine_similarity([query_embedding],[doc_embedding])[0])
scores =cosine_similarity([query_embedding],[doc_embedding])[0]

# using this index with similarity scores printed and sorted based on the similarity score
# and they are sorted in the ascending order and we are extracting the last one using [-1]
# print(sort(list(enumerate(scores)),key=lambda x:x[1])[-1]) 
index,score = sorted(list(enumerate(scores)),key=lambda x:x[1])[-1]

print(query)
print(documents[index])
print("Similarity Score is:",score)