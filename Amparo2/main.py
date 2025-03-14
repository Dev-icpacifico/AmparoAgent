from Amparo2.utils.pdf_loader import extract_text_from_pdf
from Amparo2.utils.vector_store import store_pdf_in_chroma
from Amparo2.agents.pdf_agent import ask_pdf_agent

# 1. Extraer texto del PDF
pdf_path = "R.I.O.H.S CONST. Ene. 2025.pdf"
text = extract_text_from_pdf(pdf_path)

# 2. Almacenar el texto en ChromaDB
store_pdf_in_chroma(text, "pdf_collection")

# 3. Consultar el agente
question = "¿De qué se trata este documento?"
answer = ask_pdf_agent(question, "pdf_collection")

print("Respuesta del agente:", answer)
