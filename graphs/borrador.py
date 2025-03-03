from langgraph.graph import StateGraph, START, END, MessagesState
from langchain_openai import ChatOpenAI
from IPython.display import display


class State(MessagesState):
    pregunta: str


# Primer nodo con la consulta al pago de sueldos
def consulta_sueldos(state: State):
    """Agente encargado de responder sobre las fechas de pago de remuneraciones"""
    consulta = state.pregunta.lower()

    if "fecha de pago" in consulta:
        return State(pregunta="Las fechas de pago de sueldos son el 30 de cada mes")

    return State(pregunta="Lo siento, no puedo responder a esa consulta")


# Crear el grafo
workflow = StateGraph(State)

# Agregar nodos
workflow.add_node("consulta_sueldos", consulta_sueldos)

# Definir flujo de nodos
workflow.add_edge(START, "consulta_sueldos")
workflow.add_edge("consulta_sueldos", END)

# Compilar el grafo
graph = workflow.compile()

# Ver gráfico en texto (útil para entornos sin IPython)
print(graph.get_graph().draw_mermaid())

# Ejecutar flujo con prueba inicial
if __name__ == "__main__":
    estado_inicial = State(pregunta="¿Cuál es la fecha de pago del sueldo?")
    response = workflow.invoke(estado_inicial)
    print(response.pregunta)
