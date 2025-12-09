import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# API Key de Google Gemini
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# API Key de Groq
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Rutas Base
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(BASE_DIR)

# Rutas de Datos
DOCUMENTS_DIR = os.path.join(PROJECT_ROOT, "data", "documents")
VECTOR_STORE_DIR = os.path.join(PROJECT_ROOT, "data", "vector_store")
OUTPUT_DIR = os.path.join(PROJECT_ROOT, "output")
LOGS_FILE = os.path.join(OUTPUT_DIR, "trazabilidad_logs.json")

# Nombre del Índice FAISS
INDEX_NAME = "financial_docs_index"
