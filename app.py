import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Configuración básica del sitio
load_dotenv()
st.set_page_config(page_title="SPRING AI SHIFT", page_icon="🌱", layout="wide")

# Estilos visuales
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

# Panel de configuración lateral
with st.sidebar:
    st.title("🌱 Configuración")
    
    # Campo para la API Key
    api_key_input = st.text_input(
        "Tu Gemini API Key:", 
        type="password",
        placeholder="Pega aquí tu clave AIza..."
    )
    
    st.divider()
    
    # Selector de perfil de usuario
    perfil = st.selectbox(
        "¿En qué situación estás hoy?",
        [
            "Solo tengo curiosidad",
            "Tengo un negocio propio",
            "Manejo las redes de un negocio",
            "Quiero aprender para ofrecer servicios"
        ]
    )
    st.info(f"Modo: {perfil}")

# Estructura principal de la aplicación
st.title("SPRING AI SHIFT™")
st.markdown("##### Estrategia + Educación + Tecnología")
st.markdown("### La IA no piensa por vos, piensa con vos. Empecemos:")

st.markdown('<div class="main-card">', unsafe_allow_html=True)
col_izq, col_der = st.columns([1, 1], gap="large")

with col_izq:
    st.write("**Describí el concepto técnico o el problema de tu negocio acá:**")
    consulta = st.text_area(
        "Entrada de datos:", 
        placeholder="Ej: ¿Cómo consigo más clientes para mi academia?", 
        height=200,
        label_visibility="collapsed"
    )
    
    boton_ejecutar = st.button("OBTENER CLARIDAD")

with col_der:
    st.write("**Tu Hoja de Ruta de Claridad:**")
    
    if boton_ejecutar:
        if not api_key_input:
            st.error("⚠️ Por favor, ingresá la API Key en la barra lateral.")
        elif not consulta:
            st.warning("Por favor, escribí algo para analizar.")
        else:
            with st.spinner("Paciencia :) El motor de SPRING está procesando..."):
                try:
                    # Configuración y ejecución del modelo
                    genai.configure(api_key=api_key_input)
                    model = genai.GenerativeModel('gemini-1.5-flash')
                    
                    prompt_final = f"""
                    Eres el mentor de SPRING AI SHIFT™. Da claridad estratégica en español.
                    Situación del usuario: {perfil}.
                    Tema a explicar: {consulta}
                    
                    Responde siguiendo este esquema:
                    1. LA VERDAD: Explicación directa y sin tecnicismos.
                    2. EL PUENTE: Una analogía comprensible para alguien que '{perfil}'.
                    3. PASOS A SEGUIR: 3 acciones concretas para hoy.
                    4. PREGUNTA DE PODER: Una reflexión final.
                    """
                    
                    response = model.generate_content(prompt_final)
                    st.markdown(response.text)
                    
                except Exception as e:
                    st.error(f"Error técnico: {e}")
                    st.info("Revisá que tu API Key sea la correcta y pertenezca a un proyecto activo.")
    else:
        st.caption("Esperando tu consulta...")
st.markdown('</div>', unsafe_allow_html=True)

# Footer informativo
st.divider()
c1, c2, c3 = st.columns(3)
with c1:
    st.markdown("**Redes Sociales**")
    st.caption("Entendé métricas y algoritmos para crecer.")
with c2:
    st.markdown("**Gestión de Negocio**")
    st.caption("Optimizá tus procesos con herramientas digitales.")
with c3:
    st.markdown("**Servicios**")
    st.caption("Dominá la terminología para vender mejor.")
