import streamlit as st

st.set_page_config(page_title="Enciclopedia Universal de Ciencias", layout="wide")

# --- ESTILOS DE LECTURA PROFUNDA (CSS) ---
st.markdown("""
    <style>
    .titulo-principal { color: #1e3a8a; font-size: 45px; font-weight: bold; border-bottom: 4px solid #3b82f6; }
    .texto-profundo { font-size: 19px; line-height: 2.0; text-align: justify; color: #1a202c; padding: 15px; }
    .caja-ley { background-color: #f8fafc; border: 2px solid #cbd5e1; padding: 30px; border-radius: 12px; margin: 25px 0; }
    .subtitulo-profundo { color: #1e40af; font-size: 28px; font-weight: bold; margin-top: 35px; border-left: 8px solid #1e40af; padding-left: 15px; }
    .paso-a-paso { background-color: #f0fdf4; border-left: 5px solid #16a34a; padding: 20px; margin: 20px 0; font-family: 'Courier New', Courier, monospace; }
    </style>
    """, unsafe_allow_html=True)

# --- NAVEGACIÓN ---
st.sidebar.title("📚 Biblioteca de Ingeniería")
tomo = st.sidebar.selectbox("Seleccionar Tomo:", ["Tomo I: Aritmética Profunda", "Tomo II: Álgebra", "Tomo III: Física", "Tomo IV: Química"])

if tomo == "Tomo I: Aritmética Profunda":
    st.markdown("<div class='titulo-principal'>Tomo I: Aritmética y Fundamentos Lógicos</div>", unsafe_allow_html=True)
    
    capitulo = st.sidebar.radio("Capítulos Detallados:", [
        "1.1 Los Signos y la Lógica Operativa", 
        "1.2 Fracciones, Decimales y Porcentajes",
        "1.3 Potencias, Raíces y Logaritmos",
        "1.4 Jerarquía de Operaciones",
        "1.5 Proporcionalidad y Regla de Tres"
    ])

    # ==========================================
    # 1.1 LOS SIGNOS
    # ==========================================
    if capitulo == "1.1 Los Signos y la Lógica Operativa":
        st.markdown("<div class='subtitulo-profundo'>1.1 El Dominio de los Signos: Más allá de las reglas</div>", unsafe_allow_html=True)
        st.markdown("<div class='texto-profundo'>", unsafe_allow_html=True)
        st.write("""
        ### I. La Naturaleza de la Dualidad Numérica
        En matemáticas, el signo no es un objeto, es un **operador de simetría**. Todo número real $a$ tiene un gemelo opuesto $-a$, tal que al juntarse recuperan el equilibrio original: el **Cero**.
        Esta relación se basa en el **Axioma del Inverso Aditivo**.
        """)
        st.markdown("</div>", unsafe_allow_html=True)

        st.subheader("II. Estructura de la Adición")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("<div class='caja-ley'>", unsafe_allow_html=True)
            st.write("**1. Propiedad de Clausura:**")
            st.latex(r"a, b \in \mathbb{R} \implies (a+b) \in \mathbb{R}")
            st.markdown("</div>", unsafe_allow_html=True)
        with col2:
            st.markdown("<div class='caja-ley'>", unsafe_allow_html=True)
            st.write("**2. Inverso Aditivo:**")
            st.latex(r"a + (-a) = 0")
            st.markdown("</div>", unsafe_allow_html=True)

    # ==========================================
    # 1.2 FRACCIONES
    # ==========================================
    elif capitulo == "1.2 Fracciones, Decimales y Porcentajes":
        st.markdown("<div class='subtitulo-profundo'>1.2 El Dominio de las Partes: Racionales</div>", unsafe_allow_html=True)
        st.markdown("<div class='texto-profundo'>", unsafe_allow_html=True)
        st.write("""
        ### I. Teoría de la Fracción
        Una fracción es una **división pausada**. Es la relación exacta entre la parte y el todo, permitiendo medir lo que los números enteros no pueden.
        """)
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div class='caja-ley'>", unsafe_allow_html=True)
        st.write("**Operaciones Esenciales:**")
        st.latex(r"\frac{a}{b} \pm \frac{c}{d} = \frac{ad \pm bc}{bd}")
        st.latex(r"\frac{a}{b} \cdot \frac{c}{d} = \frac{ac}{bd}")
        st.latex(r"\frac{a/b}{c/d} = \frac{ad}{bc}")
        st.markdown("</div>", unsafe_allow_html=True)

    # ==========================================
    # 1.3 POTENCIAS, RAÍCES Y LOGARITMOS
    # ==========================================
    elif capitulo == "1.3 Potencias, Raíces y Logaritmos":
        st.markdown("<div class='subtitulo-profundo'>1.3 Operaciones de Orden Superior</div>", unsafe_allow_html=True)
        st.markdown("<div class='texto-profundo'>", unsafe_allow_html=True)
        st.write("""
        ### I. Potenciación: Crecimiento Acelerado
        La potencia define el crecimiento de áreas y volúmenes. Es el motor fundamental de las leyes de la física y el cálculo.
        """)
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div class='caja-ley'>", unsafe_allow_html=True)
        st.latex(r"a^m \cdot a^n = a^{m+n}")
        st.latex(r"a^{-n} = \frac{1}{a^n}")
        st.latex(r"a^0 = 1 \quad (a \neq 0)")
        st.latex(r"\log_b(x) = y \iff b^y = x")
        st.markdown("</div>", unsafe_allow_html=True)

    # ==========================================
    # 1.4 JERARQUÍA DE OPERACIONES
    # ==========================================
    elif capitulo == "1.4 Jerarquía de Operaciones":
        st.markdown("<div class='subtitulo-profundo'>1.4 El Orden del Caos: Jerarquía Operativa</div>", unsafe_allow_html=True)
        st.markdown("<div class='texto-profundo'>", unsafe_allow_html=True)
        st.write("""
        ### I. El Protocolo GEMDAS
        El orden de las operaciones garantiza que una expresión matemática tenga un único valor lógico. Es el sistema operativo de la aritmética.
        """)
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div class='caja-ley'>", unsafe_allow_html=True)
        st.write("1. **G**rupos (Paréntesis, Corchetes)")
        st.write("2. **E**xponentes y Raíces")
        st.write("3. **M**ultiplicación y **D**ivisión (Izquierda a Derecha)")
        st.write("4. **A**dición y **S**ustracción (Izquierda a Derecha)")
        st.markdown("</div>", unsafe_allow_html=True)

    # ==========================================
    # 1.5 PROPORCIONALIDAD
    # ==========================================
    elif capitulo == "1.5 Proporcionalidad y Regla de Tres":
        st.markdown("<div class='subtitulo-profundo'>1.5 Relaciones Proporcionales y Escalas</div>", unsafe_allow_html=True)
        st.markdown("<div class='texto-profundo'>", unsafe_allow_html=True)
        st.write("""
        ### I. Proporcionalidad Práctica
        Entender cómo una variable afecta a otra es la base para diseñar escalas, presupuestos y cálculos de resistencia.
        """)
        st.markdown("</div>", unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            st.markdown("<div class='caja-ley'>", unsafe_allow_html=True)
            st.write("**Proporción Directa:**")
            st.write("A más, más; a menos, menos.")
            st.latex(r"x = \frac{b \cdot c}{a}")
            st.markdown("</div>", unsafe_allow_html=True)
        with col2:
            st.markdown("<div class='caja-ley'>", unsafe_allow_html=True)
            st.write("**Proporción Inversa:**")
            st.write("A más, menos; a menos, más.")
            st.latex(r"x = \frac{a \cdot b}{c}")
            st.markdown("</div>", unsafe_allow_html=True)
