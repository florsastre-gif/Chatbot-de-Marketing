import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
st.set_page_config(page_title="SPRING AI SHIFT", page_icon="🌱", layout="wide")

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
        border: none;
    }
    .stButton>button:hover {
        background-color: #4CAF50;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

with st.sidebar:
    st.title("🌱 Configuración")
    api_key_input = st.text_input("Tu Gemini API Key:", type="password", placeholder="...")
    st.divider()
    perfil = st.selectbox(
        "¿Situación actual?",
        ["Curiosidad", "Negocio propio", "Redes sociales", "Ofrecer servicios"]
    )

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
            st.error("⚠️ Falta la API Key en la barra lateral.")
        elif not consulta:
            st.warning("Por favor, escribí una consulta.")
        else:
            with st.spinner("Procesando..."):
                try:
                    genai.configure(api_key=api_key_input)
                    model = genai.GenerativeModel('gemini-1.5-flash')
                    
                    prompt = f"Actúa como un mentor experto para alguien que está en esta situación: {perfil}. Tu objetivo es explicar este tema de forma simple y accionable: {consulta}. Responde con: 1. LA IDEA CENTRAL, 2. ANALOGÍA, 3. ROADMAP de 3 pasos, 4. REFLEXIÓN."
                    
                    response = model.generate_content(prompt)
                    st.markdown(response.text)
                except Exception as e:
                    st.error(f"Error técnico: {e}")
    else:
        st.caption("Esperando interacción...")
st.markdown('</div>', unsafe_allow_html=True)
