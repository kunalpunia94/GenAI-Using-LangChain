from langchain_community.document_loaders import DirectoryLoader,PyPDFLoader

loader = DirectoryLoader(
    path='books',
    glob='*.pdf',
    loader_cls=PyPDFLoader
)

# docs = loader.load()

# print(len(docs))

# print(docs[0].page_content)
# print(docs[0].metadata)

# here it takes more time to load all the pdfs
# so we will use the concept of Load vs Lazy load

# 1st we are seeing Load
# for document in docs:
#     print(document.metadata)

# now using lazy (each data coming to memory at a time printing and removing it)
docs = loader.lazy_load()
for document in docs:
    print(document.metadata)
