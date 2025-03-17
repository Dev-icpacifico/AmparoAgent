import os
import langgraph.graph as lg
import graphviz
from Amparo2.utils.intent_cassifier import classify_intent
from Amparo2.agents.sueldo_agent import handle_sueldo_query
from Amparo2.agents.beneficios_agent import handle_beneficios_query
from Amparo2.agents.reglamento_agent import handle_reglamento_query
from Amparo2.agents.documentos_agent import handle_documentos_query

# 📌 Definir manualmente la ruta a Graphviz si es necesario (Windows)
os.environ["PATH"] += os.pathsep + r"C:\Program Files\Graphviz\bin"

# Crear el grafo de LangGraph
workflow = lg.Graph()
workflow.add_node("Amparo", lambda x: x)
workflow.add_node("SueldoAgent", handle_sueldo_query)
workflow.add_node("BeneficiosAgent", handle_beneficios_query)
workflow.add_node("ReglamentoAgent", handle_reglamento_query)
workflow.add_node("DocumentosAgent", handle_documentos_query)

# Función de enrutamiento
def router(user_input):
    intent = classify_intent(user_input)
    return {
        "sueldo": "SueldoAgent",
        "beneficios": "BeneficiosAgent",
        "reglamento": "ReglamentoAgent",
        "documentos": "DocumentosAgent"
    }.get(intent, "Amparo")

# Agregar el enrutador
workflow.set_entry_point("Amparo")
workflow.add_conditional_edges("Amparo", router, {
    "SueldoAgent": "SueldoAgent",
    "BeneficiosAgent": "BeneficiosAgent",
    "ReglamentoAgent": "ReglamentoAgent",
    "DocumentosAgent": "DocumentosAgent"
})

workflow = workflow.compile()

# 📌 Generar el grafo como Mermaid
graph_mermaid = workflow.get_graph().draw_mermaid()

# Guardar el grafo Mermaid en un archivo de texto
mermaid_file = "grafo_amparo.mmd"
with open(mermaid_file, "w") as f:
    f.write(graph_mermaid)

print(f"✅ Grafo Mermaid guardado en '{mermaid_file}'. Puedes visualizarlo en: https://mermaid-js.github.io/mermaid-live/")

# 📌 Convertir Mermaid a PNG usando Graphviz
try:
    graph = graphviz.Source(graph_mermaid)
    graph.render("grafo_amparo", format="png", cleanup=False)
    print("✅ Grafo generado correctamente como 'grafo_amparo.png'.")
except Exception as e:
    print(f"❌ Error al generar el PNG: {e}")
    print("⚠️ Puedes abrir 'grafo_amparo.mmd' en https://mermaid-js.github.io/mermaid-live/")
