from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("dl-curriculum.pdf")

docs = loader.load()

# print(docs)

# print(len(docs))

print(docs[0].page_content)
print(docs[0].metadata)

# https://www.youtube.com/watch?v=bL92ALSZ2Cg&list=PLKnIA16_RmvaTbihpo4MtzVm4XOQa0ER0&index=12
# read about all the pdf loaders