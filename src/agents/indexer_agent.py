import os
import sys

# Ajustar path para importar módulos src
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import time
from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from src.config import DOCUMENTS_DIR, VECTOR_STORE_DIR, GOOGLE_API_KEY, INDEX_NAME

class IndexerAgent:
    def __init__(self):
        self.documents_dir = DOCUMENTS_DIR
        self.vector_store_dir = VECTOR_STORE_DIR
        self.index_name = INDEX_NAME
        
        # Inicializar Embeddings (usando Gemini/Google)
        if not GOOGLE_API_KEY:
            raise ValueError("GOOGLE_API_KEY no encontrada en variables de entorno.")
        
        self.embeddings = GoogleGenerativeAIEmbeddings(
            model="models/embedding-001",
            google_api_key=GOOGLE_API_KEY,
            model_kwargs={"transport": "grpc"}
        )


    def load_documents(self):
        print(f"Cargando documentos desde {self.documents_dir}...")
        documents = []
        import glob
        from tqdm import tqdm

        # Buscar todos los PDFs manualmente
        pdf_files = glob.glob(os.path.join(self.documents_dir, "**/*.pdf"), recursive=True)
        print(f"Se encontraron {len(pdf_files)} archivos PDF.")

        for file_path in tqdm(pdf_files, desc="Procesando archivos"):
            try:
                loader = PyPDFLoader(file_path)
                # Cargar página por página para tener más control
                docs = loader.load()
                documents.extend(docs)
            except Exception as e:
                # Si falla un archivo, lo imprimimos pero NO detenemos todo el proceso
                print(f"\n[ADVERTENCIA] Error al leer archivo: {os.path.basename(file_path)}")
                print(f"Motivo: {e}")
                continue

        print(f"Se cargaron exitosamente {len(documents)} páginas de documentos.")
        if len(documents) == 0:
            print("No se pudo cargar ningún documento válido. Revisa tus archivos.")
        return documents

    def split_documents(self, documents):
        print("Dividiendo documentos en fragmentos (chunks)...")
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            add_start_index=True
        )
        chunks = text_splitter.split_documents(documents)
        print(f"Se generaron {len(chunks)} fragmentos.")
        return chunks

    def create_vector_store(self, chunks):
        print("Creando almacén vectorial FAISS...")
        print("Generando embeddings (esto puede tardar varios minutos)...")
        try:
            # Procesar en batches con barra de progreso
            batch_size = 100
            total_batches = (len(chunks) + batch_size - 1) // batch_size
            
            # Crear vector store con el primer batch
            first_batch = chunks[:batch_size]
            vector_store = FAISS.from_documents(first_batch, self.embeddings)
            
            # Procesar batches restantes con progreso
            from tqdm import tqdm
            for i in tqdm(range(batch_size, len(chunks), batch_size), 
                         desc="Procesando embeddings",
                         initial=1,
                         total=total_batches):
                batch = chunks[i:i+batch_size]
                batch_store = FAISS.from_documents(batch, self.embeddings)
                vector_store.merge_from(batch_store)
                time.sleep(2)  # Delay para respetar rate limits
            
            # Guardar el índice
            save_path = os.path.join(self.vector_store_dir, self.index_name)
            vector_store.save_local(save_path)
            print(f"Almacén vectorial guardado en {save_path}")
            return vector_store
        except Exception as e:
            print(f"Error creando el almacén vectorial: {e}")
            raise e

    def run(self):
        print("Verificación de Directorio:")
        if not os.path.exists(self.documents_dir):
            print(f"Error: El directorio de documentos {self.documents_dir} no existe.")
            return

        start_time = time.time()
        docs = self.load_documents()
        if not docs:
            print("No se encontraron documentos.")
            return

        chunks = self.split_documents(docs)
        self.create_vector_store(chunks)
        end_time = time.time()
        print(f"Indexación completada en {end_time - start_time:.2f} segundos.")

if __name__ == "__main__":
    agent = IndexerAgent()
    agent.run()
