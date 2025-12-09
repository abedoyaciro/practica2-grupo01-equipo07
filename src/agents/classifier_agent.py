import os
import sys

# Ajustar path para importar módulos src
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from src.config import GOOGLE_API_KEY

class ClassifierAgent:
    def __init__(self):
        # Inicializar Gemini para clasificación (Modelo Pro para razonamiento)
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
            temperature=0,
            google_api_key=GOOGLE_API_KEY
        )

        self.prompt_template = PromptTemplate(
            input_variables=["query"],
            template="""
            Eres un experto en clasificación de intenciones para un sistema de análisis de documentos financieros.
            Analiza la siguiente consulta del usuario y clasifícala en una de las siguientes categorías:

            1. **search**: El usuario busca hechos específicos, datos numéricos o definiciones contenidas en los documentos.
            2. **summary**: El usuario pide explícitamente un resumen o síntesis de uno o varios documentos.
            3. **comparison**: El usuario pide comparar dos o más conceptos, metodologías o documentos.
            4. **general**: La consulta es un saludo, una pregunta de conocimiento general fuera del dominio financiero específico, o no requiere acceso a los documentos.

            Consulta: "{query}"

            Responde ÚNICAMENTE con la palabra de la categoría (search, summary, comparison, general). No añadas explicaciones.
            """
        )
        self.chain = self.prompt_template | self.llm | StrOutputParser()

    def classify(self, query: str) -> str:
        """Clasifica la consulta del usuario."""
        print(f"--- [Clasificador] Analizando intención para: '{query}' ---")
        response = self.chain.invoke({"query": query})
        intent = response.strip().lower()
        
        # Validación básica
        valid_intents = ["search", "summary", "comparison", "general"]
        if intent not in valid_intents:
            print(f"Advertencia: Intención desconocida '{intent}', se usará 'general'.")
            return "general"
            
        print(f"--- [Clasificador] Intención detectada: {intent} ---")
        return intent

if __name__ == "__main__":
    # Prueba rápida
    agent = ClassifierAgent()
    print(agent.classify("¿Qué es el CAPM?"))
    print(agent.classify("Resume el documento de riesgo de liquidez."))
    print(agent.classify("Hola, ¿cómo estás?"))
