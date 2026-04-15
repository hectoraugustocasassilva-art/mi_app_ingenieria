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

# --- NAVEGACIÓN LATERAL ---
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
        En matemáticas aplicadas, el signo no es un simple atributo; es un **operador de simetría fundamental**. Todo número real $a$ posee un gemelo opuesto $-a$, cuya interacción es la base del equilibrio algebraico. 
        
        Este concepto se sustenta en el **Axioma del Inverso Aditivo**: Para cada elemento existe un opuesto único tal que su suma resulta en la identidad aditiva (el Cero). Sin este pilar, sería imposible modelar fuerzas en oposición o balances financieros.
        """)
        st.markdown("</div>", unsafe_allow_html=True)

        st.subheader("II. Estructura Lógica de la Adición y Multiplicación")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("<div class='caja-ley'>", unsafe_allow_html=True)
            st.write("**Axiomas de la Suma:**")
            st.latex(r"a + (-a) = 0 \quad \text{(Anulación)}")
            st.latex(r"(-a) + (-b) = -(a+b) \quad \text{(Acumulación Negativa)}")
            st.markdown("</div>", unsafe_allow_html=True)
        with col2:
            st.markdown("<div class='caja-ley'>", unsafe_allow_html=True)
            st.write("**Leyes de Polaridad (Multiplicación):**")
            st.latex(r"(-) \cdot (-) = (+) \quad \text{(Inversión de la inversión)}")
            st.latex(r"(-) \cdot (+) = (-) \quad \text{(Dominancia de polaridad)}")
            st.markdown("</div>", unsafe_allow_html=True)

    # ==========================================
    # 1.2 FRACCIONES
    # ==========================================
    elif capitulo == "1.2 Fracciones, Decimales y Porcentajes":
        st.markdown("<div class='subtitulo-profundo'>1.2 El Dominio de las Partes: Racionales</div>", unsafe_allow_html=True)
        st.markdown("<div class='texto-profundo'>", unsafe_allow_html=True)
        st.write("""
        ### I. Anatomía y Ontología de la Fracción
        Una fracción no es simplemente una operación aritmética pendiente; es la representación exacta de una relación proporcional entre una **parte** (numerador) y un **todo** (denominador). En el ámbito de la ingeniería y la topografía, la fracción es el lenguaje de la precisión absoluta. 
        
        A diferencia de los números decimales, que a menudo requieren redondeos (como en el caso de $1/3 \approx 0.333...$), la fracción conserva la integridad del dato original. Esta característica es vital para evitar el **error de truncamiento acumulado**, el cual puede desviar significativamente los resultados en cálculos de rutas técnicas o inventarios de carga en proyectos territoriales.
        """)
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div class='caja-ley'>", unsafe_allow_html=True)
        st.subheader("II. Algoritmos de Operación en el Conjunto Racional")
        st.write("**1. Suma y Resta Heterogénea (El Algoritmo del Producto Cruzado):**")
        st.latex(r"\frac{a}{b} \pm \frac{c}{d} = \frac{ad \pm bc}{bd}")
        st.write("**2. Multiplicación (Producto Lineal):**")
        st.latex(r"\frac{a}{b} \cdot \frac{c}{d} = \frac{ac}{bd}")
        st.write("**3. División (Inversión Multiplicativa o 'Ley de la Oreja'):**")
        st.latex(r"\frac{a/b}{c/d} = \frac{ad}{bc}")
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div class='subtitulo-profundo'>III. Transformación de Dominios: Decimales y Porcentajes</div>", unsafe_allow_html=True)
        st.markdown("<div class='texto-profundo'>", unsafe_allow_html=True)
        st.write("""
        La transición entre fracciones, decimales y porcentajes es una cuestión de **escala de visualización**. 
        
        * **El Decimal:** Es la expresión de la fracción en base 10, ideal para el manejo de divisas y lecturas rápidas de instrumentos de medición.
        * **El Porcentaje:** Es una fracción normalizada con denominador 100 ($n/100$), utilizada para expresar variaciones, márgenes de error y análisis estadísticos de campo.
        """)
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div class='paso-a-paso'>", unsafe_allow_html=True)
        st.write("**Ejemplo de Aplicación Técnica:**")
        st.write("Si una ruta en Murillo tiene una pendiente del 12.5%, esto se traduce directamente a:")
        st.latex(r"12.5\% = \frac{12.5}{100} = \frac{125}{1000} = \frac{1}{8}")
        st.write("Esto significa que por cada 8 metros horizontales, el terreno asciende 1 metro vertical.")
        st.markdown("</div>", unsafe_allow_html=True)

    # ==========================================
    # 1.3 POTENCIAS, RAÍCES Y LOGARITMOS
    # ==========================================
    elif capitulo == "1.3 Potencias, Raíces y Logaritmos":
        st.markdown("<div class='subtitulo-profundo'>1.3 Operaciones de Orden Superior y Funciones Exponenciales</div>", unsafe_allow_html=True)
        st.markdown("<div class='texto-profundo'>", unsafe_allow_html=True)
        st.write("""
        ### I. Potenciación: La Escala de Magnitud
        La potenciación es la herramienta para cuantificar procesos no lineales. Mientras la multiplicación acumula, la potencia **acelera**. Es el lenguaje de la geometría (áreas y volúmenes) y de la física (energía cinética, gravitación).
        """)
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div class='caja-ley'>", unsafe_allow_html=True)
        st.subheader("Axiomas y Leyes de Transformación")
        col1, col2 = st.columns(2)
        with col1:
            st.write("**Producto de potencias de igual base:**")
            st.latex(r"a^m \cdot a^n = a^{m+n}")
            st.write("**Potencia de un producto:**")
            st.latex(r"(a \cdot b)^n = a^n \cdot b^n")
        with col2:
            st.write("**Potencia de potencia:**")
            st.latex(r"(a^m)^n = a^{m \cdot n}")
            st.write("**Exponente negativo:**")
            st.latex(r"a^{-n} = \frac{1}{a^n}")
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div class='subtitulo-profundo'>II. Logaritmación</div>", unsafe_allow_html=True)
        st.markdown("<div class='caja-ley'>", unsafe_allow_html=True)
        st.write("**Propiedades Maestras:**")
        st.latex(r"\log_b(M \cdot N) = \log_b(M) + \log_b(N)")
        st.markdown("</div>", unsafe_allow_html=True)

    # ==========================================
    # 1.4 JERARQUÍA
    # ==========================================
    elif capitulo == "1.4 Jerarquía de Operaciones":
        st.markdown("<div class='subtitulo-profundo'>1.4 El Protocolo Lógico: Jerarquía Operativa y GEMDAS</div>", unsafe_allow_html=True)
        st.markdown("<div class='texto-profundo'>", unsafe_allow_html=True)
        st.write("""
        ### I. La Arquitectura del Orden Matemático
        En matemáticas y programación de ingeniería, el orden de ejecución no es una sugerencia, sino una ley física del lenguaje. Sin un protocolo estricto, una expresión aritmética carecería de un valor unívoco.
        """)
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div class='paso-a-paso'>", unsafe_allow_html=True)
        st.write("1. **G**rupos: (), [], {}")
        st.write("2. **E**xponentes y Raíces.")
        st.write("3. **M/D**ultiplicación y División.")
        st.write("4. **A/S**uma y Resta.")
        st.markdown("</div>", unsafe_allow_html=True)

    # ==========================================
    # 1.5 PROPORCIONALIDAD
    # ==========================================
    elif capitulo == "1.5 Proporcionalidad y Regla de Tres":
        st.markdown("<div class='subtitulo-profundo'>1.5 Teoría de la Proporcionalidad</div>", unsafe_allow_html=True)
        st.markdown("<div class='texto-profundo'>", unsafe_allow_html=True)
        st.write("""
        ### I. La Proporcionalidad como Relación de Dependencia
        En el análisis técnico, la proporcionalidad es el estudio de las variaciones constantes entre magnitudes.
        """)
        st.markdown("</div>", unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            st.markdown("<div class='caja-ley'>", unsafe_allow_html=True)
            st.write("**Regla de Tres Simple Directa:**")
            st.latex(r"x = \frac{b \cdot c}{a}")
            st.markdown("</div>", unsafe_allow_html=True)
        with col2:
            st.markdown("<div class='caja-ley'>", unsafe_allow_html=True)
            st.write("**Regla de Tres Simple Inversa:**")
            st.latex(r"x = \frac{a \cdot b}{c}")
            st.markdown("</div>", unsafe_allow_html=True)
