from Amparo2.memory.session_manager import session_manager
from Amparo2.utils.reglamento_loader import buscar_en_reglamento
from openai import OpenAI
import os

# Configurar API de OpenAI
openai_api_key = os.getenv("OPENAI_API_KEY")
openai_client = OpenAI(api_key=openai_api_key)

def handle_reglamento_query(session_id, user_input):
    """
    Responde preguntas sobre el reglamento interno usando ChromaDB y GPT-4 para mejorar la claridad de la respuesta.
    """
    state = session_manager.get_session(session_id)
    if state is None:
        state = session_manager.create_session()

    # 📌 Buscar en ChromaDB la información relevante
    fragmentos = buscar_en_reglamento(user_input)

    if not fragmentos:
        respuesta = "No encontré información en el reglamento sobre este tema. Te recomiendo consultar con Recursos Humanos."
    else:
        # 📌 Enviar el texto extraído a GPT-4 para resumirlo y explicarlo mejor
        respuesta = procesar_respuesta_con_gpt4(user_input, fragmentos)

    # Agregar la respuesta al historial de la sesión
    state.add_message(user_input, respuesta)
    session_manager.update_session(session_id, state)

    return state

def procesar_respuesta_con_gpt4(user_input, fragmentos):
    """
    Usa GPT-4 para resumir y explicar mejor el contenido del reglamento interno.
    """
    try:
        prompt = f"""
        Un trabajador ha preguntado: "{user_input}".
        En el reglamento interno encontramos la siguiente información relevante:

        {fragmentos}

        Por favor, resume y explica esta información de manera clara y fácil de entender para el trabajador.
        No agregues información adicional, solo resume lo relevante.
        """

        gpt_reply = openai_client.chat.completions.create(
            model="gpt-4-turbo",
            messages=[
                {"role": "system", "content": "Eres un asistente de Recursos Humanos que responde preguntas sobre el reglamento interno de una empresa de construcción."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.5,
            max_tokens=300
        )

        return gpt_reply.choices[0].message.content.strip()

    except Exception as e:
        print(f"❌ Error al procesar con GPT-4: {e}")
        return "No encontré información clara en el reglamento. Te recomiendo consultar con Recursos Humanos."
