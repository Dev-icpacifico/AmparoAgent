# 📂 Estructura de Directorios para el Proyecto LangGraph

Este archivo describe la estructura de directorios utilizada en el proyecto basado en LangGraph.

```
/mi_agente_langgraph
│── /agents                  # Definición de agentes (nodos en el grafo)
│   ├── __init__.py
│   ├── base_agent.py        # Clase base para agentes
│   ├── agent_1.py           # Implementación de un agente específico
│   ├── agent_2.py           # Otro agente en el sistema
│── /graphs                  # Implementación de los grafos multiagente
│   ├── __init__.py
│   ├── base_graph.py        # Configuración base para grafos
│   ├── main_graph.py        # Grafo principal con agentes conectados
│── /states                  # Manejo del estado compartido entre agentes
│   ├── __init__.py
│   ├── state_manager.py     # Gestión del estado global
│── /utils                   # Utilidades y funciones auxiliares
│   ├── __init__.py
│   ├── helpers.py           # Funciones de soporte
│── /config                  # Configuración del proyecto
│   ├── config.yaml          # Variables de configuración
│   ├── settings.py
│── /logs                    # Archivos de logs
│── /tests                   # Pruebas unitarias y de integración
│   ├── __init__.py
│   ├── test_agents.py
│   ├── test_graphs.py
│   ├── test_states.py
│── main.py                   # Script principal para ejecutar el sistema
│── requirements.txt          # Dependencias del proyecto
│── README.md                 # Documentación del proyecto
```

## 📌 Explicación de los directorios:

### `/agents/`
Contiene la definición de los agentes, que son los nodos en el grafo de LangGraph.
- `base_agent.py`: Clase base para todos los agentes.
- `agent_1.py`, `agent_2.py`: Implementaciones de agentes específicos.

### `/graphs/`
Define la estructura del sistema multiagente usando grafos.
- `base_graph.py`: Configuración base del grafo.
- `main_graph.py`: Implementación del grafo principal, conectando a los agentes.

### `/states/`
Manejo del estado compartido entre los agentes.
- `state_manager.py`: Administra la información que los agentes pueden compartir.

### `/utils/`
Funciones auxiliares y utilidades comunes para el proyecto.

### `/config/`
Archivos de configuración del sistema.
- `config.yaml`: Configuración general del proyecto.
- `settings.py`: Variables de entorno y configuraciones específicas.

### `/logs/`
Almacena logs del sistema para monitoreo y depuración.

### `/tests/`
Contiene pruebas unitarias y de integración.
- `test_agents.py`: Pruebas de agentes.
- `test_graphs.py`: Pruebas de la estructura del grafo.
- `test_states.py`: Validación del estado compartido.

### Archivos principales:
- `main.py`: Punto de entrada principal del proyecto.
- `requirements.txt`: Lista de dependencias necesarias.
- `README.md`: Documentación general del proyecto.

Esta estructura permite modularidad y escalabilidad para futuros desarrollos 🚀.

