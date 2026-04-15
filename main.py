import streamlit as st

st.set_page_config(page_title="Enciclopedia Universal de Ciencias", layout="wide")

# --- ESTILOS DE LIBRO TÉCNICO ---
st.markdown("""
    <style>
    .titulo-principal { color: #1e3a8a; font-size: 45px; font-weight: bold; border-bottom: 4px solid #3b82f6; }
    .texto-profundo { font-size: 19px; line-height: 1.9; text-align: justify; color: #1a202c; padding: 10px; }
    .caja-ley { background-color: #f8fafc; border: 1px solid #cbd5e1; padding: 25px; border-radius: 12px; margin: 25px 0; box-shadow: 2px 2px 10px rgba(0,0,0,0.05); }
    .nota-ingeniero { border-left: 5px solid #eab308; background-color: #fefce8; padding: 15px; margin: 20px 0; font-style: italic; }
    .paso-titulo { color: #1e40af; font-weight: bold; font-size: 22px; margin-top: 20px; }
    </style>
    """, unsafe_allow_html=True)

# --- NAVEGACIÓN DE BIBLIOTECA ---
st.sidebar.title("📚 Biblioteca Universal")
tomo = st.sidebar.selectbox("Seleccionar Tomo:", 
    ["Tomo I: Aritmética y Teoría Numérica", "Tomo II: Álgebra", "Tomo III: Física", "Tomo IV: Química"])

if tomo == "Tomo I: Aritmética y Teoría Numérica":
    st.markdown("<div class='titulo-principal'>Tomo I: El Fundamento de las Cantidades</div>", unsafe_allow_html=True)
    
    capitulo = st.sidebar.radio("Navegar por los Capítulos:", [
        "1.1 Los Signos y la Lógica Operativa", 
        "1.2 Fracciones, Decimales y Porcentajes", 
        "1.3 Potencias, Raíces y Logaritmos",
        "1.4 Jerarquía de Operaciones (PEMDAS)",
        "1.5 Proporcionalidad (Regla de Tres Simple y Compuesta)"
    ])

    # --- CAPÍTULO 1.1 ---
    if capitulo == "1.1 Los Signos y la Lógica Operativa":
        st.header("1.1 El Dominio de los Signos: Leyes Universales")
        st.markdown("<div class='texto-profundo'>", unsafe_allow_html=True)
        st.write("""
        Para un estudiante de ingeniería, los signos no son adornos; son **operadores de dirección**. En el mundo real, un signo negativo puede significar una fuerza de compresión, una deuda financiera o un retroceso en una trayectoria.
        """)
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("<div class='caja-ley'>", unsafe_allow_html=True)
            st.subheader("Ley de la Adición (Suma/Resta)")
            st.write("Cuando los signos son iguales, las magnitudes se acumulan:")
            st.latex(r"(-a) + (-b) = -(a+b)")
            st.write("Cuando los signos son diferentes, las magnitudes se restan:")
            st.latex(r"a + (-b) = a - b")
            st.markdown("</div>", unsafe_allow_html=True)
            
        with col2:
            st.markdown("<div class='caja-ley'>", unsafe_allow_html=True)
            st.subheader("Ley del Producto (Multiplicación/División)")
            st.latex(r"(+) \times (+) = (+)")
            st.latex(r"(-) \times (-) = (+)")
            st.latex(r"(+) \times (-) = (-)")
            st.latex(r"(-) \times (+) = (-)")
            st.markdown("</div>", unsafe_allow_html=True)

    # --- CAPÍTULO 1.3 ---
    elif capitulo == "1.3 Potencias, Raíces y Logaritmos":
        st.header("1.3 Operaciones de Orden Superior")
        
        st.markdown("<div class='paso-titulo'>Leyes de los Exponentes (Fundamento del Crecimiento)</div>", unsafe_allow_html=True)
        st.markdown("<div class='caja-ley'>", unsafe_allow_html=True)
        st.latex(r"a^m \cdot a^n = a^{m+n}")
        st.latex(r"\frac{a^m}{a^n} = a^{m-n}")
        st.latex(r"(a^m)^n = a^{m \cdot n}")
        st.latex(r"(a \cdot b)^n = a^n \cdot b^n")
        st.latex(r"a^{-n} = \frac{1}{a^n}")
        st.markdown("</div>", unsafe_allow_html=True)
        
        st.markdown("<div class='paso-titulo'>Radicación: La operación inversa</div>", unsafe_allow_html=True)
        st.write("Una raíz es en realidad una potencia con un exponente fraccionario.")
        st.markdown("<div class='caja-ley'>", unsafe_allow_html=True)
        st.latex(r"\sqrt[n]{a} = a^{1/n}")
        st.latex(r"\sqrt[n]{a \cdot b} = \sqrt[n]{a} \cdot \sqrt[n]{b}")
        st.latex(r"\sqrt[n]{\frac{a}{b}} = \frac{\sqrt[n]{a}}{\sqrt[n]{b}}")
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div class='paso-titulo'>Logaritmos: ¿A qué potencia debo elevar?</div>", unsafe_allow_html=True)
        st.write("El logaritmo responde a la pregunta: ¿Cuántas veces debo multiplicar la base para llegar al número?")
        st.markdown("<div class='caja-ley'>", unsafe_allow_html=True)
        st.latex(r"\log_b(x) = y \iff b^y = x")
        st.latex(r"\log(a \cdot b) = \log(a) + \log(b)")
        st.latex(r"\log\left(\frac{a}{b}\right) = \log(a) - \log(b)")
        st.latex(r"\log(a^n) = n \cdot \log(a)")
        st.markdown("</div>", unsafe_allow_html=True)

    # --- CAPÍTULO 1.5 ---
    elif capitulo == "1.5 Proporcionalidad (Regla de Tres Simple y Compuesta)":
        st.header("1.5 Relaciones de Proporción")
        st.write("Esta es la herramienta más usada en la vida cotidiana y técnica para escalar medidas.")
        
        st.subheader("1. Regla de Tres Simple Directa")
        st.write("Si una variable sube y la otra también (ejemplo: más gasolina = más kilómetros).")
        st.latex(r"\frac{a}{b} = \frac{c}{x} \implies x = \frac{b \cdot c}{a}")
        
        st.subheader("2. Regla de Tres Simple Inversa")
        st.write("Si una variable sube y la otra baja (ejemplo: más obreros = menos tiempo de trabajo).")
        st.latex(r"a \cdot b = c \cdot x \implies x = \frac{a \cdot b}{c}")

# --- SECCIÓN PARA FUTUROS TOMOS ---
elif tomo == "Tomo II: Álgebra":
    st.header("📐 Tomo II: Álgebra General")
    st.write("Estamos preparando el despliegue de **Factorización**, **Productos Notables** y **Sistemas de Ecuaciones** con la misma profundidad.")
