# 🎓 Universidad Nacional de Colombia - Sede Medellín

## Procesamiento del Lenguaje Natural - 3011176

### Trabajo Práctico 2 - Valor: 25%

**Título:** Agentic AI: LLMs y Langchain 1.0

* **Profesor:** Jaime Alberto Guzmán Luna
* **Fecha de Entrega:** miércoles 10 de diciembre, Hora de cierre: 12:00 meridiano.
* **Fecha de Sustentación:** Video tipo pitch entregado con el material de la práctica en la fecha de entrega enunciada anteriormente.

---

### INTRODUCCIÓN

Esta práctica tiene como fin la aplicación de los dos temas básicos vistos en clase: Transformers/LLMs y Agentic AI con LangChain 1.0. El estudiante debe seleccionar un dominio de aplicación (salud, agricultura, turismo, arte, educación, historia, etc) y construir un sistema Agentic AI basado en agentes orientado al análisis inteligente de documentos.

### OBJETIVO GENERAL

Desarrollar un sistema Agentic AI multi-agente capaz de procesar, indexar, recuperar y analizar documentos mediante un modelo RAG, empleando al menos cinco agentes especializados implementados con LangChain 1.0 e integrando los modelos LLM **Gemini** y **Groq** de forma diferenciada.

### OBJETIVOS ESPECÍFICOS

1.  Diseñar e implementar un flujo Agentic AI multi-agente que integre de manera orquestada al menos cinco agentes funcionales basados en LangChain 1.0.
2.  Implementar un agente especializado para consumo, limpieza, chunking e indexación de documentos usando embeddings y un vector store (**Faiss**).
3.  Construir un agente clasificador de intención del usuario capaz de reconocer cuatro tipos de consultas: búsqueda de información en el vector store (Faiss), resumen de documentos, comparación de documentos y consulta general (diferente a la almacenada en el sistema). Para ello se usará el LLM apropiado para identificar la intención de la solicitud del usuario.
4.  Implementar un agente recuperador semántico basado en embeddings para localizar los documentos más relevantes frente a una consulta.
5.  Desarrollar un agente generador de respuestas mediante RAG utilizando el LLM seleccionado para respuestas contextuales rápidas.
6.  Implementar un agente crítico/verificador utilizando un LLM para validar coherencia, evitar alucinaciones y garantizar el uso apropiado del contexto.
7.  Implementar al menos **5 herramientas (Tools)** apropiadas para ser usadas en las actividades de los agentes.
8.  Integrar mecanismos de **trazabilidad** para registrar decisiones, rutas ejecutadas y documentos utilizados.
9.  Elaborar un informe técnico del sistema completo y una demostración en video tipo pitch del funcionamiento completo del sistema.

---

### DESCRIPCIÓN DETALLADA DEL SISTEMA A DESARROLLAR

El sistema debe constar de los siguientes agentes:

#### 1. Agente de Consumo / Indexador
* Cargar documentos (PDF/TXT/HTML). Al menos **100 documentos** en el dominio seleccionado.
* Limpiar texto, segmentar en chunks y generar embeddings.
* Indexar información en un vector store (**FAISS**).

#### 2. Agente Orquestador (Orquestador)
* Administrar el flujo completo del sistema.
* Determinar qué agente debe ejecutarse según la consulta del usuario.
* Debe usar un LLM para decisiones rápidas y eficientes.

#### 3. Agente Clasificador de Consultas (Clasificador)
Clasificar la consulta del usuario en cuatro categorías:
* **Búsqueda de consumo:** Solicita hechos o datos específicos contenidos en los documentos mediante lenguaje natural.
* **Resumen:** Requiere hacer un resumen de uno o varios documentos.
* **Comparación:** Solicita contrastar secciones/documentos.
* **General:** No requiere acceso al corpus ni a la recuperación de la base vectorial. Se realizará una pregunta directa a un LLM seleccionado en diseño.

**Alcance del agente:**
* Determinar si la consulta requiere búsqueda semántica.
* Identificar si el usuario desea un resumen o comparación de documentos.
* Detectar si la consulta puede resolverse sin RAG llamando al LLM seleccionado (intención de respuesta general).
* Este agente deberá usar un LLM que permita una capacidad de interpretación profunda del lenguaje y comprensión contextual.

#### 4. Agente de Búsqueda Semántica (Recuperador)
* Ejecutar la búsqueda de similaridad semántica usando el vector store.
* Seleccionar los documentos más relevantes.
* Este agente deberá utilizar un LLM para optimizar la velocidad de recuperación.

#### 5. Agente de Respuesta con RAG (Agente de Respuesta)
* Construye una respuesta combinando: La consulta del usuario y los fragmentos recuperados.
* Produce respuestas justificadas con citas.
* Este agente deberá utilizar un LLM para generar respuestas rápidas basadas en contexto.

#### 6. Agente Verificador / Crítico (Evaluador)
* Evalúa si la respuesta generada:
    * Está respaldada por el contexto recuperado.
    * Es coherente y libre de alucinaciones.
    * Cumple con los requerimientos del usuario.
* En caso de fallo, solicita nueva respuesta al agente RAG (loop controlado).
* Este agente deberá utilizar un LLM para las tareas de razonamiento y validación compleja que se requiere.

### USO DIFERENCIADO DE LLMS

Se hará uso de los LLMs **Gemini** y **Groq** en los agentes donde se solicita el uso de un LLM. Se deberá hacer un análisis y presentar la respectiva justificación de cuál LLM se usará y por qué es mejor para esa actividad.

### FLUJO GENERAL DEL SISTEMA

1.  Usuario → Orquestador.
2.  Orquestador → Clasificador (Gemini).
3.  Si intención $\in$ {búsqueda, resumen, comparación}:
    * Recuperador → Agente de Respuesta → Evaluador.
    * Si la respuesta no es adecuada → regeneración de respuesta.
4.  Si intención = general:
    * Responder directamente con el LLM del respectivo agente (clasificador).
5.  Se retorna la respuesta final con trazabilidad completa.

### REQUISITOS ESPECÍFICOS

1.  Mantener trazabilidad explícita del flujo.
2.  Procesar y analizar documentos reales.

---

### ENTREGABLES

1.  **Código fuente** de la implementación Agentic AI. Deberá incluir comentarios por función y explicación del flujo general.
2.  **Carpeta con documentos** (PDF/TXT/HTML) utilizados: **100**.
3.  **Informe técnico** del sistema Agentic AI (documento PDF). Debe incluir:
    * Diseño y registros de ejecución.
    * Documentación de al menos **10 casos de uso**.
    * Explicación del porqué se seleccionó Gemini y Groq en cada agente.
4.  **Enlace de un vídeo tipo pitch** de la sustentación (máx. 5 minutos) donde se detalla el funcionamiento del sistema.

### SUSTENTACIÓN (Video tipo pitch)

* **Duración máxima:** 5 minutos.
* **Contenido:**
    * Explicación clara del problema.
    * Estructura de los componentes del sistema Agentic AI en LangChain (agentes y requerimientos).
    * Demostración funcional del sistema con sus casos de uso.
    * **Todos los integrantes deben participar.**
* El video deberá ser subido a YouTube y el enlace incluido en el Informe técnico.

### METODOLOGÍA DE EVALUACIÓN

1.  Código y documentación: **70%**
2.  Sustentación (video): **30%**

### MATERIAL POR ENTREGAR (Archivo ZIP)

Se deberá entregar en Google Classroom un archivo ZIP (Nombre: `practica3-grupo-XX-equipo-YY.zip`) que contenga:
* **Informe técnico** (PDF).
* **Código Fuente** (Python, organizado y documentado).
* **Carpeta con documentos** (100 documentos).
