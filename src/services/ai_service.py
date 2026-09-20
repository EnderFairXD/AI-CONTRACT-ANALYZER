import os
from dotenv import load_dotenv
from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate

load_dotenv()

def analyze_contract(contract_text: str) -> str:
    """Envía el texto del contrato a tu servidor local de Ollama."""
    
    base_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
    
    # 🔧 TOQUE SENIOR: Aumentamos el num_ctx a 8192 (aprox 6000 palabras / 12 páginas).
    # Si tu servidor tiene mucha RAM/VRAM, puedes subirlo a 16384 o 32768.
    llm = Ollama(
        base_url=base_url,
        model="llama3.1", # o "mistral"
        temperature=0.2,
        num_ctx=8192 
    )
    
    template = """
    Eres un abogado experto y analista de riesgos. Analiza el siguiente contrato y proporciona un informe estructurado en Markdown con las siguientes secciones en español:
    
    1. **Resumen automático**: Un resumen de 3-4 líneas sobre de qué trata el contrato.
    2. **Cláusulas importantes**: Viñetas con las 3 o 4 cláusulas más críticas.
    3. **Riesgos potenciales**: Identifica cualquier trampa, penalización o riesgo oculto para las partes.
    4. **Explicación en lenguaje sencillo**: Explica el contrato como si se lo estuvieras contando a un adolescente de 15 años.

    Texto del contrato:
    {texto}
    """
    
    prompt = PromptTemplate(input_variables=["texto"], template=template)
    chain = prompt | llm
    
    return chain.invoke({"texto": contract_text})