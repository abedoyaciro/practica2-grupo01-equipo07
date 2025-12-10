import os
import sys

# Ajustar path para importar módulos src
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from src.agents.classifier_agent import ClassifierAgent
from src.agents.retriever_agent import RetrieverAgent
from src.agents.rag_response_agent import RagResponseAgent
from src.agents.evaluator_agent import EvaluatorAgent
from src.tools.custom_tools import document_summarizer_tool, document_comparison_tool, general_llm_query_tool, trazability_logger_tool
from langchain_groq import ChatGroq
from src.config import GROQ_API_KEY

class OrchestratorAgent:
    def __init__(self):
        # Inicializar LLM propio para decisiones rápidas (Groq)
        self.llm = ChatGroq(
            model_name="llama-3.3-70b-versatile",
            temperature=0,
            groq_api_key=GROQ_API_KEY
        )
        
        # Inicializar agentes
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
            
            # Registrar contexto recuperado con nombres de documentos
            # Extraer nombres de documentos del contexto (nuevo formato: --- [nombre] ---)
            import re
            doc_sources = re.findall(r'--- \[(.+?)\] ---', context)
            doc_sources = list(dict.fromkeys(doc_sources))  # Eliminar duplicados manteniendo orden
            
            fragments_count = len(re.findall(r'--- \[.+?\] ---', context))
            trazability_logger_tool.run(f"Recuperación: {fragments_count} fragmentos de documentos: {', '.join(doc_sources)}")
            
            while not approved and attempts < max_attempts:
                attempts += 1
                trazability_logger_tool.run(f"Generación RAG: Intento {attempts}/{max_attempts}")
                
                # Generar respuesta
                response = self.rag_agent.generate_response(query, context)
                
                # Evaluar
                evaluation = self.evaluator.evaluate(query, context, response)
                
                # Registrar evaluación
                eval_status = "APROBADO" if "APROBADO" in evaluation else "RECHAZADO"
                trazability_logger_tool.run(f"Evaluación: {eval_status}")
                
                if "APROBADO" in evaluation:
                    final_response = response
                    approved = True
                else:
                    if attempts < max_attempts:
                        print(f"[Sistema] Intento {attempts} no aprobado, regenerando...")
                    else:
                        final_response = f"Nota: Esta respuesta puede no ser perfecta.\n\n{response}"
            
            if not approved:
                final_response = "Lo siento, no pude generar una respuesta verificada con el contexto disponible."

        elif intent == "summary":
            # Para resumen, asumimos que se quiere resumir lo que se encuentre relevante
            context = self.retriever.retrieve(query)
            
            # Extraer y registrar documentos usados (nuevo formato)
            import re
            doc_sources = re.findall(r'--- \[(.+?)\] ---', context)
            doc_sources = list(dict.fromkeys(doc_sources))  # Eliminar duplicados
            
            fragments_count = len(re.findall(r'--- \[.+?\] ---', context))
            trazability_logger_tool.run(f"Recuperación para resumen: {fragments_count} fragmentos de: {', '.join(doc_sources)}")
            trazability_logger_tool.run(f"Tool ejecutada: document_summarizer_tool")
            final_response = document_summarizer_tool.run(context)
            
        elif intent == "comparison":
            context = self.retriever.retrieve(query)
            
            # Extraer y registrar documentos usados (nuevo formato)
            import re
            doc_sources = re.findall(r'--- \[(.+?)\] ---', context)
            doc_sources = list(dict.fromkeys(doc_sources))  # Eliminar duplicados
            
            fragments_count = len(re.findall(r'--- \[.+?\] ---', context))
            trazability_logger_tool.run(f"Recuperación para comparación: {fragments_count} fragmentos de: {', '.join(doc_sources)}")
            trazability_logger_tool.run(f"Tool ejecutada: document_comparison_tool")
            final_response = document_comparison_tool.run(context)

        # 4. Trazabilidad Final
        trazability_logger_tool.run(f"Respuesta final generada para intención {intent}")
        
        return final_response
