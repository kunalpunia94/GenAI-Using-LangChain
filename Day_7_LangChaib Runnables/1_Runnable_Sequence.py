from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence

load_dotenv()

llm_model = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)

# create a model instance of hugging face
model = ChatHuggingFace(llm=llm_model)

# create a prompt
prompt1 = PromptTemplate(
    template = "Write a joke about {topic}",
    input_variables = ["topic"]
)

# create a parser
parser = StrOutputParser()

# create a prompot2
prompt2 = PromptTemplate(
    template = "Explain the following joke -{text}",
    input_variables = ["text"]
)

# create a chain with the help of RunnableSequence and just pass what all you need to connect
chain = RunnableSequence(prompt1,model,parser,prompt2,model,parser)

# now invoke the chain and give topic and print the it
print(chain.invoke({'topic':"AI"}))