### 📌 **README.md** (Copia y pega directamente en tu archivo `README.md`)


# 🏗️ Amparo - Sistema Multiagente con LangGraph

**Amparo** es un **sistema multiagente basado en LangGraph** diseñado para asistir a los trabajadores de la empresa de construcción a través de un **tótem de autoatención** en la oficina de Recursos Humanos.

## 📌 **Objetivo del Proyecto**
- **Brindar asistencia automatizada** sobre temas de **recursos humanos**.
- **Responder preguntas sobre:**
  - 📅 **Sueldos y anticipos**
  - 📜 **Reglamento interno**
  - 🎁 **Beneficios (Caja Los Andes, Cámara Chilena de la Construcción, etc.)**
  - 📑 **Documentos de RRHH (ej. liquidaciones en BUK)**
- **Mantener historial de conversación** con cada usuario.
- **Persistir sesiones en SQLite** para que la información no se pierda tras un reinicio.
- **Visualizar el flujo del sistema con un grafo.**

---

## 📌 **Tecnologías Utilizadas**
- 🔹 **LangGraph** (Sistema multiagente)
- 🔹 **LangChain** (Manejo de consultas a documentos)
- 🔹 **OpenAI GPT-4** (Procesamiento del lenguaje natural)
- 🔹 **SQLite** (Persistencia de sesiones)
- 🔹 **ChromaDB** (Vector store para consultas en PDF)
- 🔹 **Tavily API** (Búsqueda en la web para beneficios)
- 🔹 **Graphviz & Mermaid.js** (Visualización del sistema)

---

## 📌 **Arquitectura del Sistema**
### **🔗 Flujo de Interacción**
1️⃣ **Un trabajador se acerca al tótem** y Amparo inicia un nuevo chat con:  
   🗨️ *"¿En qué le puedo ayudar hoy?"*  
2️⃣ **El usuario realiza una consulta**.  
3️⃣ **Amparo clasifica la intención de la consulta** y la dirige al agente correcto.  
4️⃣ **El agente especializado responde** y Amparo muestra la respuesta al usuario.  
5️⃣ **El historial se guarda en SQLite** para mantener contexto en la conversación.  

---

## 📌 **Estructura del Proyecto**
```
Amparo/
│── Amparo2/
│   ├── agents/             # Agentes especializados
│   │   ├── amparo_agent.py      # Agente principal (Router)
│   │   ├── sueldo_agent.py      # Responde sobre sueldos y anticipos
│   │   ├── beneficios_agent.py  # Responde sobre beneficios laborales
│   │   ├── reglamento_agent.py  # Busca información en el reglamento interno
│   │   ├── documentos_agent.py  # Gestiona documentos en BUK
│   ├── memory/
│   │   ├── session_manager.py  # Manejo de sesiones con SQLite
│   ├── utils/
│   │   ├── intent_classifier.py  # Clasifica la intención de las consultas
│   │   ├── reglamento_loader.py  # Carga el PDF del reglamento en ChromaDB
│   ├── scripts/
│   │   ├── probar_sistema.py     # Simula una conversación con Amparo
│   │   ├── visualizar_grafo.py   # Genera el grafo del sistema
│── sessions.db  # Base de datos SQLite para sesiones
│── README.md
│── requirements.txt
```

---

## 📌 **Agentes del Sistema**
### **👩‍💼 Amparo (Agente Principal)**
🔹 **Función:** Dirige las consultas al agente correcto y responde al usuario.  
🔹 **Manejo de estado:** Guarda la conversación en SQLite para recordar el contexto.  

### **💰 SueldoAgent**
🔹 **Función:** Responde preguntas sobre **sueldos, anticipos y liquidaciones.**  
🔹 **Fuente de información:** Base de conocimiento interna.  
🔹 **Redirige solicitudes de impresión de liquidaciones a `DocumentosAgent`.**  

### **📜 ReglamentoAgent**
🔹 **Función:** Busca información en el **Reglamento Interno de la empresa.**  
🔹 **Fuente de información:** Un **PDF cargado en ChromaDB.**  
🔹 **Mejora reciente:** **Resumir el contenido antes de responder.**  

### **🎁 BeneficiosAgent**
🔹 **Función:** Busca información sobre **beneficios laborales.**  
🔹 **Fuente de información:** Web **(usando Tavily API)**.  
🔹 **Mejora reciente:** **Ahora resume la información en lugar de solo devolver enlaces.**  

### **📑 DocumentosAgent**
🔹 **Función:** Gestiona solicitudes de documentos en **BUK**.  
🔹 **Fuente de información:** Enlaza con la plataforma de Recursos Humanos.  

---

## 📌 **Manejo de Sesiones con SQLite**
📌 **Antes:** Las sesiones se perdían al reiniciar el sistema.  
✅ **Ahora:** Las sesiones se almacenan en **SQLite** y son **persistentes.**  

🔹 **Al iniciar una conversación:** Se crea una sesión en `sessions.db`.  
🔹 **Cada mensaje enviado:** Se guarda en la base de datos.  
🔹 **Si el usuario vuelve a interactuar:** Se carga su historial anterior.  

---

## 📌 **Visualización del Sistema**
### 📌 **Generación del Grafo con Mermaid.js**
📌 **Genera una visualización del flujo de agentes en Amparo.**  

1️⃣ **Ejecuta el siguiente comando:**
```bash
python scripts/visualizar_grafo.py
```
2️⃣ **Resultado esperado:**
```
✅ Grafo Mermaid guardado en 'grafo_amparo.mmd'.
✅ Grafo generado correctamente como 'grafo_amparo.png'.
```
3️⃣ **Visualización en la Web:**
   - Copia el contenido de `grafo_amparo.mmd`.
   - Abre [Mermaid Live Editor](https://mermaid-js.github.io/mermaid-live/).
   - Pega el código y verás el diagrama del sistema.  

---

## 📌 **Cómo Ejecutar el Proyecto**
### **1️⃣ Instalar Dependencias**
```bash
pip install -r requirements.txt
```

### **2️⃣ Cargar el Reglamento Interno en ChromaDB**
```bash
python scripts/cargar_reglamento.py
```

### **3️⃣ Probar el Sistema**
```bash
python scripts/probar_sistema.py
```

### **4️⃣ Ver el Grafo del Sistema**
```bash
python scripts/visualizar_grafo.py
```

---

## 📌 **Mejoras Implementadas**
✅ **Persistencia de sesiones con SQLite**.  
✅ **Búsqueda web mejorada con Tavily API**.  
✅ **Respuestas resumidas en ReglamentoAgent y BeneficiosAgent**.  
✅ **Visualización del sistema con Mermaid.js**.  

---

## 📌 **Siguientes Mejoras**
🔹 **Agregar autenticación de usuarios para sesiones personalizadas.**  
🔹 **Optimizar clasificación de intenciones con modelos de IA más avanzados.**  
🔹 **Implementar API REST para conectar Amparo con otras plataformas.**  

---

### **📌 Contribuciones**
Si deseas contribuir, por favor abre un **Pull Request** o envía tus sugerencias en Issues.

📌 **¡Gracias por usar Amparo! 🚀😊**


---

✅ **Este README.md ahora está completamente actualizado** con las **últimas mejoras del proyecto**.  
📌 **Prueba copiarlo en tu proyecto y dime si necesitas ajustes. 🚀😊**