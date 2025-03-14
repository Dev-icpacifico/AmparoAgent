from langchain_community.document_loaders import PyPDFLoader
import os
from dotenv import load_dotenv, find_dotenv
from langchain_chroma import Chroma  # ✅ Nueva importación para evitar deprecación
from langchain_community.document_loaders import PyPDFLoader
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings

# 📌 Cargar variables de entorno desde .env
dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

# 📌 Asegurar que la API Key está configurada correctamente
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("❌ ERROR: No se encontró la API Key de OpenAI. Configura OPENAI_API_KEY en el archivo .env")


# 📌 Especificar la ruta donde ChromaDB guardará la información
CHROMA_DB_PATH = "./chroma_db/"

def inicializar_vector_store():
    """
    Inicializa la base de datos vectorial con persistencia habilitada.
    """
    return Chroma(
        persist_directory=CHROMA_DB_PATH,  # 📌 Asegura que los datos se guarden en disco
        embedding_function=OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY"))
    )

def cargar_reglamento(pdf_path):
    """
    Extrae texto de un PDF de reglamento interno y lo indexa en ChromaDB.
    """
    loader = PyPDFLoader(pdf_path)
    pages = loader.load()

    texts = [page.page_content for page in pages]  # Obtener texto por página
    vector_store = inicializar_vector_store()  # Inicializar ChromaDB aquí

    # 📌 Verificar cuántos documentos se van a indexar
    if not texts:
        raise ValueError("❌ ERROR: No se pudo extraer texto del PDF. Verifica que el archivo no sea una imagen escaneada.")

    vector_store.add_texts(texts)  # Almacenar en ChromaDB

    print(f"📌 Reglamento indexado correctamente ({len(texts)} páginas procesadas).")


def buscar_en_reglamento(query):
    """
    Busca en la base de datos vectorial el fragmento más relevante para responder la pregunta.
    """
    vector_store = inicializar_vector_store()  # Inicializar ChromaDB antes de buscar

    # 🔹 Buscar con puntuación de similitud
    results = vector_store.similarity_search_with_score(query, k=5)

    # 🔹 Depuración: Imprimir los resultados encontrados
    print(f"📌 [DEBUG] Resultados de búsqueda en ChromaDB para '{query}':")
    for doc, score in results:
        print(f"- {doc.page_content[:200]}... (Score: {score})")

    if not results:
        return ["No encontré información en el reglamento sobre este tema."]

    # 📌 Ajustamos el umbral de similitud para aceptar respuestas con menor puntaje
    umbral_similitud = 0.2  # 🔹 Reducimos de 0.7 a 0.2

    respuestas_relevantes = [doc.page_content for doc, score in results if score >= umbral_similitud]

    # 🔹 Si hay respuestas, devolverlas; si no, dar una respuesta general
    if respuestas_relevantes:
        return respuestas_relevantes
    else:
        return [
            "No encontré información clara en el reglamento, pero aquí tienes algunas secciones relacionadas:\n\n" + "\n\n".join(
                [doc.page_content for doc, _ in results])]
