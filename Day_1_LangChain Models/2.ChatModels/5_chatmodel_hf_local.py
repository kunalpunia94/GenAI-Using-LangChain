# OPEN SOURCE

#here we will import hugginfpipeline
from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

# using this files will not be stored in c drive where we want it will go
import os
os.environ['HF_HOME']='D:/huggingface_cache'
llm_model = HuggingFacePipeline.from_model_id(
    model_id='HuggingFaceH4/zephyr-7b-beta',
    task='text-generation',
    pipeline_kwargs=dict(
        temperature = 0.5,
        max_completion_tokens=100
    )
)

model = ChatHuggingFace(llm = llm_model)

result = model.invoke("what is the capital of India")

print(result.content)