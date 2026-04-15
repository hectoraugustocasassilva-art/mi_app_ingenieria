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
# ==========================================
    # 1.2 FRACCIONES, DECIMALES Y PORCENTAJES
    # ==========================================
    elif capitulo == "1.2 Fracciones, Decimales y Porcentajes":
        st.markdown("<div class='subtitulo-profundo'>1.2 El Dominio de las Partes: Números Racionales ($\mathbb{Q}$)</div>", unsafe_allow_html=True)
        
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
        st.write("Para combinar fracciones con distintos denominadores, debemos encontrar una base común que permita la conmensurabilidad:")
        st.latex(r"\frac{a}{b} \pm \frac{c}{d} = \frac{ad \pm bc}{bd}")
        
        st.write("**2. Multiplicación (Producto Lineal):**")
        st.write("A diferencia de la suma, la multiplicación opera sobre la magnitud total de los componentes:")
        st.latex(r"\frac{a}{b} \cdot \frac{c}{d} = \frac{ac}{bd}")
        
        st.write("**3. División (Inversión Multiplicativa o 'Ley de la Oreja'):**")
        st.write("Dividir por una fracción es equivalente a multiplicar por su inverso recíproco. Este es el fundamento para el cálculo de densidades y escalas:")
        st.latex(r"\frac{\frac{a}{b}}{\frac{c}{d}} = \frac{a \cdot d}{b \cdot c}")
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
    # 1.3 POTENCIAS, RAÍCES Y LOGARITMOS (VERSIÓN TÉCNICA AVANZADA)
    # ==========================================
    elif capitulo == "1.3 Potencias, Raíces y Logaritmos":
        st.markdown("<div class='subtitulo-profundo'>1.3 Operaciones de Orden Superior y Funciones Exponenciales</div>", unsafe_allow_html=True)
        
        st.markdown("<div class='texto-profundo'>", unsafe_allow_html=True)
        st.write("""
        ### I. Potenciación: La Escala de Magnitud
        La potenciación es la herramienta para cuantificar procesos no lineales. Mientras la multiplicación acumula, la potencia **acelera**. Es el lenguaje de la geometría (áreas y volúmenes) y de la física (energía cinética, gravitación).
        
        #### El Fenómeno de los Casos Especiales:
        * **Bases negativas:** $(-a)^n$ es positivo si $n$ es par, y negativo si $n$ es impar. Esta alternancia es la base de los sistemas oscilatorios.
        * **La Indeterminación $0^0$:** En el análisis de límites, esta expresión representa una de las mayores singularidades matemáticas, requiriendo herramientas avanzadas como la regla de L'Hôpital para su resolución.
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
            st.write("**Exponente negativo (Inversión funcional):**")
            st.latex(r"a^{-n} = \frac{1}{a^n}")
        st.markdown("</div>", unsafe_allow_html=True)

        st.error("⚠️ **La Trampa del Binomio:** Nunca confundir $(a + b)^n$ con $a^n + b^n$. Esta es la fuente más común de errores en el despeje de fórmulas de ingeniería.")

        st.markdown("<div class='subtitulo-profundo'>II. Radicación y Racionalización</div>", unsafe_allow_html=True)
        st.markdown("<div class='texto-profundo'>", unsafe_allow_html=True)
        st.write("""
        La radicación es la operación que extrae la raíz de una magnitud. Su importancia técnica reside en su interpretación como **exponente fraccionario**, lo que permite tratar raíces mediante el álgebra de potencias.
        """)
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div class='caja-ley'>", unsafe_allow_html=True)
        st.write("**Identidad Fundamental:**")
        st.latex(r"\sqrt[n]{a^m} = a^{m/n}")
        st.write("**Racionalización de Denominadores:**")
        st.write("En cálculos de precisión, no se permiten raíces en el denominador para evitar la propagación de errores decimales:")
        st.latex(r"\frac{1}{\sqrt{a}} = \frac{\sqrt{a}}{a}")
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div class='subtitulo-profundo'>III. Logaritmación: La Regla de Cálculo de la Naturaleza</div>", unsafe_allow_html=True)
        st.markdown("<div class='texto-profundo'>", unsafe_allow_html=True)
        st.write("""
        Los logaritmos son la operación inversa de la potencia. Su utilidad radica en su capacidad para **linealizar lo exponencial**. Gracias a ellos, podemos convertir multiplicaciones complejas en sumas simples y divisiones en restas.
        """)
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div class='caja-ley'>", unsafe_allow_html=True)
        st.write("**Propiedades Maestras:**")
        st.latex(r"\log_b(M \cdot N) = \log_b(M)
        # ==========================================
    # 1.4 JERARQUÍA DE OPERACIONES (VERSIÓN TÉCNICA AGUDA)
    # ==========================================
    elif capitulo == "1.4 Jerarquía de Operaciones":
        st.markdown("<div class='subtitulo-profundo'>1.4 El Protocolo Lógico: Jerarquía Operativa y GEMDAS</div>", unsafe_allow_html=True)
        
        st.markdown("<div class='texto-profundo'>", unsafe_allow_html=True)
        st.write("""
        ### I. La Arquitectura del Orden Matemático
        En matemáticas y programación de ingeniería, el orden de ejecución no es una sugerencia, sino una ley física del lenguaje. Sin un protocolo estricto, una expresión aritmética carecería de un valor unívoco, lo que resultaría en el colapso de cualquier cálculo estructural o algoritmo computacional. 
        
        El sistema moderno se rige bajo el acrónimo **GEMDAS** (Grupos, Exponentes, Multiplicación/División, Adición/Sustracción), el cual establece la precedencia de los operadores basándose en su complejidad funcional y su "energía" operativa.
        """)
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div class='caja-ley'>", unsafe_allow_html=True)
        st.subheader("II. El Protocolo de Prioridad Escalar")
        
        st.write("**Nivel 1: Signos de Agrupación (G)**")
        st.write("Paréntesis `()`, Corchetes `[]`, Llaves `{}` y barras de fracción. Su función es romper la jerarquía natural para dar prioridad a una operación específica. Son los 'interruptores' del flujo lógico.")
        
        st.write("**Nivel 2: Exponentes y Raíces (E)**")
        st.write("Operaciones de segundo orden. Se resuelven antes que las multiplicaciones debido a que representan una acumulación de intensidad mucho mayor.")
        
        st.write("**Nivel 3: Multiplicación y División (MD)**")
        st.write("Operaciones de primer orden. **Regla de Oro:** No hay prioridad de una sobre la otra; se ejecutan estrictamente de izquierda a derecha.")
        
        st.write("**Nivel 4: Adición y Sustracción (AS)**")
        st.write("El nivel base de la aritmética. Al igual que el nivel anterior, se resuelven de izquierda a derecha.")
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div class='subtitulo-profundo'>III. El Error de la Precedencia Horizontal</div>", unsafe_allow_html=True)
        st.markdown("<div class='texto-profundo'>", unsafe_allow_html=True)
        st.write("""
        El error más recurrente en el cálculo de campo y en la interpretación de fórmulas ocurre cuando se ignora la regla de **Izquierda a Derecha** en operaciones de igual rango. 
        
        Consideremos la siguiente expresión de flujo:
        """)
        st.latex(r"P = 12 \div 3 \times 2")
        st.write("""
        * **Interpretación Errónea:** Multiplicar antes que dividir ($12 \div 6 = 2$). 
        * **Interpretación Correcta:** Seguir el flujo de lectura ($4 \times 2 = 8$).
        
        En ingeniería, esta diferencia del 400% en el resultado puede ser la diferencia entre la estabilidad y el fallo de un sistema.
        """)
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div class='paso-a-paso'>", unsafe_allow_html=True)
        st.subheader("IV. Desglose de una Operación Compleja")
        st.write("Analicemos la resolución paso a paso de una fórmula integrada:")
        st.latex(r"E = 5 + [ 2 \cdot (3 + 1)^2 ] \div 4")
        
        st.write("**Paso 1 (Grupo Interno):** $3 + 1 = 4$")
        st.write("**Paso 2 (Exponente):** $4^2 = 16$")
        st.write("**Paso 3 (Multiplicación en Corchete):** $2 \cdot 16 = 32$")
        st.write("**Paso 4 (División):** $32 \div 4 = 8$")
        st.write("**Paso 5 (Adición Final):** $5 + 8 = 13$")
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div class='texto-profundo'>", unsafe_allow_html=True)
        st.write("""
        ### V. Jerarquía en Entornos Digitales
        Al trabajar con lenguajes como Python (que es el motor de esta aplicación), la jerarquía se respeta de forma estricta. Sin embargo, se recomienda el uso de paréntesis redundantes para mejorar la **legibilidad humana** y evitar errores de interpretación por parte de otros técnicos que revisen el código o la memoria de cálculo.
        """)
        st.markdown("</div>", unsafe_allow_html=True)
        # ==========================================
    # 1.5 PROPORCIONALIDAD Y REGLA DE TRES (VERSIÓN TÉCNICA INTEGRAL)
    # ==========================================
    elif capitulo == "1.5 Proporcionalidad y Regla de Tres":
        st.markdown("<div class='subtitulo-profundo'>1.5 Teoría de la Proporcionalidad: Relaciones Funcionales y Escalas</div>", unsafe_allow_html=True)
        
        st.markdown("<div class='texto-profundo'>", unsafe_allow_html=True)
        st.write("""
        ### I. La Proporcionalidad como Relación de Dependencia
        En el análisis técnico, rara vez una magnitud existe de forma aislada; la mayoría de los fenómenos físicos y sociales se definen por cómo una variable cambia en respuesta a otra. La proporcionalidad es el estudio de estas variaciones constantes. 
        
        Para un **Enlace Territorial** o un ingeniero, dominar la proporcionalidad es la diferencia entre un cálculo preciso de recursos y un error logístico crítico. No se trata solo de "cruzar datos", sino de entender la **razón de cambio**.
        """)
        st.markdown("</div>", unsafe_allow_html=True)

        col1, col2 = st.columns(2)
