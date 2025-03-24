import os
from langchain.chat_models import init_chat_model
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore
from pinecone import Pinecone
from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain import hub
from langchain_core.documents import Document
from typing import List, TypedDict
from langgraph.graph import START, StateGraph

# Configurar claves desde variables de entorno
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
LANGSMITH_API_KEY = os.getenv("LANGSMITH_API_KEY", "")

if not OPENAI_API_KEY or not PINECONE_API_KEY:
    raise EnvironmentError("Debes definir OPENAI_API_KEY y PINECONE_API_KEY en tu entorno.")

os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
os.environ["LANGSMITH_API_KEY"] = LANGSMITH_API_KEY
os.environ["LANGSMITH_TRACING"] = "true"

# Inicializar modelo y embeddings
llm = init_chat_model("gpt-4o-mini", model_provider="openai")
embeddings = OpenAIEmbeddings(model="text-embedding-3-large")

# Conectarse a Pinecone
pc = Pinecone(api_key=PINECONE_API_KEY)
index_name = "bmw-m235i-index"
index = pc.Index(index_name)
vector_store = PineconeVectorStore(embedding=embeddings, index=index)

# Cargar y dividir contenido
url = "https://extremamotor.es/prueba-bmw-m235i-coupe-326-cv-explosivos/"
loader = WebBaseLoader(
    web_paths=[url],
    bs_kwargs={"parse_only": "p"}
)
docs = loader.load()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
all_splits = text_splitter.split_documents(docs)

# Indexar en Pinecone
_ = vector_store.add_documents(documents=all_splits)

# Prompt base y definición de flujo
prompt = hub.pull("rlm/rag-prompt")

class State(TypedDict):
    question: str
    context: List[Document]
    answer: str

def retrieve(state: State):
    retrieved_docs = vector_store.similarity_search(state["question"])
    return {"context": retrieved_docs}

def generate(state: State):
    docs_content = "\n\n".join(doc.page_content for doc in state["context"])
    messages = prompt.invoke({"question": state["question"], "context": docs_content})
    response = llm.invoke(messages)
    return {"answer": response.content}

# Crear y ejecutar grafo
graph_builder = StateGraph(State).add_sequence([retrieve, generate])
graph_builder.add_edge(START, "retrieve")
graph = graph_builder.compile()

if __name__ == "__main__":
    print("\n Bienvenido al RAG del BMW M235i")
    while True:
        question = input("\n Escribe tu pregunta (o 'salir'): ")
        if question.lower() in ["salir", "exit"]:
            print("Hasta luego!")
            break
        result = graph.invoke({"question": question})
        print("\n Respuesta:", result["answer"])