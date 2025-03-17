from Amparo2.memory.session_manager import session_manager
from Amparo2.utils.intent_cassifier import classify_intent
from Amparo2.agents.sueldo_agent import handle_sueldo_query
from Amparo2.agents.reglamento_agent import handle_reglamento_query
from Amparo2.agents.beneficios_agent import handle_beneficios_query
from Amparo2.agents.documentos_agent import handle_documentos_query
from openai import OpenAI
import os

# Inicializar cliente de OpenAI con GPT-4
openai_api_key = os.getenv("OPENAI_API_KEY")
openai_client = OpenAI(api_key=openai_api_key)


def amparo_router(session_id, user_input):
    """
    Amparo recibe la pregunta del usuario, recupera su sesión y decide a qué agente derivarla.
    Ahora también usa GPT-4 para mejorar la respuesta final.
    """
    state = session_manager.get_session(session_id)
    if state is None:
        state = session_manager.create_session()

    state.add_message(user_input, "")

    # 🔹 Detectar la intención de la pregunta
    intent = classify_intent(user_input)
    print(f"📌 [DEBUG] Intención detectada: {intent}")

    # Enrutamiento de la consulta a los agentes especializados
    if intent == "sueldo":
        response_state = handle_sueldo_query(session_id, user_input)
    elif intent == "reglamento":
        response_state = handle_reglamento_query(session_id, user_input)
    elif intent == "beneficios":
        response_state = handle_beneficios_query(session_id, user_input)
    elif intent == "documentos":
        response_state = handle_documentos_query(session_id, user_input)
    else:
        response_state = state
        response_state.add_message(user_input, "Lo siento, pero no puedo ayudarte con esa consulta.")

    # Obtener la respuesta generada por el agente
    respuesta = response_state.history[-1]["amparo"] if response_state.history else "No tengo información sobre esto."

    # 🔥 Mejorar la respuesta con GPT-4
    gpt_response = mejorar_respuesta_con_gpt4(user_input, respuesta)

    # Agregar la respuesta mejorada al historial
    response_state.add_message(user_input, gpt_response)
    session_manager.update_session(session_id, response_state)

    return response_state


def mejorar_respuesta_con_gpt4(user_input, respuesta_base):
    """
    Usa GPT-4 para mejorar la respuesta basada en la información de ChromaDB o de los agentes.
    Ahora se incluye un prompt de personalidad para Amparo.
    """
    try:
        prompt_sistema = """
        Eres Amparo, una asistente virtual de Recursos Humanos para trabajadores de la construcción.
        Tu objetivo es responder de manera clara, amigable y profesional.
        Siempre debes ser respetuosa, empática y transmitir confianza.
        Si no tienes una respuesta exacta, ofrece orientación sobre dónde encontrar la información.
        No inventes respuestas, y si el usuario pregunta algo fuera de tu alcance, explica qué temas puedes responder.
        """

        prompt_usuario = f"""
        Usuario: "{user_input}".
        Respuesta base encontrada: "{respuesta_base}".
        Reformula la respuesta con un tono claro, profesional y amigable.
        """

        gpt_reply = openai_client.chat.completions.create(
            model="gpt-4-turbo",
            messages=[
                {"role": "system", "content": prompt_sistema},
                {"role": "user", "content": prompt_usuario}
            ],
            temperature=0.7,
            max_tokens=300
        )

        return gpt_reply.choices[0].message.content.strip()

    except Exception as e:
        print(f"❌ Error al generar respuesta con GPT-4: {e}")
        return respuesta_base  # Si falla, usa la respuesta original
