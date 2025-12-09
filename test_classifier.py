from src.agents.classifier_agent import ClassifierAgent
from dotenv import load_dotenv
load_dotenv()

agent = ClassifierAgent()
print("Test 1 (search):", agent.classify("¿Qué es el riesgo de mercado?"))
print("Test 2 (general):", agent.classify("Hola, buenos días."))