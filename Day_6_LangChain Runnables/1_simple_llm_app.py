from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
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

# define the input
topic = input("Enter the topic: ")

# format the prompt manually
formatted_prompt = prompt.format(topic=topic)

# call the llm
blog_title = model.invoke(formatted_prompt)

# print the prompt
print("Generated Blog title :",blog_title)