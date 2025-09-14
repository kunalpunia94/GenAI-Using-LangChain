from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

llm_model = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm_model)

parser = JsonOutputParser()

template = PromptTemplate(
    template = 'Give me the name, age and city of a fictional person \n {format_instruction}',
    input_variables=[],
    partial_variables={'format_instruction':parser.get_format_instructions()}
    # Give me the name, age and city of a fictional person 
    # Return a JSON object.   ->this is the actual prompt i am sending to llm we got this from output
)

# prompt = template.format()

# # print(prompt)
# result = model.invoke(prompt)

# final_result = parser.parse(result.content)

# instead of above we can use chain
chain = template | model | parser

final_result = chain.invoke({})

print(final_result)
print(type(final_result))

# PROBLEM WITH JSONOUTPUTPARSER -> we can get the json object but can't define the json schema below we won't get in structured way
# template = PromptTemplate(
#     template = 'Give me 5 lines about {topic} \n {format_instruction}',
#     input_variables=['topic'],
#     partial_variables={'format_instruction':parser.get_format_instructions()}
# )