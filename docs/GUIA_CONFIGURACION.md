# Guía de Configuración y Obtención de API Keys

Este documento explica cómo obtener las credenciales necesarias para ejecutar el proyecto y cómo configurar el entorno.

## 1. Obtención de API Keys

### Google Gemini API Key
Para utilizar los modelos de Google (Gemini Pro) y los Embeddings:
1.  Ve a [Google AI Studio](https://aistudio.google.com/).
2.  Inicia sesión con tu cuenta de Google.
3.  Haz clic en **"Get API key"** (Obtener clave API).
4.  Haz clic en **"Create API key in new project"** (Crear clave API en proyecto nuevo).
5.  Copia la clave generada (empieza por `AIza...`).

### Groq API Key
Para utilizar los modelos rápidos de Groq (Llama 3, Mixtral, etc.):
1.  Ve a [Groq Cloud Console](https://console.groq.com/keys).
2.  Inicia sesión (puedes usar GitHub o Google).
3.  Ve a la sección **"API Keys"**.
4.  Haz clic en **"Create API Key"**.
5.  Asigna un nombre (ej. `ProyectoPLN`).
6.  Copia la clave generada (empieza por `gsk_...`).

## 2. Configuración del Entorno (.env)

Crea un archivo llamado `.env` en la raíz del proyecto (`practica2-grupo01-equipo07/.env`) y agrega las claves que copiaste:

```env
GOOGLE_API_KEY=tu_clave_de_google_aqui
GROQ_API_KEY=tu_clave_de_groq_aqui
```

**Nota:** No compartas este archivo `.env` ni lo subas a repositorios públicos.

## 3. Instalación de Dependencias

Asegúrate de tener Python 3.10+ instalado. Ejecuta en tu terminal:

```bash
pip install -r requirements.txt
```

## 4. Estructura de Carpetas

Asegúrate de que tus documentos PDF estén en `data/documents/`. El sistema buscará recursivamente archivos `.pdf` en esa carpeta.
