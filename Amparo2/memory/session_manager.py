import uuid
from Amparo2.memory.chat_state import ChatState  # ✅ Ahora importamos ChatState correctamente

class SessionManager:
    def __init__(self):
        self.sessions = {}  # Diccionario para almacenar sesiones activas

    def create_session(self):
        """
        Crea una nueva sesión con un ID único y un objeto ChatState.
        """
        session_id = str(uuid.uuid4())  # Genera un ID único
        self.sessions[session_id] = ChatState()  # 📌 Almacenar un objeto ChatState
        return session_id

    def get_session(self, session_id):
        """
        Obtiene el historial de la sesión si existe.
        """
        return self.sessions.get(session_id, None)

    def update_session(self, session_id, state):
        """
        Actualiza el estado del historial de chat en una sesión específica.
        """
        if session_id in self.sessions:
            self.sessions[session_id] = state

    def end_session(self, session_id):
        """
        Elimina la sesión una vez que el usuario finaliza el chat.
        """
        if session_id in self.sessions:
            del self.sessions[session_id]

# Instancia global del gestor de sesiones
session_manager = SessionManager()
