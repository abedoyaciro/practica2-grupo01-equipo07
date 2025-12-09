# Guía de Pruebas y Verificación - Sistema Agentic AI

Esta guía te permitirá configurar el entorno, verificar la instalación y ejecutar pruebas paso a paso de cada componente del sistema.

## 1. Análisis de Código de Referencia

He analizado el contenido de la carpeta `docs/codigo_referencia` y confirmo que hemos utilizado los siguientes patrones fundamentales:

*   **Uso de Gemini y Embeddings**: Basado en `04_Embeddings_LangChain1_Gemini.ipynb` y `05_BD_vectores_Gemini_LangChain1.ipynb`. Hemos implementado `GoogleGenerativeAIEmbeddings` tal como se sugiere.
*   **Vector Store (FAISS)**: Inspirado en `05_BD_vectores_Gemini_LangChain1.ipynb`, usamos FAISS para indexación eficiente local.
*   **LangChain Chains**: La estructura de `LLMChain` y `PromptTemplate` se alinea con los ejemplos básicos de `LangChain_v1_OpenAI.ipynb` y `02_Wikipedia_Gemini_LangChain1.ipynb`, adaptándolos a la nueva arquitectura basada en clases y Agentes.
*   **Carga de Documentos**: El uso de `PyPDFLoader` y `DirectoryLoader` sigue las prácticas de `01_Cargadores_documentos_Gemini.ipynb`.

**Diferencia Clave**: Hemos evolucionado de notebooks sueltos a una arquitectura modular orientada a objetos (`class Agent`), lista para producción, con separación de responsabilidades y orquestación centralizada.

## 2. Configuración del Entorno de Pruebas

Para no afectar tu instalación global de Python, crearemos un entorno virtual.

### Paso 2.1: Verificar Python
Abre una terminal (PowerShell o CMD) en la carpeta del proyecto y ejecuta:
```powershell
python --version
```
Debes tener Python 3.10 o superior (he detectado Python 3.12.7 en tu sistema, lo cual es perfecto).

### Paso 2.2: Crear el Entorno Virtual
Ejecuta el siguiente comando para crear una carpeta `venv` que contendrá las librerías:
```powershell
python -m venv venv
```

### Paso 2.3: Activar el Entorno
*   **En PowerShell:**
    ```powershell
    .\venv\Scripts\Activate.ps1
    ```
    (Si sale error de ejecución de scripts, usa: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process` y reintenta).

*   **En CMD:**
    ```cmd
    venv\Scripts\activate.bat
    ```

Verás que tu terminal ahora empieza con `(venv)`.

### Paso 2.4: Instalar Dependencias
Instala las librerías necesarias con:
```powershell
pip install -r requirements.txt
```
(Esto puede tardar unos minutos).

## 3. Pruebas Funcionales Paso a Paso

Asegúrate de tener tu archivo `.env` configurado con las API Keys (ver `docs/GUIA_CONFIGURACION.md`).

### Prueba 1: Indexación de Documentos
El primer paso es procesar los documentos.
1.  Asegúrate de que hay PDFs en `data/documents/`.
2.  Ejecuta el agente indexador:
    ```powershell
    python src/agents/indexer_agent.py
    ```
3.  **Resultado Esperado**: Deberías ver logs indicando "Cargando documentos...", "Dividiendo...", y finalmente "Almacén vectorial guardado...". Se creará la carpeta `data/vector_store/financial_docs_index`.

### Prueba 2: Clasificación de Intención (Agente Clasificador)
Verificaremos que Gemini clasifique bien las preguntas.
1.  Crea un archivo temporal `test_classifier.py` con:
    ```python
    from src.agents.classifier_agent import ClassifierAgent
    from dotenv import load_dotenv
    load_dotenv()
    
    agent = ClassifierAgent()
    print("Test 1 (search):", agent.classify("¿Qué es el riesgo de mercado?"))
    print("Test 2 (general):", agent.classify("Hola, buenos días."))
    ```
2.  Ejecútalo: `python test_classifier.py`.
3.  **Resultado**: Debería imprimir las categorías correctas.

### Prueba 3: Ejecución Completa (Orquestador)
Prueba la integración de todos los agentes.
1.  Ejecuta la aplicación principal:
    ```powershell
    python src/main.py
    ```
2.  Interactúa con el sistema:
    *   **Consulta General**: Escribe "Hola, ¿quién eres?". -> Debería responder el LLM directamente.
    *   **Búsqueda RAG**: Escribe "¿Cuáles son los factores del modelo de Fama-French?". -> Debería buscar en los documentos, generar respuesta y citar fuentes.
    *   **Resumen**: Escribe "Resume el documento sobre volatilidad implícita."
    *   **Salir**: Escribe "salir".

### Prueba 4: Verificación de Trazabilidad
1.  Después de ejecutar consultas, abre el archivo `output/trazabilidad_logs.json`.
2.  **Resultado**: Deberías ver un historial JSON con las marcas de tiempo y las acciones realizadas (inicio, clasificación, respuesta).

## 4. Inicializar Repositorio Git

Si deseas versionar tu código ignorando lo innecesario:
```powershell
git init
git add .
git commit -m "Configuración inicial del sistema Agentic AI"
```
El archivo `.gitignore` que he creado se encargará de excluir `venv`, `.env` y el código de referencia automáticamente.
