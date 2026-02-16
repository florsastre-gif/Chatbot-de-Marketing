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
        "¿En qué situación estás hoy?",
        ["Solo tengo curiosidad", "Tengo un negocio propio", "Manejo las redes", "Quiero ofrecer servicios"]
    )

# Cuerpo
st.title("SPRING AI SHIFT™")
st.markdown("##### Estrategia + Educación + Tecnología")

st.markdown('<div class="main-card">', unsafe_allow_html=True)
col_izq, col_der = st.columns([1, 1], gap="large")

with col_izq:
    st.write("**Describí el problema acá:**")
    consulta = st.text_area("Entrada:", placeholder="Ej: ¿Cómo mejoro mis ventas?", height=200, label_visibility="collapsed")
    boton_ejecutar = st.button("OBTENER CLARIDAD")

with col_der:
    st.write("**Tu Hoja de Ruta de Claridad:**")
    if boton_ejecutar:
        if not api_key_input:
            st.error("Falta la API Key en la barra lateral.")
        else:
            with st.spinner("Procesando..."):
                try:
                    # CONFIGURACIÓN CORRECTA PARA EVITAR 404
                    genai.configure(api_key=api_key_input)
                    
                    # Quitamos el prefijo 'models/' y usamos solo el nombre
                    model = genai.GenerativeModel('gemini-1.5-flash')
                    
                    prompt = f"Como mentor experto para alguien que '{perfil}', explica: {consulta}."
                    
                    # Llamada directa al modelo estable
                    response = model.generate_content(prompt)
                    
                    if response:
                        st.markdown(response.text)
                except Exception as e:
                    st.error(f"Error técnico: {e}")
                    st.info("Sugerencia: Esperá 2 minutos o verificá que la API Key sea la de Project1.")
    else:
        st.caption("Esperando tu consulta...")
st.markdown('</div>', unsafe_allow_html=True)
