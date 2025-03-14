# 🏗️ Amparo - Asistente Virtual de RRHH 📢

**Amparo** es un **sistema multiagente basado en LangGraph** diseñado para asistir a los trabajadores de una empresa de construcción mediante un **tótem de autoatención**.  
Este sistema permite responder consultas sobre **sueldos, reglamento interno, beneficios y documentos laborales**, proporcionando información precisa y automatizada.

---

## **🎯 Objetivos del Proyecto**
El sistema **Amparo** tiene como objetivo proporcionar una plataforma de atención eficiente y automatizada para los trabajadores de la empresa. Se enfoca en:

✅ **Reducir la carga de trabajo del personal de RRHH**, proporcionando respuestas automáticas a consultas frecuentes.  
✅ **Facilitar el acceso a información clave**, como el reglamento interno, fechas de pago y beneficios disponibles.  
✅ **Permitir la consulta y solicitud de documentos laborales** sin necesidad de intervención humana.  
✅ **Ofrecer una experiencia de usuario intuitiva y accesible a través de un tótem de autoatención.**  

---

## **📌 Alcance del Proyecto**
El sistema **Amparo** está diseñado para responder consultas **exclusivamente dentro del ámbito de Recursos Humanos**, incluyendo:

🔹 **Consultas sobre sueldos:** Anticipos, fechas de pago y descuentos en la liquidación.  
🔹 **Normativa interna:** Reglas de la empresa, derechos y deberes de los trabajadores.  
🔹 **Beneficios laborales:** Información sobre Caja Los Andes, convenios y seguros.  
🔹 **Documentos oficiales:** Liquidaciones de sueldo, contratos y certificados.  

❌ **No responde consultas fuera de estos temas**. Si el usuario hace una pregunta fuera del alcance, **Amparo le indicará que no puede ayudarle**.

---

## **🧠 Agentes Implementados y Funcionalidades**
El sistema Amparo está diseñado bajo una arquitectura **multiagente**, donde cada tipo de consulta es manejada por un **agente especializado**.

| **Agente**           | **Descripción y Funcionalidades** |
|----------------------|----------------------------------|
| `amparo_agent.py`   | **Agente principal.** Recibe las consultas de los trabajadores y las redirige al agente especializado adecuado. También maneja las respuestas finales que se mostrarán al usuario. |
| `sueldo_agent.py`   | **Maneja consultas sobre sueldos.** Responde preguntas sobre: (1) montos de anticipos, (2) explicación de descuentos en la liquidación, (3) redirigir solicitudes de impresión de liquidaciones al agente de documentos. |
| `beneficios_agent.py` | **Obtiene información en tiempo real sobre beneficios.** Utiliza Google para buscar información actualizada sobre Caja Los Andes, la Cámara Chilena de la Construcción y otros beneficios disponibles para los trabajadores. |
| `reglamento_agent.py` | **Busca información en el reglamento interno.** Utiliza ChromaDB para encontrar fragmentos relevantes de un PDF previamente cargado con las normas de la empresa. Se encarga de responder preguntas sobre derechos, prohibiciones y reglamentaciones internas. |
| `documentos_agent.py` | **Maneja solicitudes de documentos.** Responde preguntas sobre cómo acceder a documentos laborales en la plataforma BUK y redirige al usuario a la sección correspondiente para descargar liquidaciones, contratos y certificados. |

---

## **📂 Estructura del Proyecto**
```bash
Amparo/
│── Amparo2/
│   ├── agents/                 # Agentes inteligentes del sistema
│   │   ├── amparo_agent.py      # Agente principal (Amparo)
│   │   ├── sueldo_agent.py      # Maneja consultas de sueldos
│   │   ├── beneficios_agent.py  # Busca información sobre beneficios
│   │   ├── reglamento_agent.py  # Responde consultas sobre el reglamento interno
│   │   ├── documentos_agent.py  # Maneja consultas sobre documentos en BUK
│   ├── memory/                  # Manejador de sesiones
│   │   ├── session_manager.py    # Permite gestionar el historial de cada usuario
│   │   ├── chat_state.py         # Define el estado del chat
│   ├── utils/                    # Utilidades del sistema
│   │   ├── intent_classifier.py   # Clasificación de intención de preguntas
│   │   ├── reglamento_loader.py   # Carga y búsqueda en el reglamento interno
│   ├── scripts/                   # Scripts auxiliares
│   │   ├── cargar_reglamento.py   # Script para indexar el reglamento interno
│   │   ├── probar_sistema.py      # Script para probar Amparo en la terminal
│   ├── documentos/                # PDFs del reglamento
│   ├── chroma_db/                 # Base de datos de ChromaDB
│── README.md                      # Documentación del proyecto
│── requirements.txt                # Dependencias del proyecto
```

---

## **🔧 Instalación**
### **1️⃣ Clonar el repositorio**
```bash
git clone https://github.com/tu-usuario/amparo.git
cd amparo
```

### **2️⃣ Crear un entorno virtual**
```bash
python -m venv .venv
source .venv/bin/activate  # Mac/Linux
.venv\Scripts\activate      # Windows
```

### **3️⃣ Instalar dependencias**
```bash
pip install -r requirements.txt
```

---

## **⚙️ Configuración**
### **1️⃣ Configurar Variables de Entorno**
Crea un archivo **`.env`** en la raíz del proyecto con tu clave de OpenAI:
```ini
OPENAI_API_KEY="tu-clave-de-openai"
```

### **2️⃣ Instalar Dependencias Adicionales**
Si aparecen advertencias de deprecación, actualiza LangChain:
```bash
pip install -U langchain-openai langchain-chroma
```

---

## **🚀 Uso del Sistema**
### **1️⃣ Indexar el Reglamento Interno**
Antes de hacer preguntas sobre el reglamento, es necesario cargarlo en la base de datos vectorial:
```bash
python scripts/cargar_reglamento.py
```

### **2️⃣ Probar Amparo en la Terminal**
Para simular una interacción con el tótem:
```bash
python scripts/probar_sistema.py
```
👤 **Ejemplo de conversación:**
```
👋 Amparo: ¿En qué le puedo ayudar hoy?
🧑 Usuario: ¿Cuánto anticipo puedo solicitar?
🤖 Amparo: El máximo de anticipo permitido es el 50% del sueldo líquido del mes anterior.
🧑 Usuario: ¿Qué dice el reglamento sobre el uso del celular?
🤖 Amparo: Según el reglamento interno: "El uso de celulares está prohibido durante la jornada laboral excepto en descansos."
```

---

## **🧠 Agentes Implementados y Funcionalidades**
| **Agente**           | **Descripción** |
|----------------------|----------------|
| `amparo_agent.py`   | **Agente principal.** Enruta las consultas al agente adecuado. |
| `sueldo_agent.py`   | **Maneja consultas sobre sueldos.** Responde sobre anticipos, descuentos y liquidaciones. |
| `beneficios_agent.py` | **Busca información sobre beneficios.** Usa Google para obtener datos actualizados sobre Caja Los Andes y otros beneficios. |
| `reglamento_agent.py` | **Responde preguntas sobre el reglamento interno.** Usa ChromaDB para recuperar información desde un PDF indexado. |
| `documentos_agent.py` | **Maneja solicitudes de documentos en BUK.** Redirige a la plataforma adecuada para descargar liquidaciones de sueldo y otros documentos laborales. |

---

## **📌 Scripts Auxiliares**
| **Script**              | **Descripción** |
|------------------------|----------------|
| `cargar_reglamento.py` | Carga el PDF del reglamento en ChromaDB |
| `probar_sistema.py`   | Permite probar Amparo desde la terminal |

---

## **🛠️ Solución de Problemas**
### **1️⃣ ChromaDB No Guarda Datos**
**Solución:**
```bash
rm -rf chroma_db/
python scripts/cargar_reglamento.py
```

### **2️⃣ "No encontré información en el reglamento"**
Si Amparo no encuentra información relevante, revisa `reglamento_loader.py` y baja el umbral de similitud:
```python
umbral_similitud = 0.2  # En lugar de 0.7
```

### **3️⃣ Error: `The class Chroma was deprecated`**
**Solución:**
```bash
pip install -U langchain-chroma
```
Y cambia:
```python
from langchain_community.vectorstores import Chroma
```
Por:
```python
from langchain_chroma import Chroma
```

---

## **📜 Licencia**
Este proyecto está bajo la licencia MIT.  

---

## **💡 Próximos Pasos**
🔹 **Integrar FastAPI** para exponer el sistema como un servicio web.  
🔹 **Mejorar la precisión en la recuperación de información desde ChromaDB.**  
🔹 **Agregar más agentes especializados en otras áreas de RRHH.**  

---
