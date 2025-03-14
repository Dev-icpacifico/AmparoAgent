import chromadb
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document


# Inicializar el almacenamiento de ChromaDB
def initialize_chroma():
    client = chromadb.PersistentClient(path="./chroma_db")  # Base de datos persistente
    return client.get_or_create_collection(name="pdf_collection")


# Función para procesar y almacenar fragmentos en ChromaDB
def store_pdf_in_chroma(text, collection_name="pdf_collection"):
    client = chromadb.PersistentClient(path="./chroma_db")
    collection = client.get_or_create_collection(name=collection_name)

    # Dividir el texto en fragmentos
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    docs = text_splitter.split_text(text)

    # Agregar fragmentos a ChromaDB
    for i, chunk in enumerate(docs):
        collection.add(documents=[chunk], ids=[f"doc_{i}"])

    print(f"📌 Se han indexado {len(docs)} fragmentos en ChromaDB.")
    return collection


# Función para hacer una búsqueda semántica en los datos almacenados
def query_chroma(query, collection_name="pdf_collection", top_k=3):
    client = chromadb.PersistentClient(path="./chroma_db")
    collection = client.get_or_create_collection(name=collection_name)

    # Realizar la consulta en la base de datos vectorial
    results = collection.query(query_texts=[query], n_results=top_k)

    return results["documents"][0] if results["documents"] else []