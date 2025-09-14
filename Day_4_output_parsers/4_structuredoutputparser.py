from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema

load_dotenv()

llm_model = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm_model)

# first need to make schema which guides the LLM that what type of ouput it wants
schema = [
    ResponseSchema(name = 'fact_1', description='Fact 1 about the topic'),
    ResponseSchema(name = 'fact_2', description='Fact 2 about the topic'),
    ResponseSchema(name = 'fact_3', description='Fact 3 about the topic'),
]

# create a pars.
parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template = 'Give 3 facts about the {topic} \n {format_instruction}',
    input_variables=['topic'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

# prompt = template.invoke({'topic':'black hole'})

# result = model.invoke(prompt)

# final_result = parser.parse(result.content)

# do this using chain 
chain = template | model | parser
final_result = chain.invoke({'topic':'black hole'})

print(final_result)

# Ḍisadvantage->no data validation