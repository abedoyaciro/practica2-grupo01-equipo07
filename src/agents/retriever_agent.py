import os
import sys

# Ajustar path para importar módulos src
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from src.config import GROQ_API_KEY
from src.tools.custom_tools import semantic_search_tool

class RetrieverAgent:
    def __init__(self):
        # Inicializar Groq para velocidad en recuperación
        self.llm = ChatGroq(
            model_name="llama3-70b-8192",
            temperature=0,
            groq_api_key=GROQ_API_KEY
        )

    def retrieve(self, query: str) -> str:
        """Recupera documentos relevantes para la consulta."""
        print(f"--- [Recuperador] Buscando información para: '{query}' ---")
        
        # En este paso podríamos refinar la query con el LLM si fuera necesario,
        # pero para mantener eficiencia usamos la tool directamente.
        
        context = semantic_search_tool.run(query)
        
        if "Error" in context:
            print("--- [Recuperador] Error al acceder a la base vectorial. ---")
            return ""

        print("--- [Recuperador] Contexto recuperado exitosamente. ---")
        return context

if __name__ == "__main__":
    agent = RetrieverAgent()
    # Requiere que el index exista
    # print(agent.retrieve("modelos de riesgo")) 
