import os
import sys

# Ajustar path para importar módulos src
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.output_parsers import StrOutputParser
from src.config import GOOGLE_API_KEY

class EvaluatorAgent:
    def __init__(self):
        # Inicializar Gemini para razonamiento crítico y validación
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
            temperature=0,
            google_api_key=GOOGLE_API_KEY
        )

        self.prompt_template = PromptTemplate(
            input_variables=["query", "context", "response"],
            template="""
            Actúa como un crítico y evaluador riguroso.
            Tienes la siguiente tríada: Pregunta, Contexto, Respuesta Generada.

            Pregunta: {query}
            
            Contexto:
            {context}
            
            Respuesta Generada:
            {response}

            Evalúa lo siguiente:
            1. ¿La respuesta responde a la pregunta?
            2. ¿La información de la respuesta está respaldada por el contexto (no hay alucinaciones)?
            3. ¿Es coherente y está en español?

            Si la respuesta cumple todo, responde con "APROBADO".
            Si falla en algo, responde con "RECHAZADO" seguido de una breve explicación del por qué.
            """
        )
        self.chain = self.prompt_template | self.llm | StrOutputParser()

    def evaluate(self, query: str, context: str, response: str) -> str:
        """Evalúa la calidad de la respuesta."""
        print(f"--- [Evaluador] Verificando respuesta... ---")
        evaluation = self.chain.invoke({"query": query, "context": context, "response": response})
        print(f"--- [Evaluador] Resultado: {evaluation} ---")
        return evaluation.strip()
