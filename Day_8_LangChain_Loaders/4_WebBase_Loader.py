from langchain_community.document_loaders import WebBaseLoader

url = 'https://www.flipkart.com/skechers-d-lux-trekker-hiking-trekking-shoes-men/p/itm1f40ffcc9a1d8?pid=SHOGNATBVUGJ92ZD&lid=LSTSHOGNATBVUGJ92ZDEWPJVV&marketplace=FLIPKART&store=osp&srno=b_1_29&otracker=browse&fm=organic&iid=0150523f-cb0c-4a85-8846-500d73e3d9ed.SHOGNATBVUGJ92ZD.SEARCH&ppt=sp&ppn=productListView&ssid=hjmrnmsdow0000001749910826142'

loader = WebBaseLoader(url)

docs = loader.load()

# print(len(docs))

# print(docs[0].page_content)

# now lets ask some questions from this
from langchain_community.document_loaders import TextLoader
from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

llm_model = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm_model)
parser = StrOutputParser()

Prompt = PromptTemplate(
    template="Answer the following question \n {question} from the following text - \n {text}",
    input_variables=['question','text']
)

chain = Prompt | model | parser

result = chain.invoke({'question':'What is the product that we are talking about?','text':docs[0].page_content})

print(result)