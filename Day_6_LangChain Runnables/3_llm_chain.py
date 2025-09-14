# Like in the 1_simple_llm we create the prompt and manually givin
# so one conept of llm_chain comes which do all these automatically
# bcoz this process is done in every llm model so they made a general class wew can use anywhere

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv

load_dotenv()

llm_model = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm_model)

# create a prompt templte
prompt = PromptTemplate(
    template="Suggest a catchy blog title about {topic}",
    input_variables=['topic']
)

# # define the input
# topic = input("Enter the topic: ")

# # format the prompt manually
# formatted_prompt = prompt.format(topic=topic)

# # call the llm
# blog_title = model.invoke(formatted_prompt)

# # print the prompt
# print("Generated Blog title :",blog_title)   

# below done using the LLMChain
# chain = LLMChain(llm = llm_model,prompt = prompt)   this is not used nowadays
chain = prompt | model


# run the chain with a specific topic
topic = input("Enter your topic: ")
output = chain.invoke({'topic':topic})

print("Generated Blog Title: ",output)