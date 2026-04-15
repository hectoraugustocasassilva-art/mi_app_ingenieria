import streamlit as st

st.set_page_config(page_title="Enciclopedia Universal de Ciencias", layout="wide")

# --- ESTILOS DE LECTURA PROFUNDA ---
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
st.sidebar.title("📚 Biblioteca Universal")
tomo = st.sidebar.selectbox("Seleccionar Tomo:", ["Tomo I: Aritmética Profunda", "Tomo II: Álgebra", "Tomo III: Física", "Tomo IV: Química"])

if tomo == "Tomo I: Aritmética Profunda":
    st.markdown("<div class='titulo-principal'>Tomo I: Aritmética y Fundamentos Lógicos</div>", unsafe_allow_html=True)
    
    capitulo = st.sidebar.radio("Capítulos Detallados:", [
        "1.1 Los Signos y la Lógica Operativa (Completo)", 
        "1.2 Fracciones, Decimales y Porcentajes (Completo)",
        "1.3 Potencias, Raíces y Logaritmos (En desarrollo)",
        "1.4 Jerarquía de Operaciones",
        "1.5 Proporcionalidad"
    ])

    if capitulo == "1.1 Los Signos y la Lógica Operativa (Completo)":
        st.markdown("<div class='subtitulo-profundo'>1.1 El Dominio de los Signos: Más allá de las reglas</div>", unsafe_allow_html=True)
        st.markdown("<div class='texto-profundo'>", unsafe_allow_html=True)
        st.write("""
        El estudio de los signos es el estudio de la **polaridad**. En matemáticas, un signo no indica solo si algo es 'bueno' o 'malo', sino su posición respecto al **Cero (Punto de Equilibrio)**. 
        
        ### I. La Naturaleza de la Adición y Sustracción
        Cuando sumamos o restamos, estamos desplazándonos por la recta numérica. El error común es tratar de memorizar 'más por menos' en la suma. **Error grave.** La suma se rige por la **Magnitud y la Dirección**.
        
        **A. Números con Signos Iguales:** Se suman sus valores absolutos y se mantiene el signo. Si debes 5 y pides prestados otros 10, tu deuda total es de 15.
        """)
        st.markdown("</div>", unsafe_allow_html=True)
        
        st.markdown("<div class='caja-ley'>", unsafe_allow_html=True)
        st.latex(r"(+a) + (+b) = +(a+b)")
        st.latex(r"(-a) + (-b) = -(a+b)")
        st.write("**Ejemplo:** $(-120) + (-80) = -200$")
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div class='texto-profundo'>", unsafe_allow_html=True)
        st.write("""
        **B. Números con Signos Diferentes:** Se restan sus valores absolutos (el mayor menos el menor) y el resultado lleva el signo del número con mayor magnitud.
        """)
        st.markdown("</div>", unsafe_allow_html=True)
        st.latex(r"(+a) + (-b) \implies \text{Si } |a| > |b|, \text{ resultado es } (+)")
        
        st.markdown("<div class='subtitulo-profundo'>II. Leyes Multiplicativas (El Operador de Inversión)</div>", unsafe_allow_html=True)
        st.write("Aquí el signo actúa como un interruptor. El signo $(-)$ invierte la dirección.")
        
        st.markdown("<div class='caja-ley'>", unsafe_allow_html=True)
        st.latex(r"(+) \cdot (+) = (+)")
        st.latex(r"(-) \cdot (-) = (+)")
        st.latex(r"(+) \cdot (-) = (-)")
        st.latex(r"(-) \cdot (+) = (-)")
        st.markdown("</div>", unsafe_allow_html=True)

    elif capitulo == "1.2 Fracciones, Decimales y Porcentajes (Completo)":
        st.markdown("<div class='subtitulo-profundo'>1.2 La Partición de la Unidad: Fracciones y sus Equivalentes</div>", unsafe_allow_html=True)
        
        st.write("### I. Teoría de la Fracción")
        st.write("Una fracción es un cociente no realizado. Es la expresión exacta de una división.")
        
        st.markdown("<div class='caja-ley'>", unsafe_allow_html=True)
        st.write("**Suma de Fracciones Heterogéneas (Distinto Denominador):**")
        st.latex(r"\frac{a}{b} + \frac{c}{d} = \frac{(a \cdot d) + (b \cdot c)}{b \cdot d}")
        st.write("**Multiplicación:**")
        st.latex(r"\frac{a}{b} \cdot \frac{c}{d} = \frac{a \cdot c}{b \cdot d}")
        st.write("**División (Producto Cruzado):**")
        st.latex(r"\frac{a}{b} \div \frac{c}{d} = \frac{a \cdot d}{b \cdot c}")
        st.markdown("</div>", unsafe_allow_html=True)

        st.write("### II. Transformación a Decimales")
        st.write("Todo número fraccionario tiene una representación decimal que se obtiene dividiendo el numerador por el denominador.")
        st.markdown("<div class='paso-a-paso'>", unsafe_allow_html=True)
        st.write("1. Fracción: 3/4")
        st.write("2. Proceso: 3 ÷ 4 = 0.75")
        st.write("3. Interpretación: El 75% de la unidad.")
        st.markdown("</div>", unsafe_allow_html=True)

        st.write("### III. Porcentajes: La base 100")
        st.write("El porcentaje es una fracción cuyo denominador es siempre 100.")
        st.latex(r"x\% = \frac{x}{100}")
        st.write("**Cálculo de un porcentaje de una cantidad:**")
        st.latex(r"\text{Total} \cdot \left(\frac{\%}{100}\right)")

# Seguiremos expandiendo los demás capítulos de la misma forma masiva.
