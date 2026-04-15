import streamlit as st

st.set_page_config(page_title="Enciclopedia de Ciencias Básicas", layout="wide")

# Estilos visuales para resaltar fórmulas y texto
st.markdown("""
    <style>
    .texto-profundo { font-size: 18px; line-height: 1.8; text-align: justify; color: #1a202c; }
    .caja-formula { background-color: #f1f5f9; border: 2px solid #3b82f6; padding: 20px; border-radius: 10px; margin: 20px 0; }
    .explicacion-paso { color: #065f46; font-weight: bold; border-left: 4px solid #10b981; padding-left: 15px; }
    </style>
    """, unsafe_allow_html=True)

st.sidebar.title("📚 Biblioteca Total")
tomo = st.sidebar.selectbox("Selecciona un Tomo:", 
    ["Tomo I: Aritmética Avanzada", "Tomo II: Álgebra", "Tomo III: Física", "Tomo IV: Química"])

if tomo == "Tomo I: Aritmética Avanzada":
    st.title("🔢 Tomo I: Fundamentos Numéricos y Operaciones")
    
    capitulo = st.sidebar.radio("Capítulos:", [
        "1.1 Leyes de los Signos (El Corazón de la Operación)", 
        "1.2 Teoría de Fracciones (Partición y Proporción)", 
        "1.3 Potenciación y Radicación (Crecimiento Exponencial)"
    ])

    if capitulo == "1.1 Leyes de los Signos (El Corazón de la Operación)":
        st.header("1.1 Leyes de los Signos: Dirección y Magnitud")
        st.markdown("<div class='texto-profundo'>", unsafe_allow_html=True)
        st.write("""
        En ingeniería y matemáticas generales, el signo nos dice hacia dónde va la cantidad. 
        Para dominar esto, debemos separar las reglas de la **Suma** de las reglas de la **Multiplicación**.
        """)
        
        st.subheader("A) Reglas para Suma y Resta")
        st.markdown("<div class='caja-formula'>", unsafe_allow_html=True)
        st.latex(r"(+) + (+) = (+)")
        st.latex(r"(-) + (-) = (-)")
        st.latex(r"(+) + (-) = \text{Signo del número con mayor valor absoluto}")
        st.markdown("</div>", unsafe_allow_html=True)
        st.write("""
        <p class='explicacion-paso'>¿Cómo leer esto?</p>
        Si sumas dos deudas, tendrás una deuda más grande. Si sumas un número positivo y uno negativo, imagina una cuerda: el número más fuerte (más grande) arrastra el resultado hacia su signo.
        """, unsafe_allow_html=True)

        st.subheader("B) Reglas para Multiplicación y División")
        st.markdown("<div class='caja-formula'>", unsafe_allow_html=True)
        st.latex(r"(+) \cdot (+) = (+)")
        st.latex(r"(-) \cdot (-) = (+)")
        st.latex(r"(+) \cdot (-) = (-)")
        st.latex(r"(-) \cdot (+) = (-)")
        st.markdown("</div>", unsafe_allow_html=True)
        st.write("""
        <p class='explicacion-paso'>El fundamento:</p>
        Multiplicar por un negativo es una orden de 'invertir'. Si inviertes algo que ya estaba invertido (negativo), vuelve a ser original (positivo).
        """, unsafe_allow_html=True)

    elif capitulo == "1.2 Teoría de Fracciones (Partición y Proporción)":
        st.header("1.2 El Operador Fraccionario")
        st.markdown("<div class='caja-formula'>", unsafe_allow_html=True)
        st.write("**Suma y Resta (Método de la Mariposa/MCM):**")
        st.latex(r"\frac{a}{b} \pm \frac{c}{d} = \frac{ad \pm bc}{bd}")
        st.write("**Multiplicación (Directa):**")
        st.latex(r"\frac{a}{b} \cdot \frac{c}{d} = \frac{ac}{bd}")
        st.write("**División (Inversa/Oreja):**")
        st.latex(r"\frac{a}{b} \div \frac{c}{d} = \frac{ad}{bc}")
        st.markdown("</div>", unsafe_allow_html=True)
        st.write("""
        <p class='explicacion-paso'>Análisis de la Fórmula:</p>
        En la multiplicación, el numerador ($a$) se multiplica directamente por el otro numerador ($c$). No necesitas buscar comunes denominadores porque estás creando una nueva unidad de medida.
        """, unsafe_allow_html=True)

    elif capitulo == "1.3 Potenciación y Radicación (Crecimiento Exponencial)":
        st.header("1.3 Potencias: Multiplicación Abreviada")
        st.write("Las potencias nos dicen cuántas veces se multiplica la **Base** por sí misma.")
        
        st.markdown("<div class='caja-formula'>", unsafe_allow_html=True)
        st.latex(r"a^n \cdot a^m = a^{n+m}")
        st.latex(r"\frac{a^n}{a^m} = a^{n-m}")
        st.latex(r"(a^n)^m = a^{n \cdot m}")
        st.latex(r"a^0 = 1 \quad (a \neq 0)")
        st.markdown("</div>", unsafe_allow_html=True)
        
        st.write("""
        <p class='explicacion-paso'>¿Por qué se suman los exponentes?</p>
        Si tienes $2^2 \cdot 2^3$, en realidad tienes $(2 \cdot 2) \cdot (2 \cdot 2 \cdot 2)$. En total hay cinco '2'. Por eso $2+3=5$. La fórmula es solo el resumen de lo que ves.
        """, unsafe_allow_html=True)

# Espacio para los siguientes tomos
elif tomo == "Tomo II: Álgebra":
    st.title("📐 Tomo II: Álgebra General")
    st.info("Próximamente: Leyes de Newton, Ecuaciones de primer grado y Factorización.")
