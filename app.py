import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-1.5-pro') # Usando el modelo Pro solicitado

st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: white; }
    .stTextArea textarea { background-color: #262730; color: white; }
    </style>
    """, unsafe_allow_html=True)

#Identidad y Encabezado
st.title("🌱 SPRING AI SHIFT™")
st.write("Estrategia + educación + tecnología")

# 3. Sidebar y Perfiles Personalizados
with st.sidebar:
    st.header("Configuración")
    # Los perfiles que pediste exactamente
    perfil = st.selectbox(
        "¿Cuál es tu situación hoy?",
        [
            "Solo vengo por curiosidad",
            "Tengo un negocio propio",
            "Manejo las redes de un negocio",
            "Quiero aprender para ofrecer servicio"
        ]
    )
    st.info(f"Modo actual: {perfil}")

# 4. Área de Interacción (Clarity Engine)
st.subheader("La IA no piensa por vos, piensa con vos. Empecemos:")
consulta = st.text_area("Escribe tu problema técnico o el dolor de tu empresa acá:", height=150)

if st.button("Obtener Claridad"):
    if consulta:
        with st.spinner("Paciencia :) El motor de SPRING está procesando..."):
            # Prompt directo y con sentido
            prompt = f"Como mentor experto para alguien que '{perfil}', explica de forma simple y accionable: {consulta}"
            
            try:
                response = model.generate_content(prompt)
                st.success("Análisis completado")
                st.markdown("---")
                st.markdown(response.text)
            except Exception as e:
                st.error(f"Error de conexión: {e}")
    else:
        st.warning("Por favor, ingresa un texto para analizar.")

# 5. Secciones de utilidad (Footer con sentido)
st.divider()
col1, col2, col3 = st.columns(3)
with col1:
    st.write("**Redes Sociales**")
    st.caption("Ideal para entender métricas y algoritmos.")
with col2:
    st.write("**Gestión de Negocio**")
    st.caption("Claridad sobre herramientas y procesos.")
with col3:
    st.write("**Servicios**")
    st.caption("Aprende conceptos para tus clientes.")
