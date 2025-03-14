from Amparo2.memory.session_manager import session_manager
from googlesearch import search  # ✅ Ahora usamos googlesearch-python para buscar en la web

def handle_beneficios_query(session_id, user_input):
    """
    Busca información en Internet sobre beneficios y mantiene la sesión.
    """
    # Obtener la sesión actual o crear una nueva si no existe
    state = session_manager.get_session(session_id)
    if state is None:
        state = session_manager.create_session()

    # Construir la consulta de búsqueda
    query = f"{user_input} beneficios laborales en Chile Caja Los Andes Cámara Chilena de la Construcción"

    try:
        # Hacer una búsqueda en Google y obtener los primeros 3 resultados
        search_results = list(search(query, num_results=3))
        respuesta = "Encontré información relevante sobre tu consulta:\n\n" + "\n".join(search_results)
    except Exception as e:
        respuesta = "No pude obtener información en este momento. Intenta más tarde."

    # Agregar la respuesta al historial de la sesión
    state.add_message(user_input, respuesta)

    # 📌 Asegurar que se devuelve el `state` actualizado
    session_manager.update_session(session_id, state)
    return state
