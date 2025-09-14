# Let's see how it works first
# from langchain.schema.runnable import RunnableLambda

# def word_counter(text):
#     return len(text.split())

# runnable_word_counter = RunnableLambda(word_counter)
# print(runnable_word_counter.invoke("Hi! there how are you?"))

# Now let's make application prints joke and number of words as written in the notebook
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence,RunnableParallel,RunnablePassthrough,RunnableLambda

load_dotenv()

llm_model = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm_model)
parser = StrOutputParser()


prompt = PromptTemplate(
    template = "Write a joke about {topic}",
    input_variables = ["topic"]
)

def word_counter(text):
    return len(text.split())

joke_gen_chain = RunnableSequence(prompt,model,parser)
parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'word_count': RunnableLambda(word_counter)  #RunnableLambda(lambda x : len(x.split()))
})

final_chain = RunnableSequence(joke_gen_chain,parallel_chain)

result = final_chain.invoke({'topic':'AI'})

# print(result)
final_result = """{} \nword count - {}""".format(result['joke'],result['word_count'])

print(final_result)