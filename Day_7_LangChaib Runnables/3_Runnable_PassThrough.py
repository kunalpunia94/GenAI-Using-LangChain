from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence,RunnableParallel,RunnablePassthrough

load_dotenv()

llm_model = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm_model)
parser = StrOutputParser()

# # First let's see how RunnablePassThrough works demo
# passthrough = RunnablePassthrough()
# print(passthrough.invoke(2)) #->gives same input


# let's see where it is useful as written in the notebook
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

joke_gen_chain = RunnableSequence(prompt1,model,parser)
paraller_chian = RunnableParallel({
    'joke':RunnablePassthrough(),
    'explanation':RunnableSequence(prompt2,model,parser)
})
final_chain = RunnableSequence(joke_gen_chain,paraller_chian)

result = final_chain.invoke({'topic':'cricket'})
print(result)