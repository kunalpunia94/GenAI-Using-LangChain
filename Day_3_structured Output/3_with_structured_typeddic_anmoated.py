# here annoated one like sometimes model won't understand so we need to mention personally 

# from langchain_openai import ChatOpenAI
# from dotenv import load_dotenv
# from typing import TypedDict,Annotated

# load_dotenv()

# model = ChatOpenAI()

# #creating the typeddic schema
# class Review(TypedDict):
#     # Here we defined what model should do with the text
#     summary : Annotated[str,'A brief summary of review']
#     sentiment : Annotated[str,'Return sentiment of the review either negative or positive']


# structured_model = model.with_structured_output(Review)

# result = structured_model.invoke("""To handle sentiment-based conversations effectively, it's important to maintain a structured chat history using HumanMessage and AIMessage. This allows you to track the flow of dialogue clearly and extract sentiments from specific messages using their .content. With this structure, you can easily analyze emotional tone, detect shifts in mood, and build more responsive, sentiment-aware chatbots.
# """)

# print(result)
# print(result['summary'])
# print(result['sentiment'])


# now we will work on the big data and fetch many things
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict,Annotated,Optional,Literal

load_dotenv()

model = ChatOpenAI()

#creating the typeddic schema
class Review(TypedDict):
    key_themes : Annotated[list[str],"Write down all the the key themes discussed in the review"] #list of string
    summary : Annotated[str,'A brief summary of review']
    # sentiment : Annotated[str,'Return sentiment of the review either negative or positive']
    sentiment : Annotated[Literal["Pos", "Neg"],'Return sentiment of the review either negative or positive']
    # this is optional
    pros : Annotated[Optional[list[str]],"Write down all the pros inside the list"]
    cons : Annotated[Optional[list[str]],"Write down all the cons inside the list"]
    name : Annotated[Optional[str],"Write the name of the reviewer"]

structured_model = model.with_structured_output(Review)

result = structured_model.invoke("""I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it’s an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I’m gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.

The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often. What really blew me away is the 200MP camera—the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.

However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung’s One UI still comes with bloatware—why do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard pill to swallow.

Pros:
Insanely powerful processor (great for gaming and productivity)
Stunning 200MP camera with incredible zoom capabilities
Long battery life with fast charging
S-Pen support is unique and useful
                                 
Review by Nitish Singh
""")

print(result)
print(result['summary'])
print(result['sentiment']) 


# in with_structured_output there is no validation 
# next we will study pydantic with the validation