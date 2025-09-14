#  HERE WE HAVE USED THE PARSER

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm_model = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm_model)

# 1st prompt ->detailed report
template1 = PromptTemplate(
    template = "Write a detailed report on {topic}",
    input_variables = ['topic']
)

# 2nd prompot ->summary
template2 = PromptTemplate(
    template = "Write a 5 line summary on the following text. /n {text}",
    input_variables = ['text']
)

# created a parser
parser = StrOutputParser()

# create a chain to work with parser(below used parser only gets the text)
# if we are not using the strparser then we need to make two chain extract result from the model and use in another chain
# but with the help of parser it is so easy parser automatically gets the result from the model and pass it to next step
chain = template1 | model | parser | template2 | model | parser

result = chain.invoke({'topic':'Black Hole'})

print(result)