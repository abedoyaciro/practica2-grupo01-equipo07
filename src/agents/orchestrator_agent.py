import os
import sys

# Ajustar path para importar módulos src
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from src.agents.classifier_agent import ClassifierAgent
from src.agents.retriever_agent import RetrieverAgent
from src.agents.rag_response_agent import RagResponseAgent
from src.agents.evaluator_agent import EvaluatorAgent
from src.tools.custom_tools import document_summarizer_tool, document_comparison_tool, general_llm_query_tool, trazability_logger_tool

class OrchestratorAgent:
    def __init__(self):
        self.classifier = ClassifierAgent()
        self.retriever = RetrieverAgent()
        self.rag_agent = RagResponseAgent()
        self.evaluator = EvaluatorAgent()
        
    def run_flow(self, query: str):
        """Ejecuta el flujo principal del sistema."""
        print(f"\n{'='*50}")
        print(f"Nueva Consulta: {query}")
        print(f"{'='*50}\n")
        
        # 1. Trazabilidad Inicial
        trazability_logger_tool.run(f"Inicio de consulta: {query}")

        # 2. Clasificación
        intent = self.classifier.classify(query)
        trazability_logger_tool.run(f"Intención clasificada: {intent}")

        final_response = ""

        # 3. Enrutamiento
        if intent == "general":
            final_response = general_llm_query_tool.run(query)
            
        elif intent == "search":
            # Flujo RAG completo con Evaluación
            attempts = 0
            max_attempts = 2
            approved = False
            
            context = self.retriever.retrieve(query)
            
            while not approved and attempts < max_attempts:
                # Generar respuesta
                response = self.rag_agent.generate_response(query, context)
                
                # Evaluar
                evaluation = self.evaluator.evaluate(query, context, response)
                
                if "APROBADO" in evaluation:
                    final_response = response
                    approved = True
                else:
                    print(f"Intento {attempts+1} fallido. Razón: {evaluation}")
                    # En una implementación más compleja, aquí se podría pedir regenerar con feedback
                    # Por simplicidad, si falla 2 veces, devolvemos la última respuesta con una advertencia.
                    final_response = f"Nota: Esta respuesta puede no ser perfecta.\n\n{response}"
                    attempts += 1
            
            if not approved:
                final_response = "Lo siento, no pude generar una respuesta verificada con el contexto disponible."

        elif intent == "summary":
            # Para resumen, asumimos que se quiere resumir lo que se encuentre relevante
            # Ojo: Si la query no especifica documento, busca los más relevantes y los resume.
            context = self.retriever.retrieve(query)
            final_response = document_summarizer_tool.run(context)
            
        elif intent == "comparison":
            context = self.retriever.retrieve(query)
            final_response = document_comparison_tool.run(context)

        # 4. Trazabilidad Final
        trazability_logger_tool.run(f"Respuesta final generada para intención {intent}")
        
        return final_response
