import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Configuración básica
load_dotenv()
st.set_page_config(page_title="SPRING AI SHIFT", page_icon="🌱", layout="wide")

# Estilos (CSS)
st.markdown("""
    <style>
    .stApp { background-color: #0d0d0d; color: #f0f0f0; }
    [data-testid="stSidebar"] { background-color: #111111; }
    .main-card {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 20px;
        padding: 30px;
        margin-bottom: 25px;
    }
    .stButton>button {
        width: 100%;
        border-radius: 12px;
        height: 3em;
        background-color: #ffffff;
        color: #000000;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.title("🌱 Configuración")
    api_key_input = st.text_input("Tu Gemini API Key:", type="password")
    st.divider()
    perfil = st.selectbox(
        "Situación actual:",
        ["Curiosidad", "Negocio propio", "Redes sociales", "Ofrecer servicios"]
    )

# Cuerpo principal
st.title("SPRING AI SHIFT™")
st.markdown("##### Estrategia + Educación + Tecnología")

st.markdown('<div class="main-card">', unsafe_allow_html=True)
col_izq, col_der = st.columns([1, 1], gap="large")

with col_izq:
    st.write("**Escribí tu consulta:**")
    consulta = st.text_area("Entrada:", placeholder="Ej: ¿Cómo mejoro mis ventas?", height=200, label_visibility="collapsed")
    boton_ejecutar = st.button("OBTENER CLARIDAD")

with col_der:
    st.write("**Tu Hoja de Ruta:**")
    if boton_ejecutar:
        if not api_key_input:
            st.error("Falta la API Key en la barra lateral.")
        elif not consulta:
            st.warning("Escribí algo primero.")
        else:
            with st.spinner("Procesando..."):
                try:
                    # Configuración manual de la API
                    genai.configure(api_key=api_key_input)
                    
                    # Definición del modelo (Aquí estaba el NameError)
                    model = genai.GenerativeModel('gemini-1.5-flash')
                    
                    # Generación de contenido
                    response = model.generate_content(
                        f"Como mentor para un perfil de '{perfil}', explica: {consulta}"
                    )
                    
                    if response.text:
                        st.markdown(response.text)
                except Exception as e:
                    st.error(f"Error técnico: {e}")
    else:
        st.caption("Esperando consulta...")
st.markdown('</div>', unsafe_allow_html=True)
