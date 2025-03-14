from Amparo2.memory.session_manager import session_manager

# Base de conocimiento sobre sueldos
BASE_CONOCIMIENTO_SUELDOS = {
    "anticipos": "El máximo de anticipo permitido es el 40% del sueldo líquido del mes anterior.",
    "explicacion_liquidacion": "Tu sueldo líquido final se calcula restando los descuentos legales (AFP, salud, impuestos) y otros descuentos aplicables al sueldo bruto."
}


def handle_sueldo_query(session_id, user_input):
    """
    Responde preguntas sobre anticipos y explicaciones de liquidaciones, manteniendo la sesión.
    """
    # Obtener la sesión actual o crear una nueva si no existe
    state = session_manager.get_session(session_id)
    if state is None:
        state = session_manager.create_session()

    # Detectar el tipo de consulta dentro de sueldos
    if "anticipo" in user_input or "aumentar" in user_input or "disminuir" in user_input:
        respuesta = BASE_CONOCIMIENTO_SUELDOS["anticipos"]
    elif "liquidación" in user_input or "descuento" in user_input or "sueldo líquido" in user_input:
        respuesta = BASE_CONOCIMIENTO_SUELDOS["explicacion_liquidacion"]
    else:
        respuesta = "No tengo información sobre esa consulta específica de sueldos."

    # Agregar la respuesta al historial de la sesión
    state.add_message(user_input, respuesta)

    # Actualizar la sesión con el nuevo historial
    session_manager.update_session(session_id, state)

    return state
