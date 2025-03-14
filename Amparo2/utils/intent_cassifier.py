import re

# Diccionario de palabras clave para clasificar la intención
INTENT_KEYWORDS = {
    "sueldo": ["sueldo", "salario", "pago", "fecha de pago", "anticipo", "cuánto puedo solicitar"],
    "reglamento": [
        "reglamento", "normas", "política", "documento interno", "leyes de trabajo",
        "permitido", "prohibido", "consumo de alcohol", "beber alcohol", "uso de celular",
        "puedo hacer", "qué está permitido", "qué no puedo hacer", "reglas de la empresa"
    ],
    "beneficios": ["beneficio", "seguro", "caja los andes", "cámara chilena", "bono", "descuento"],
    "documentos": ["documento", "certificado", "contrato", "buk", "liquidación", "finiquito", "imprimir", "descargar", "ver liquidación"]
}




def classify_intent(user_input):
    """
    Clasifica la intención del usuario basándose en palabras clave.

    Params:
    - user_input (str): Pregunta o mensaje del usuario.

    Returns:
    - str: Tipo de intención ("sueldo", "reglamento", "beneficios", "documentos", "desconocido").
    """
    user_input = user_input.lower()  # Convertir a minúsculas para mejor coincidencia

    for intent, keywords in INTENT_KEYWORDS.items():
        for keyword in keywords:
            if re.search(rf"\b{keyword}\b", user_input):
                return intent

    return "desconocido"
