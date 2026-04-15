import streamlit as st

st.set_page_config(page_title="Enciclopedia Universal de Ciencias", layout="wide")

# --- ESTILOS VISUALES (CSS) ---
st.markdown("""
    <style>
    .titulo-principal { color: #1e3a8a; font-size: 45px; font-weight: bold; border-bottom: 4px solid #3b82f6; }
    .texto-profundo { font-size: 19px; line-height: 2.0; text-align: justify; color: #1a202c; padding: 15px; }
    .caja-ley { background-color: #f8fafc; border: 2px solid #cbd5e1; padding: 30px; border-radius: 12px; margin: 25px 0; }
    .subtitulo-profundo { color: #1e40af; font-size: 28px; font-weight: bold; margin-top: 35px; border-left: 8px solid #1e40af; padding-left: 15px; }
    .paso-a-paso { background-color: #f0fdf4; border-left: 5px solid #16a34a; padding: 20px; margin: 20px 0; font-family: 'Courier New', Courier, monospace; }
    </style>
    """, unsafe_allow_html=True)

# --- MENÚ LATERAL ---
st.sidebar.title("📚 Menú de Ingeniería")
tomo = st.sidebar.selectbox("Seleccionar Tomo:", ["Tomo I: Aritmética Profunda", "Tomo II: Álgebra", "Tomo III: Física", "Tomo IV: Química"])

if tomo == "Tomo I: Aritmética Profunda":
    st.markdown("<div class='titulo-principal'>Tomo I: Aritmética y Fundamentos Lógicos</div>", unsafe_allow_html=True)
    
    capitulo = st.sidebar.radio("Capítulos:", [
        "1.1 Los Signos y la Lógica Operativa", 
        "1.2 Fracciones, Decimales y Porcentajes",
        "1.3 Potencias, Raíces y Logaritmos",
        "1.4 Jerarquía de Operaciones",
        "1.5 Proporcionalidad"
    ])

    # --- CONTENIDO 1.1 ---
    if capitulo == "1.1 Los Signos y la Lógica Operativa":
        st.markdown("<div class='subtitulo-profundo'>1.1 El Dominio de los Signos</div>", unsafe_allow_html=True)
        st.write("### I. La Dualidad de los Números")
        st.markdown("<div class='caja-ley'>", unsafe_allow_html=True)
        st.latex(r"a + (-a) = 0")
        st.latex(r"(-) \cdot (-) = (+)")
        st.markdown("</div>", unsafe_allow_html=True)

    # --- CONTENIDO 1.2 ---
    elif capitulo == "1.2 Fracciones, Decimales y Porcentajes":
        st.markdown("<div class='subtitulo-profundo'>1.2 Racionales y Proporciones</div>", unsafe_allow_html=True)
        st.markdown("<div class='caja-ley'>", unsafe_allow_html=True)
        st.latex(r"\frac{a}{b} \cdot \frac{c}{d} = \frac{ac}{bd}")
        st.markdown("</div>", unsafe_allow_html=True)

    # --- CONTENIDO 1.3 (ESTE ES EL QUE FALTABA AMPLIAR) ---
    elif capitulo == "1.3 Potencias, Raíces y Logaritmos":
        st.markdown("<div class='subtitulo-profundo'>1.3 Operaciones de Orden Superior</div>", unsafe_allow_html=True)
        
        st.markdown("<div class='texto-profundo'>", unsafe_allow_html=True)
        st.write("""
        ### I. Potenciación: Multiplicación de Intensidad
        La potencia representa el crecimiento acelerado. En ingeniería, esto se usa para calcular áreas, volúmenes o la propagación de una señal.
        """)
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div class='caja-ley'>", unsafe_allow_html=True)
        st.write("**Leyes de los Exponentes:**")
        st.latex(r"a^m \cdot a^n = a^{m+n}")
        st.latex(r"\frac{a^m}{a^n} = a^{m-n}")
        st.latex(r"a^{-n} = \frac{1}{a^n}")
        st.latex(r"a^0 = 1")
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div class='subtitulo-profundo'>II. Radicación</div>", unsafe_allow_html=True)
        st.write("La raíz es una potencia fraccionaria. Es buscar la base original.")
        st.markdown("<div class='caja-ley'>", unsafe_allow_html=True)
        st.latex(r"\sqrt[n]{a} = a^{1/n}")
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div class='subtitulo-profundo'>III. Logaritmación</div>", unsafe_allow_html=True)
        st.write("El logaritmo responde: ¿A qué potencia elevé la base para obtener este número?")
        st.markdown("<div class='caja-ley'>", unsafe_allow_html=True)
        st.latex(r"\log_b(x) = y \iff b^y = x")
        st.markdown("</div>", unsafe_allow_html=True)

    # --- CAPÍTULOS POR HACER ---
    elif capitulo == "1.4 Jerarquía de Operaciones":
        st.info("Próximamente: Reglas de PEMDAS.")
    elif capitulo == "1.5 Proporcionalidad":
        st.info("Próximamente: Regla de tres.")
