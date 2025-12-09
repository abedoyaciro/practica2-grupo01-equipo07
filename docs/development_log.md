# Bitácora de Desarrollo - Práctica 2 Agentic AI

## Estado General
- **Dominio Seleccionado**: Finanzas Cuantitativas, Pricing de Activos y Riesgo Financiero.
- **Corpus**: +200 documentos PDF identificados en `data/documents`.
- **Estado**: Inicio de desarrollo.

## Historial de Cambios

### [Fecha Actual] - Inicio del Proyecto
- **Actividad**: Análisis de requerimientos y definición de arquitectura.
- **Acción**: Se modificó el `README.md` para establecer el dominio de la aplicación.
- **Acción**: Se creó el plan de implementación y la lista de tareas.
- **Arquitectura Definida**:
    - **Framework**: LangChain 1.0.
    - **Agentes**:
        1. Indexador (FAISS + Embeddings).
        2. Clasificador de Intención (Gemini).
        3. Recuperador (Groq).
        4. Generador RAG (Groq).
        5. Evaluador/Crítico (Gemini).
        6. Orquestador (Groq).

## Próximos Pasos
1. Configuración del entorno (`requirements.txt`, variables de entorno).
2. Implementación del Agente Indexador para procesar los documentos financieros.
3. Desarrollo de las herramientas (Tools) base.
