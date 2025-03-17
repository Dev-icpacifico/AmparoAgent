from dotenv import load_dotenv

from Amparo2.memory.session_manager import session_manager
from tavily import TavilyClient
import os

# Cargar variables de entorno
load_dotenv()

# Configurar API de Tavily
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
tavily_client = TavilyClient(api_key=TAVILY_API_KEY)

def handle_beneficios_query(session_id, user_input):
    """
    Busca información en Tavily sobre beneficios y genera un resumen para el usuario.
    """
    state = session_manager.get_session(session_id)
    if state is None:
        state = session_manager.create_session()

    # 📌 Realizar la búsqueda con Tavily
    try:
        search_results = tavily_client.search(query=user_input, max_results=3)
        articles = search_results.get("results", [])

        if not articles:
            respuesta = "No encontré información relevante sobre tu consulta. Intenta buscar en la página de Caja Los Andes."
        else:
            # 📌 Generar un resumen de los artículos encontrados
            resumen = "\n\n".join([f"📌 {art['title']}: {art['content'][:300]}..." for art in articles])
            respuesta = f"Encontré esta información relevante sobre beneficios:\n\n{resumen}"

    except Exception as e:
        print(f"❌ Error en la búsqueda web: {e}")
        respuesta = "Hubo un problema al obtener información en la web. Inténtalo más tarde."

    state.add_message(user_input, respuesta)
    session_manager.update_session(session_id, state)

    return state
