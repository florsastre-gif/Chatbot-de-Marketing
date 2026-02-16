import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Configuración inicial
load_dotenv()
st.set_page_config(page_title="SPRING AI SHIFT", page_icon="🌱", layout="wide")

# Diseño de Interfaz (CSS)
st.markdown("""
    <style>
    .stApp { background-color: #0d0d0d; color: #e0e0e0; }
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

# --- BARRA LATERAL (Sidebar) ---
with st.sidebar:
    st.title("🌱 Configuración")
    
    # Campo para que la profesora ingrese su propia clave
    api_key_input = st.text_input(
        "Hola :) Introducí tu Gemini API Key acá:", 
        type="password",
        help="Conseguí tu llave en aistudio.google.com"
    )
    
    st.divider()
    
    # Perfiles personalizados solicitados
    perfil = st.selectbox(
        "¿Cuál es tu situación hoy?",
        [
            "Solo tengo curiosidad",
            "Tengo un negocio propio",
            "Manejo las redes de un negocio",
            "Quiero aprender para ofrecer servicio"
        ]
    )
    st.info(f"Modo: {perfil}")

# --- CUERPO PRINCIPAL ---
st.title("SPRING AI SHIFT™")
st.markdown("##### Estrategia + educación + tecnología")
st.markdown("### La IA no piensa por vos, piensa con vos. Empecemos:")

st.markdown('<div class="main-card">', unsafe_allow_html=True)
col_izq, col_der = st.columns([1, 1], gap="large")

with col_izq:
    st.write("**Escribí tu problema técnico o el dolor de tu empresa acá:**")
    consulta = st.text_area(
        "Ingreso de datos:", 
        placeholder="Ej: Necesito más clientes para mi local de yoga...", 
        height=200,
        label_visibility="collapsed"
    )
    
    boton_ejecutar = st.button("Obtener Claridad")

with col_der:
    st.write("**Tu Hoja de Ruta de Claridad:**")
    
    if boton_ejecutar:
        if not api_key_input:
            st.error("⚠️ Falta la API Key en la barra lateral.")
        elif not consulta:
            st.warning("Por favor, escribí una consulta para procesar.")
        else:
            with st.spinner("Paciencia :) El motor de SPRING está procesando..."):
                try:
                    # Configuración dinámica del modelo
                    genai.configure(api_key=api_key_input)
                    model = genai.GenerativeModel('gemini-1.5-flash')                    
                    # Prompt estructurado con identidad SPRING
                    prompt_final = f"""
                    Actúa como un mentor experto para alguien que está en esta situación: {perfil}.
                    Tu objetivo es explicar este tema de forma simple y accionable: {consulta}
                    
                    Responde siguiendo este esquema:
                    1. LA IDEA CENTRAL: Explicación sin tecnicismos.
                    2. ANALOGÍA: Un ejemplo físico relacionado con el perfil '{perfil}'.
                    3. ROADMAP: 3 pasos concretos para accionar hoy.
                    4. REFLEXIÓN: Una pregunta para validar el entendimiento.
                    """
                    
                    response = model.generate_content(prompt_final)
                    st.markdown(response.text)
                    
                except Exception as e:
                    st.error(f"Error técnico: {e}")
    else:
        st.caption("Esperando interacción...")
st.markdown('</div>', unsafe_allow_html=True)

# --- SECCIONES INFORMATIVAS ---
st.divider()
c1, c2, c3 = st.columns(3)
with c1:
    st.markdown("**Redes Sociales**")
    st.caption("Ideal para entender métricas y algoritmos.")
with c2:
    st.markdown("**Gestión de Negocio**")
    st.caption("Claridad sobre herramientas y procesos.")
with c3:
    st.markdown("**Servicios**")
    st.caption("Aprende conceptos para tus clientes.")
