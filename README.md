# Analizador de Contratos IA (Local)

Una aplicación web construida con Streamlit y LangChain que utiliza modelos locales a través de Ollama para analizar contratos legales en PDF, garantizando un 100% de privacidad sin enviar datos a la nube.

## Requisitos Previos
1. Instalar [Python 3.9+](https://www.python.org/)
2. Instalar [Ollama](https://ollama.com/) y mantenerlo ejecutándose en segundo plano.
3. Descargar el modelo base ejecutando en tu terminal: `ollama run llama3.1`

## Instalación y Ejecución
1. Clona el repositorio: `git clone <tu-enlace-aqui>`
2. Crea un entorno virtual: `python -m venv .venv`
3. Activa el entorno virtual: 
   * Windows: `.venv\Scripts\activate` 
   * Mac/Linux: `source .venv/bin/activate`
4. Instala las dependencias: `pip install -r requirements.txt`
5. Copia la plantilla de variables: `cp .env.example .env`
6. Inicia la aplicación: `streamlit run src/main.py`