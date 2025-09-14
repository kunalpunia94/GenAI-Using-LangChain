# i am using huffingface bcoz it is free can do same using opanai also

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
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

# user ek topic lenge uske upar 5 facts generate karke denge

prompt = PromptTemplate(
    template="Generate 5 interesting facts about {topic}",
    input_variables=['topic']
)

chain = prompt | model | parser

result = chain.invoke({'topic':'cricket'})

print(result)

chain.get_graph().print_ascii() 