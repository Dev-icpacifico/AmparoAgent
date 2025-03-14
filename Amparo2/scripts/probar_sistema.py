from Amparo2.agents.amparo_agent import amparo_router
from Amparo2.memory.session_manager import session_manager

# Crear una nueva sesión
session_id = session_manager.create_session()

print("👋 Amparo: ¿En qué le puedo ayudar hoy?")
while True:
    user_input = input("🧑 Usuario: ")  # Entrada del usuario

    if user_input.lower() in ["salir", "terminar", "exit"]:
        print("👋 Amparo: ¡Hasta luego!")
        session_manager.end_session(session_id)  # Terminar sesión
        break

    # Enviar la consulta a Amparo
    state = amparo_router(session_id, user_input)

    # Obtener la última respuesta de Amparo
    last_message = state.history[-1]["amparo"]
    print(f"🤖 Amparo: {last_message}")
