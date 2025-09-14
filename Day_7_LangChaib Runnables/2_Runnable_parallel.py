from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence,RunnableParallel

load_dotenv()

llm_model = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm_model)
parser = StrOutputParser()

# same we will make here how written in notebook one will generate tweet and another one will generate the linkedin post
prompt1 = PromptTemplate(
    template = "Generate a tweet about {topic}",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template = "Generate a linkedIn post about {topic}",
    input_variables=['topic']
)

# we initialize RunnableParallel in the form of dictionary
paraller_chain = RunnableParallel({
    'tweet':RunnableSequence(prompt1,model,parser),
    'linkedIn':RunnableSequence(prompt2,model,parser),
})

# this AI will be given to both the chains
result = paraller_chain.invoke({'topic':'AI'})

print(result)

# or
print(result['tweet'])
print(result['linkedIN'])