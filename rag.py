from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

# Load knowledge
loader = TextLoader("knowledge.txt")
documents = loader.load()

# Split text into chunks
text_splitter = CharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=50
)

docs = text_splitter.split_documents(documents)

# Embeddings
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Create vector DB
vectorstore = FAISS.from_documents(docs, embeddings)

retriever = vectorstore.as_retriever()


def retrieve_context(query):

    results = retriever.invoke(query)

    if results:
        return results[0].page_content

    return "No relevant information found."