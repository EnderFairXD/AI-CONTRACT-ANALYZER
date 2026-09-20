import streamlit as st
import re
from utils.pdf_parser import extract_text_from_pdf
from services.ai_service import analyze_contract

st.set_page_config(page_title="Analizador de Contratos IA", page_icon="⚖️", layout="wide")

st.title("⚖️ Analizador de Contratos con IA (Local y Privado)")
st.markdown("Sube un contrato en PDF. El documento **nunca saldrá de tu red local**, garantizando 100% de privacidad.")

uploaded_file = st.file_uploader("Sube tu contrato (PDF)", type="pdf")

if uploaded_file is not None:
    st.info("📄 PDF cargado correctamente en memoria.")
    
    if st.button("🚀 Iniciar Análisis de Riesgos"):
        
        # Usamos st.status para mostrar un progreso paso a paso
        with st.status("Procesando el documento...", expanded=True) as status:
            try:
                st.write("Extraeciendo texto del PDF...")
                raw_text = extract_text_from_pdf(uploaded_file)
                
                if not raw_text.strip():
                    status.update(label="Error en la lectura", state="error", expanded=True)
                    st.error("El PDF está vacío o es una imagen escaneada sin OCR.")
                else:
                    # 🔧 TOQUE SENIOR: Limpieza básica de texto para ahorrar tokens
                    st.write("Optimizando texto (eliminando espacios muertos)...")
                    clean_text = re.sub(r'\n+', '\n', raw_text) # Quita saltos de línea dobles
                    clean_text = re.sub(r'\s+', ' ', clean_text) # Quita espacios múltiples
                    
                    st.write("Enviando al servidor local (Ollama) para análisis legal. Esto puede tardar...")
                    
                    # Llamada a la IA
                    resultado = analyze_contract(clean_text)
                    
                    status.update(label="¡Análisis completado con éxito!", state="complete", expanded=False)
                    
                    # Mostrar resultados
                    st.markdown("---")
                    st.markdown("### 📋 Informe Legal IA")
                    st.markdown(resultado)
                    
            except Exception as e:
                status.update(label="Ocurrió un error", state="error", expanded=True)
                st.error(f"Error técnico: {str(e)}")