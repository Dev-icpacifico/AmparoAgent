from Amparo2.memory.session_manager import session_manager

# Base de conocimiento sobre documentos en BUK
BASE_CONOCIMIENTO_BUK = {
    "liquidacion": "Puedes descargar tu liquidación de sueldo ingresando a la plataforma BUK con tu usuario y contraseña. En la sección 'Mis Documentos', selecciona 'Liquidaciones' y descarga el archivo en formato PDF.",
    "otros_documentos": "Para acceder a otros documentos laborales en BUK, ingresa a la plataforma con tu usuario y dirígete a la sección correspondiente. Si tienes dudas, consulta con Recursos Humanos."
}


def handle_documentos_query(session_id, user_input):
    """
    Responde preguntas sobre la obtención de documentos en BUK y guarda la conversación en la sesión.
    """
    # Obtener la sesión actual o crear una nueva si no existe
    state = session_manager.get_session(session_id)
    if state is None:
        state = session_manager.create_session()

    # Detectar si la consulta es sobre liquidaciones de sueldo
    if "liquidación" in user_input or "imprimir mi sueldo" in user_input or "descargar mi sueldo" in user_input:
        respuesta = BASE_CONOCIMIENTO_BUK["liquidacion"]
    else:
        respuesta = BASE_CONOCIMIENTO_BUK["otros_documentos"]

    # Agregar la respuesta al historial de la sesión
    state.add_message(user_input, respuesta)

    # Actualizar la sesión con el nuevo historial
    session_manager.update_session(session_id, state)

    return state
