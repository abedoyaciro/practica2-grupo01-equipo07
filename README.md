# Práctica 2: Sistema Agentic AI Multi-Agente con RAG (LLMs Gemini y Groq)

## 🎯 Objetivo Concreto de la Práctica

El objetivo principal es **diseñar e implementar un sistema de Recuperación Aumentada (RAG)** basado en una arquitectura **Agentic AI multi-agente** utilizando **LangChain 1.0**. El sistema debe ser capaz de procesar, indexar y responder preguntas complejas sobre un corpus de **100 documentos** en el dominio de **Finanzas Cuantitativas, Pricing de Activos y Riesgo Financiero**, empleando al menos cinco agentes especializados y realizando una integración justificada de los modelos **Gemini** y **Groq**.

## 🛠️ Cómo se Realizará (Metodología)

El proyecto se abordará mediante la construcción de un flujo de trabajo orquestado por agentes. Este flujo debe garantizar el procesamiento inicial de los documentos, la clasificación de la intención del usuario y la generación de respuestas verificadas y citadas.

### Tecnología Clave

* **Framework:** LangChain 1.0 (para la definición y orquestación de agentes y herramientas).
* **LLMs:** Gemini (para tareas de razonamiento profundo y clasificación) y Groq (para respuestas rápidas y eficiencia).
* **Vector Store:** FAISS (para la indexación y recuperación semántica).
* **Documentación:** Trazabilidad explícita del flujo y justificación técnica en el informe.

## ⚙️ Actividades Prácticas Puntuales

El sistema requiere la implementación de **seis agentes** y la justificación del uso de LLMs en cada uno:

| Agente | Tarea Puntual | LLM Recomendado (Justificar en Informe) |
| :--- | :--- | :--- |
| 1. Indexador | Consumir, limpiar (chunking), generar embeddings e indexar 100 documentos en **FAISS**. | N/A (Se usa un modelo de Embeddings, no un LLM) |
| 2. Orquestador | Dirigir el flujo. Determinar el siguiente agente a ejecutar basado en la salida del Clasificador. | **Groq** (para decisiones rápidas y baja latencia). |
| 3. Clasificador | Identificar la intención del usuario: Búsqueda, Resumen, Comparación, o General. | **Gemini** (para interpretación profunda y comprensión contextual). |
| 4. Recuperador | Ejecutar búsqueda de similaridad semántica en FAISS y seleccionar los fragmentos más relevantes. | **Groq** (para optimizar la velocidad de recuperación). |
| 5. Respuesta RAG | Generar la respuesta final combinando la consulta y los fragmentos recuperados, incluyendo **citas**. | **Groq** (para generar respuestas contextuales rápidas). |
| 6. Evaluador | Evaluar la coherencia, el respaldo contextual y la ausencia de alucinaciones de la respuesta RAG. | **Gemini** (para tareas de razonamiento y validación compleja). |

---

## 🧰 Herramientas (Tools) Requeridas

Se requiere la implementación de al menos **5 Herramientas (Tools)** que puedan ser utilizadas por los agentes, según la necesidad.

**Ejemplos de Herramientas (a implementar):**

1.  **`semantic_search_tool`**: Ejecuta la búsqueda de similaridad en FAISS.
2.  **`document_summarizer_tool`**: Toma fragmentos y genera un resumen conciso.
3.  **`document_comparison_tool`**: Contraste de información entre dos o más fragmentos.
4.  **`general_llm_query_tool`**: Llama al LLM para responder preguntas fuera del corpus (intención General).
5.  **`trazability_logger_tool`**: Registra la ruta de ejecución, decisiones y documentos usados.

---

## 📂 Estructura Sencilla del Proyecto

Se propone la siguiente estructura de carpetas y archivos, siguiendo las convenciones estándar:

```
practica2-grupoXX-equipoYY/
├── src/                                  \# Código Fuente Principal
│   ├── agents/                           \# Definición de cada Agente
│   │   ├── indexer\_agent.py
│   │   ├── orchestrator\_agent.py
│   │   ├── classifier\_agent.py
│   │   ├── retriever\_agent.py
│   │   ├── rag\_response\_agent.py
│   │   └── evaluator\_agent.py
│   ├── tools/                            \# Implementación de las 5+ Tools
│   │   └── custom\_tools.py
│   ├── main.py                           \# Punto de entrada y Flujo principal de la aplicación
│   └── config.py                         \# Variables de entorno (API Keys, Paths, etc.)
├── data/
│   ├── documents/                        \# (Carpeta requerida) Al menos 100 documentos (PDF/TXT/HTML)
│   └── vector\_store/                     \# Archivos de persistencia de FAISS (.faiss, .pkl)
├── output/
│   └── trazabilidad\_logs.json            \# Archivos de registro de la trazabilidad
├── InformeTecnico.pdf                    \# (Entregable) Informe detallado del sistema
├── README.md                             \# (Este archivo) Documentación del proyecto
└── requirements.txt                      \# Dependencias de Python (LangChain, FAISS, LLMs, etc.)
```