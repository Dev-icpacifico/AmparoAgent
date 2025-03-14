import os
from Amparo2.utils.reglamento_loader import cargar_reglamento

# 📌 Obtener la ruta absoluta de la carpeta principal (nivel raíz del proyecto)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Sube un nivel desde "scripts/"

# 📌 Definir la ruta correcta del PDF
pdf_path = os.path.join(BASE_DIR, "documentos", "riohs", "R.I.O.H.S CONST. Ene. 2025.pdf")

# 📌 Verificar si el archivo existe antes de cargarlo
if not os.path.exists(pdf_path):
    raise FileNotFoundError(f"❌ ERROR: No se encontró el archivo en {pdf_path}. Verifica la ruta.")

# 📌 Cargar el reglamento en ChromaDB
cargar_reglamento(pdf_path)
