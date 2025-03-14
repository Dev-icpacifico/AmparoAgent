from Amparo2.memory.chat_state import ChatState  # ✅ Importar ChatState desde el nuevo archivo
from langgraph.graph import StateGraph
from Amparo2.utils.intent_cassifier import classify_intent
from Amparo2.agents.sueldo_agent import handle_sueldo_query
from Amparo2.agents.reglamento_agent import handle_reglamento_query
from Amparo2.agents.beneficios_agent import handle_beneficios_query
from Amparo2.agents.documentos_agent import handle_documentos_query
from Amparo2.memory.session_manager import session_manager


# Agente Amparo (Router) con gestión de sesiones
def amparo_router(session_id, user_input):
    """
    Amparo recibe la pregunta del usuario, recupera su sesión y decide a qué agente derivarla.
    """
    state = session_manager.get_session(session_id)
    if state is None:
        state = session_manager.create_session()

    state.add_message(user_input, "")

    # 🔹 Depuración: Imprimir intención detectada
    intent = classify_intent(user_input)
    print(f"📌 [DEBUG] Intención detectada: {intent}")  # 🔹 Imprime la intención para depuración

    # Enrutamiento a los agentes correspondientes
    if intent == "sueldo":
        if "imprimir" in user_input or "descargar" in user_input:
            updated_state = handle_documentos_query(session_id, user_input)
        else:
            updated_state = handle_sueldo_query(session_id, user_input)
    elif intent == "reglamento":
        updated_state = handle_reglamento_query(session_id, user_input)
    elif intent == "beneficios":
        updated_state = handle_beneficios_query(session_id, user_input)
    elif intent == "documentos":
        updated_state = handle_documentos_query(session_id, user_input)
    else:
        respuesta = "Lo siento, pero no puedo ayudarte con esa consulta."
        updated_state = state
        updated_state.add_message(user_input, respuesta)

    session_manager.update_session(session_id, updated_state)
    return updated_state

# Construcción del grafo de flujo conversacional con LangGraph
def create_amparo_graph():
    graph = StateGraph(str)

    graph.add_node("start", lambda session_id: session_id)
    graph.add_node("amparo_router", amparo_router)

    graph.set_entry_point("start")
    graph.add_edge("start", "amparo_router")

    return graph.compile()
