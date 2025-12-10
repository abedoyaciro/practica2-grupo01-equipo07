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
            user_input = input("\n>> Ingresa tu consulta: ").strip()
        
            if user_input.lower() in ["salir", "exit", "quit"]:
                print("Hasta luego.")
                break
            
            if not user_input:
                print("Por favor ingresa una consulta válida.")
                continue
            
            try:
                response = orchestrator.run_flow(user_input)
                print(f"\n{'='*50}")
                print("RESPUESTA:")
                print(f"{'='*50}")
                print(response)
            except Exception as e:
                error_msg = str(e)
                if "rate_limit" in error_msg.lower() or "429" in error_msg:
                    print("\n[AVISO] Límite de uso de Groq alcanzado.")
                    print("Espera unos minutos o considera usar el modelo gratuito alternativo.")
                    print("Detalles del error:")
                    # Extraer tiempo de espera si está disponible
                    import re
                    wait_time = re.search(r'try again in ([\d\.]+[msh])', error_msg)
                    if wait_time:
                        print(f"Tiempo de espera sugerido: {wait_time.group(1)}")
                else:
                    print(f"\nOcurrió un error inesperado: {e}")
        except KeyboardInterrupt:
            print("\nOperación cancelada por el usuario.")
            break
        except Exception as e:
            print(f"\nOcurrió un error inesperado: {e}")

if __name__ == "__main__":
    main()
