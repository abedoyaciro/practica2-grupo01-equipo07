import os
import json
import datetime
from typing import List, Optional
from langchain.tools import BaseTool, tool
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from src.config import VECTOR_STORE_DIR, INDEX_NAME, GOOGLE_API_KEY, GROQ_API_KEY, LOGS_FILE

# --- Configuración Inicial ---
# Usamos el MISMO modelo local que en el indexador
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# Cargar Vector Store (Se asume que ya existe, si no, se debe manejar el error)
try:
    vector_store = FAISS.load_local(
        os.path.join(VECTOR_STORE_DIR, INDEX_NAME), 
        embeddings,
        allow_dangerous_deserialization=True # Necesario para cargar pickles confiables
    )
except Exception as e:
    print(f"Advertencia: No se pudo cargar el vector store. Asegúrese de ejecutar el IndexerAgent primero. Error: {e}")
    vector_store = None

# Inicializar LLM para herramientas (Groq para rapidez)
llm_groq = ChatGroq(model_name="llama3-70b-8192", temperature=0, groq_api_key=GROQ_API_KEY)

# --- Tool 1: Búsqueda Semántica ---
@tool
def semantic_search_tool(query: str) -> str:
    """Realiza una búsqueda semántica en la base de documentos indexada para encontrar información relevante."""
    if not vector_store:
        return "Error: La base de datos vectorial no está disponible."
    
    docs = vector_store.similarity_search(query, k=5)
    result = ""
    for i, doc in enumerate(docs):
        result += f"--- Documento {i+1} ---\nFuente: {os.path.basename(doc.metadata.get('source', 'Desconocido'))}\nContenido: {doc.page_content}\n\n"
    return result

# --- Tool 2: Resumidor de Documentos ---
@tool
def document_summarizer_tool(text: str) -> str:
    """Genera un resumen conciso del texto proporcionado."""
    prompt = PromptTemplate(
        input_variables=["text"],
        template="Por favor, genera un resumen conciso y bien estructura del siguiente texto:\n\n{text}\n\nResumen:"
    )
    chain = prompt | llm_groq | StrOutputParser()
    return chain.invoke({"text": text})

# --- Tool 3: Comparador de Documentos ---
@tool
def document_comparison_tool(texts: str) -> str:
    """Compara dos o más fragmentos de texto o conceptos proporcionados en el input."""
    prompt = PromptTemplate(
        input_variables=["texts"],
        template="Compara los siguientes textos o conceptos, destacando similitudes y diferencias clave:\n\n{texts}\n\nComparación:"
    )
    chain = prompt | llm_groq | StrOutputParser()
    return chain.invoke({"texts": texts})

# --- Tool 4: Consulta General LLM ---
@tool
def general_llm_query_tool(query: str) -> str:
    """Responde preguntas de conocimiento general que no requieren acceso a documentos específicos."""
    prompt = PromptTemplate(
        input_variables=["query"],
        template="Responde a la siguiente pregunta de manera clara y profesional:\n\nPregunta: {query}\n\nRespuesta:"
    )
    chain = prompt | llm_groq | StrOutputParser()
    return chain.invoke({"query": query})

# --- Tool 5: Logger de Trazabilidad ---
@tool
def trazability_logger_tool(log_entry: str) -> str:
    """Registra una entrada en el log de trazabilidad del sistema."""
    try:
        entry = {
            "timestamp": datetime.datetime.now().isoformat(),
            "log": log_entry
        }
        
        # Leer logs existentes
        if os.path.exists(LOGS_FILE):
            with open(LOGS_FILE, 'r', encoding='utf-8') as f:
                logs = json.load(f)
        else:
            logs = []
        
        logs.append(entry)
        
        # Escribir logs actualizados
        with open(LOGS_FILE, 'w', encoding='utf-8') as f:
            json.dump(logs, f, indent=4, ensure_ascii=False)
            
        return "Log registrado exitosamente."
    except Exception as e:
        return f"Error al registrar log: {e}"

# Lista de herramientas exportables
custom_tools = [
    semantic_search_tool,
    document_summarizer_tool,
    document_comparison_tool,
    general_llm_query_tool,
    trazability_logger_tool
]
