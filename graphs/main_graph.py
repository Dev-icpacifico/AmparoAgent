from langgraph.graph import StateGraph, START, END, MessagesState
from langchain_openai import ChatOpenAI
from IPython.display import display, Image


class State(MessagesState):
    pregunta: str


# Primer nodo con la consulta al pago de sueldos
def consulta_sueldos(state: dict):
    """Agente encargado de responder sobre las fechas de pago de remuneraciones"""
    pregunta = state.get("pregunta", "").lower()  # 🔹 Corregido para usar .get()

    if "fecha de pago" in pregunta:
        return {"pregunta": "Las fechas de pago de sueldos son el 30 de cada mes"}

    return {"pregunta": "Lo siento, no puedo responder a esa consulta."}


# Crear el flujo del grafo
workflow = StateGraph(State)

# Agregar nodos al grafo
workflow.add_node("consulta_sueldos", consulta_sueldos)

# Definir flujo de nodos
workflow.add_edge(START, "consulta_sueldos")
workflow.add_edge("consulta_sueldos", END)

# Compilar el grafo
graph = workflow.compile()

# Mostrar el grafo en una imagen
display(Image(graph.get_graph().draw_mermaid_png()))

# Ejecutar flujo con prueba inicial
if __name__ == "__main__":
    estado_inicial = {"pregunta": "¿Cual es mi nombre?"}  # 🔹 Ahora es un diccionario
    response = graph.invoke(estado_inicial)

    print(response["pregunta"])  # 🔹 Accede correctamente a la respuesta
