import openai
import os
from Amparo2.utils.vector_store import query_chroma

from dotenv import find_dotenv, load_dotenv

dotenv_path = find_dotenv()  # Encuentra la ruta del archivo .env
load_dotenv(dotenv_path)  # Carga las variables de entorno desde el archivo .env
# Asegurar que la API Key está configurada
openai.api_key = os.getenv("OPENAI_API_KEY")


def ask_pdf_agent(question, collection_name="pdf_collection"):
    """
    Realiza una consulta al PDF usando ChromaDB y OpenAI GPT.
    """
    # Recuperar fragmentos relevantes desde ChromaDB
    relevant_texts = query_chroma(question, collection_name, top_k=3)

    if not relevant_texts:
        return "Lo siento, no encontré información relevante en el documento."

    # Construir el prompt para OpenAI
    context = "\n\n".join(relevant_texts)
    prompt = f"Usa la siguiente información del documento para responder la pregunta:\n\n{context}\n\nPregunta: {question}\nRespuesta:"

    # 🔹 Nueva API de OpenAI
    client = openai.OpenAI()
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Eres un asistente experto en responder preguntas basadas en documentos."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=300
    )

    return response.choices[0].message.content.strip()
