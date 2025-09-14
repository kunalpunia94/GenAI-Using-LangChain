from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm_model = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm_model)

# Load the document
loader = TextLoader("doc.txt")
documents = loader.load()

# split the text into smaller chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size = 500, chunk_overlap = 50)
docs = text_splitter.split_documents(documents)

# convert text into embeddings and store in the FAISS
vectorstore = FAISS.from_documents(docs, HuggingFaceEmbeddings())

# create a retriver for the semantic search
retriever = vectorstore.as_retriever()

# manually retrieve relevant documents
query = "What are the key takeways from the document?"
retrieved_docs = retriever.get_relevant_documents(query)

# combine retrieved text into a single prompt
retrieved_text = "\n".join([doc.page_content for doc in retrieved_docs])

# manually pass retrieved text to llm
prompt = f"Based on the following text, answer the question: {query}\n\n{retrieved_text}"
answer = model.invoke(prompt)

# print the answer
print(answer)
