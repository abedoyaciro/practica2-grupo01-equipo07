import os
import sys

# Ajustar path para importar módulos src
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from src.config import GROQ_API_KEY

class RagResponseAgent:
    def __init__(self):
        # Inicializar Groq para generación rápida de respuestas
        self.llm = ChatGroq(
            model_name="llama3-70b-8192",
            temperature=0.3, # Ligera creatividad pero controlada
            groq_api_key=GROQ_API_KEY
        )

        self.prompt_template = PromptTemplate(
            input_variables=["query", "context"],
            template="""
            Eres un asistente experto en Finanzas Cuantitativas.
            Tu tarea es responder a la pregunta del usuario BASÁNDOTE ÚNICAMENTE en el contexto proporcionado.
            
            Reglas:
            1. Usa el contexto para responder. Si la respuesta no está en el contexto, dilo claramente.
            2. Menciona la fuente (nombre del documento) cuando sea posible (usando la información del contexto).
            3. Sé profesional, claro y conciso.
            4. Responde siempre en Español.

            --- Contexto ---
            {context}
            ----------------

            Pregunta: {query}

            Respuesta:
            """
        )
        self.chain = self.prompt_template | self.llm | StrOutputParser()

    def generate_response(self, query: str, context: str) -> str:
        """Genera una respuesta RAG."""
        print(f"--- [Agente RAG] Generando respuesta... ---")
        response = self.chain.invoke({"query": query, "context": context})
        return response.strip()
