from Amparo2.memory.session_manager import session_manager
from Amparo2.utils.reglamento_loader import buscar_en_reglamento


def handle_reglamento_query(session_id, user_input):
    """
    Responde preguntas sobre el reglamento interno de la empresa basándose en un PDF previamente cargado.
    """
    # Obtener la sesión actual o crear una nueva si no existe
    state = session_manager.get_session(session_id)
    if state is None:
        state = session_manager.create_session()

    # Buscar en el reglamento los fragmentos más relevantes
    fragmentos = buscar_en_reglamento(user_input)

    if fragmentos:
        respuesta = f"Según el reglamento interno:\n\n{fragmentos[0]}"
    else:
        respuesta = "No encontré información en el reglamento sobre este tema."

    # Agregar la respuesta al historial de la sesión
    state.add_message(user_input, respuesta)

    # Actualizar la sesión con el nuevo historial
    session_manager.update_session(session_id, state)

    return state
