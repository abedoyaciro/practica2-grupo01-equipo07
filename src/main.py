import sys
import os

# Ajustar path para importar módulos src
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.agents.orchestrator_agent import OrchestratorAgent

def main():
    print("================================================================")
    print(" Sistema Agentic AI - Finanzas Cuantitativas ")
    print("================================================================")
    print("Iniciando componentes...")
    
    try:
        orchestrator = OrchestratorAgent()
        print(">> Sistema listo. Escribe 'salir' para terminar.")
    except Exception as e:
        print(f"Error al iniciar el sistema: {e}")
        print("Verifica tu archivo .env y las API Keys.")
        return

    while True:
        try:
            query = input("\n>> Ingresa tu consulta: ")
            if query.lower() in ["salir", "exit", "quit"]:
                print("Hasta luego.")
                break
            
            if not query.strip():
                continue

            print("\nProcesando consulta...")
            response = orchestrator.run_flow(query)
            
            print("\n" + "-"*60)
            print("RESPUESTA DEL SISTEMA:")
            print("-"*60)
            print(response)
            print("-"*60)
            
        except KeyboardInterrupt:
            print("\nOperación cancelada por el usuario.")
            break
        except Exception as e:
            print(f"\nOcurrió un error inesperado: {e}")

if __name__ == "__main__":
    main()
