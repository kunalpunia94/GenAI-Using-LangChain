#OPEN SOURCE

# using huggingfaceendpoint->when we use hf api so we need this
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm_model = HuggingFaceEndpoint(
    repo_id='HuggingFaceH4/zephyr-7b-beta',
    task='text-generation'
)
model = ChatHuggingFace(llm=llm_model)

result = model.invoke("What is the capital of India?")

print(result.content)