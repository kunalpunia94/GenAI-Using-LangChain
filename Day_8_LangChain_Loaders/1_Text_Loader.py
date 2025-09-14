from langchain_community.document_loaders import TextLoader
from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

llm_model = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm_model)
parser = StrOutputParser()

Prompt = PromptTemplate(
    template="Write a summary for the following poem -\n {poem}",
    input_variables=['poem']
)

loader = TextLoader('cricket.txt',encoding='utf-8')

# inside loader there is a function load simply call it
docs = loader.load()

# print(docs)

# print(type(docs))

# print(len(docs))

# print(docs[0])

# print(type(docs[0]))

# print(docs[0])  #gives both page_content and meta data

print(docs[0].page_content)
print(docs[0].metadata)

chain = Prompt | model | parser
print(chain.invoke({'poem':docs[0].page_content}))