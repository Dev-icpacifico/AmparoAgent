import sqlite3
import json

class ChatState:
    """
    Representa el estado de una conversación con un usuario.
    Guarda el historial de mensajes en la base de datos SQLite.
    """
    def __init__(self, session_id):
        self.session_id = str(session_id)  # Asegurar que sea una string
        self.history = self._load_history()  # Cargar historial desde SQLite

    def _load_history(self):
        """
        Carga el historial de conversación desde la base de datos.
        """
        conn = sqlite3.connect("sessions.db")
        cursor = conn.cursor()
        cursor.execute("SELECT history FROM sessions WHERE session_id = ?", (self.session_id,))
        row = cursor.fetchone()
        conn.close()
        return json.loads(row[0]) if row else []

    def add_message(self, user_input, amparo_response):
        """
        Agrega un nuevo mensaje al historial de la conversación y lo guarda en SQLite.
        """
        self.history.append({"usuario": user_input, "amparo": amparo_response})
        self._save_history()

    def _save_history(self):
        """
        Guarda el historial de la sesión en SQLite.
        """
        conn = sqlite3.connect("sessions.db")
        cursor = conn.cursor()
        cursor.execute("INSERT OR REPLACE INTO sessions (session_id, history) VALUES (?, ?)",
                       (self.session_id, json.dumps(self.history)))
        conn.commit()
        conn.close()

    def get_history(self):
        """
        Devuelve el historial completo de la conversación.
        """
        return self.history


class SessionManager:
    """
    Administra sesiones de conversación con múltiples usuarios usando SQLite.
    """
    def __init__(self):
        self._setup_database()

    def _setup_database(self):
        """
        Crea la tabla de sesiones en SQLite si no existe.
        """
        conn = sqlite3.connect("sessions.db")
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS sessions (
                session_id TEXT PRIMARY KEY,
                history TEXT
            )
        """)
        conn.commit()
        conn.close()

    def get_session(self, session_id):
        """
        Obtiene el estado de la sesión de un usuario desde SQLite.
        """
        session_id = str(session_id)  # Asegurar que sea string
        conn = sqlite3.connect("sessions.db")
        cursor = conn.cursor()
        cursor.execute("SELECT session_id FROM sessions WHERE session_id = ?", (session_id,))
        exists = cursor.fetchone()
        conn.close()
        return ChatState(session_id) if exists else None

    def create_session(self):
        """
        Crea una nueva sesión y la guarda en SQLite.
        """
        session_id = self._generate_session_id()
        conn = sqlite3.connect("sessions.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO sessions (session_id, history) VALUES (?, ?)", (session_id, json.dumps([])))
        conn.commit()
        conn.close()
        return ChatState(session_id)

    def _generate_session_id(self):
        """
        Genera un ID único para una nueva sesión.
        """
        conn = sqlite3.connect("sessions.db")
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM sessions")
        session_count = cursor.fetchone()[0]
        conn.close()
        return str(session_count + 1)  # Genera IDs numéricos como strings

    def update_session(self, session_id, state):
        """
        Guarda el estado actualizado de la sesión en SQLite.
        """
        session_id = str(session_id)  # Asegurar que sea string
        conn = sqlite3.connect("sessions.db")
        cursor = conn.cursor()
        cursor.execute("UPDATE sessions SET history = ? WHERE session_id = ?",
                       (json.dumps(state.history), session_id))
        conn.commit()
        conn.close()


# Instancia global de SessionManager para ser usada en to_do el sistema
session_manager = SessionManager()
