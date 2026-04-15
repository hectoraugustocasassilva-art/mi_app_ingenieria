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
    # 1.1 LOS SIGNOS (EXTENSIÓN MÁXIMA)
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
    # 1.2 FRACCIONES (EXTENSIÓN MÁXIMA)
    # ==========================================
    elif capitulo == "1.2 Fracciones, Decimales y Porcentajes":
        st.markdown("<div class='subtitulo-profundo'>1.2 El Dominio de las Partes: Racionales</div>", unsafe_allow_html=True)
        st.markdown("<div class='texto-profundo'>", unsafe_allow_html=True)
        st.write("""
        ### I. Anatomía y Teoría de la Fracción
        Una fracción representa la razón exacta entre dos cantidades enteras, definida como el conjunto $\mathbb{Q}$. A diferencia de los decimales, la fracción conserva la precisión infinita, evitando errores de redondeo en cálculos estructurales o topográficos.
        
        El **Numerador** actúa como el contador de unidades de medida, mientras que el **Denominador** define la partición del espacio o la unidad.
        """)
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div class='caja-ley'>", unsafe_allow_html=True)
        st.subheader("Algoritmos de Operación Racional")
        st.write("**Suma de Distinto Denominador (Mínimo Común Múltiplo):**")
        st.latex(r"\frac{a}{b} \pm \frac{c}{d} = \frac{ad \pm bc}{bd}")
        st.write("**División por Inversión (Ley de la Oreja):**")
        st.latex(r"\frac{a/b}{c/d} = \frac{ad}{bc}")
        st.write("**Simplificación por Factores Primos:**")
        st.latex(r"\frac{an}{bn} = \frac{a}{b}")
        st.markdown("</div>", unsafe_allow_html=True)

    # ==========================================
    # 1.3 POTENCIAS, RAÍCES Y LOGARITMOS (AMPLIADO)
    # ==========================================
    elif capitulo == "1.3 Potencias, Raíces y Logaritmos":
        st.markdown("<div class='subtitulo-profundo'>1.3 Operaciones de Orden Superior</div>", unsafe_allow_html=True)
        st.markdown("<div class='texto-profundo'>", unsafe_allow_html=True)
        st.write("""
        ### I. Potenciación: La Multiplicación de Intensidad
        La potencia representa el crecimiento exponencial y la magnitud escalar. En ingeniería, se utiliza para modelar áreas ($L^2$), volúmenes ($L^3$) y la propagación de ondas. 
        
        **Demostración del Exponente 0:** Partiendo de $\\frac{a^n}{a^n} = a^{n-n} = a^0$, y sabiendo que cualquier magnitud entre sí misma es la unidad, se concluye que $a^0 = 1$.
        """)
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div class='caja-ley'>", unsafe_allow_html=True)
        st.write("**Leyes Universales de Exponentes:**")
        st.latex(r"a^m \cdot a^n = a^{m+n} \quad | \quad (a^m)^n = a^{m \cdot n}")
        st.latex(r"a^{-n} = \frac{1}{a^n} \quad | \quad \sqrt[n]{a} = a^{1/n}")
        st.write("**Logaritmación (Búsqueda del Exponente):**")
        st.latex(r"\log_b(x) = y \iff b^y = x")
        st.latex(r"\log(a \cdot b) = \log(a) + \log(b)")
        st.markdown("</div>", unsafe_allow_html=True)

    # ==========================================
    # 1.4 JERARQUÍA (AMPLIADO)
    # ==========================================
    elif capitulo == "1.4 Jerarquía de Operaciones":
        st.markdown("<div class='subtitulo-profundo'>1.4 El Orden del Caos: Protocolo GEMDAS</div>", unsafe_allow_html=True)
        st.markdown("<div class='texto-profundo'>", unsafe_allow_html=True)
        st.write("""
        ### I. Arquitectura de Prioridad Operativa
        La jerarquía de operaciones es el protocolo lógico que garantiza la univocidad en el resultado de cualquier expresión. Sin este orden estricto, el cálculo técnico carecería de validez universal.
        """)
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div class='paso-a-paso'>", unsafe_allow_html=True)
        st.write("1. **G**rupos: Paréntesis (), Corchetes [], Llaves {} y barras de división.")
        st.write("2. **E**xponentes y Raíces.")
        st.write("3. **M/D**ultiplicación y División: Se ejecutan estrictamente de izquierda a derecha.")
        st.write("4. **A/S**uma y Resta: Nivel final de ejecución.")
        st.markdown("</div>", unsafe_allow_html=True)
        
        st.info("💡 **Aviso Técnico:** La multiplicación no precede a la división; ambas comparten rango y se resuelven por aparición secuencial.")

    # ==========================================
    # 1.5 PROPORCIONALIDAD (AMPLIADO)
    # ==========================================
    elif capitulo == "1.5 Proporcionalidad y Regla de Tres":
        st.markdown("<div class='subtitulo-profundo'>1.5 Relaciones Proporcionales y Escalas Técnicas</div>", unsafe_allow_html=True)
        st.markdown("<div class='texto-profundo'>", unsafe_allow_html=True)
        st.write("""
        ### I. Proporcionalidad Directa e Inversa
        Este concepto es vital para la dosificación de mezclas, el cálculo de escalas en cartografía y la gestión de recursos en campo.
        
        - **Proporcionalidad Directa:** $y = kx$. Al aumentar una variable, la otra aumenta en la misma razón constante $k$.
        - **Proporcionalidad Inversa:** $y = k/x$. El incremento de una variable produce el decremento proporcional de la otra.
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

        st.write("### II. Aplicación Técnica: Constante de Proporcionalidad")
        st.latex(r"k = \frac{y}{x} \quad \text{(En relaciones directas)}")
