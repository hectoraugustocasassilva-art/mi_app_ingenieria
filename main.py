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

    # ==========================================
    # CAPÍTULO 1.1: LOS SIGNOS
    # ==========================================
    if capitulo == "1.1 Los Signos y la Lógica Operativa (Completo)":
        st.markdown("<div class='subtitulo-profundo'>1.1 El Dominio de los Signos: Más allá de las reglas</div>", unsafe_allow_html=True)
        
        st.markdown("<div class='texto-profundo'>", unsafe_allow_html=True)
        st.write("""
        ### I. La Naturaleza de la Dualidad Numérica
        En matemáticas, el signo no es un objeto, es un **operador de simetría**. Todo número real $a$ tiene un gemelo opuesto $-a$, tal que al juntarse recuperan el equilibrio original: el **Cero**.
        
        Esta relación se basa en el **Axioma del Inverso Aditivo**. Sin este fundamento, no existiría el álgebra, ya que no podríamos "cancelar" términos de un lado a otro de una ecuación.
        """)
        st.markdown("</div>", unsafe_allow_html=True)

        st.subheader("II. Estructura de la Adición (Suma y Resta)")
        st.write("Para dominar la suma de signos, debemos entender tres propiedades fundamentales:")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("<div class='caja-ley'>", unsafe_allow_html=True)
            st.write("**1. Propiedad de Clausura:**")
            st.write("La suma de dos números reales siempre es otro número real.")
            st.latex(r"a, b \in \mathbb{R} \implies (a+b) \in \mathbb{R}")
            
            st.write("**2. Elemento Neutro (Identidad):**")
            st.write("El cero no altera la magnitud ni el signo.")
            st.latex(r"a + 0 = a")
            st.markdown("</div>", unsafe_allow_html=True)
            
        with col2:
            st.markdown("<div class='caja-ley'>", unsafe_allow_html=True)
            st.write("**3. Propiedad Conmutativa:**")
            st.write("El orden de los sumandos no altera la dirección final.")
            st.latex(r"a + (-b) = (-b) + a")
            
            st.write("**4. Inverso Aditivo (Simetría):**")
            st.latex(r"a + (-a) = 0")
            st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div class='subtitulo-profundo'>III. Leyes de la Multiplicación: El Efecto Espejo</div>", unsafe_allow_html=True)
        st.write("""
        La multiplicación por un signo negativo es una **transformación lineal**. 
        Imagina que el signo positivo $(+)$ es 'mantener' y el signo negativo $(-)$ es 'invertir'.
        """)

        st.markdown("<div class='caja-ley'>", unsafe_allow_html=True)
        st.latex(r"\text{Ley 1: } (+) \times (+) = (+) \quad \text{(Mantener lo que se mantiene)}")
        st.latex(r"\text{Ley 2: } (-) \times (+) = (-) \quad \text{(Invertir lo que se mantiene)}")
        st.latex(r"\text{Ley 3: } (+) \times (-) = (-) \quad \text{(Mantener lo que está invertido)}")
        st.latex(r"\text{Ley 4: } (-) \times (-) = (+) \quad \text{(Invertir lo que ya estaba invertido)}")
        st.markdown("</div>", unsafe_allow_html=True)

        st.subheader("IV. Casos de Análisis Crítico")
        st.markdown("<div class='paso-a-paso'>", unsafe_allow_html=True)
        st.write("**Caso 1: Signos en Potencias (Diferencia Vital)**")
        st.write("No es lo mismo $-a^n$ que $(-a)^n$.")
        st.latex(r"-3^2 = -(3 \times 3) = -9")
        st.latex(r"(-3)^2 = (-3) \times (-3) = 9")
        st.write("*Explicación:* En el primer caso, el signo no está afectado por la potencia. En el segundo, el signo se multiplica por sí mismo.")
        
        st.write("**Caso 2: El signo en la División (Fracciones)**")
        st.write("El signo puede estar en cualquier lugar, pero el valor es el mismo.")
        st.latex(r"\frac{-a}{b} = \frac{a}{-b} = -\frac{a}{b}")
        st.markdown("</div>", unsafe_allow_html=True)

        st.subheader("V. Resumen de Ejecución para el Estudiante")
        st.info("""
        1. **Para Sumar:** Si los signos pelean (son diferentes), gana el más grande y se llevan la diferencia.
        2. **Para Multiplicar:** Cuenta los signos negativos. Si el total de negativos es PAR, el resultado es POSITIVO. Si es IMPAR, es NEGATIVO.
        """)

    # ==========================================
    # CAPÍTULO 1.2: FRACCIONES
    # ==========================================
    elif capitulo == "1.2 Fracciones, Decimales y Porcentajes (Completo)":
        st.markdown("<div class='subtitulo-profundo'>1.2 El Dominio de las Partes: Racionales y Proporciones</div>", unsafe_allow_html=True)

        st.markdown("<div class='texto-profundo'>", unsafe_allow_html=True)
        st.write("""
        ### I. ¿Por qué inventamos las fracciones?
        Los números enteros sirven para contar objetos completos. Pero la aritmética de los enteros se rompe cuando quieres medir algo continuo (como el agua) o repartir. 
        Ahí nace el conjunto de los **Números Racionales ($\mathbb{Q}$)**. 
        
        Una fracción no es un número extraño, es una **división pausada** o "congelada". Es la relación exacta entre la parte y el todo.
        """)
        st.markdown("</div>", unsafe_allow_html=True)

        st.subheader("II. Anatomía y la Regla del Cero")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("<div class='caja-ley'>", unsafe_allow_html=True)
            st.write("**Estructura Base:**")
            st.latex(r"\frac{a}{b} = \frac{\text{Numerador (Partes que tomas)}}{\text{Denominador (Partes en que cortas)}}")
            st.write("*Condición absoluta:* $b \neq 0$. ¿Por qué? Porque no puedes cortar un objeto en 'cero' pedazos. La división por cero destruye las reglas de la matemática y no tiene solución.")
            st.markdown("</div>", unsafe_allow_html=True)
            
        with col2:
            st.markdown("<div class='caja-ley'>", unsafe_allow_html=True)
            st.write("**Fracciones Equivalentes:**")
            st.write("Si multiplicas o divides arriba y abajo por el mismo número, el valor real no cambia.")
            st.latex(r"\frac{a}{b} = \frac{a \cdot k}{b \cdot k}")
            st.write("*Ejemplo:* $\\frac{1}{2}$ es exactamente lo mismo que $\\frac{50}{100}$.")
            st.markdown("</div>", unsafe_allow_html=True)

        st.subheader("III. Operaciones: La Lógica del Tamaño")
        st.write("El mayor error es sumar el de arriba con el de arriba, y el de abajo con el de abajo. Hacer eso viola las leyes de la física y la proporción.")

        st.markdown("<div class='paso-a-paso'>", unsafe_allow_html=True)
        st.write("**A. Suma y Resta (El problema del Mínimo Común Múltiplo - MCM)**")
        st.write("No puedes sumar tercios con cuartos directamente. Tienen tamaños distintos. El MCM sirve para encontrar un 'tamaño de corte' en el que ambas fracciones encajen perfectamente.")
        st.latex(r"\frac{a}{b} \pm \frac{c}{d} = \frac{(a \cdot d) \pm (b \cdot c)}{b \cdot d}")
        st.write("*Nota:* Esta 'fórmula cruzada' sirve rápido para dos fracciones. Para tres o más, se debe usar el MCM de los denominadores para no obtener números gigantes.")
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div class='caja-ley'>", unsafe_allow_html=True)
        st.write("**B. Multiplicación (Una parte de otra parte)**")
        st.write("Multiplicar fracciones es directo. Conceptualmente, significa sacar 'la mitad de la tercera parte'.")
        st.latex(r"\frac{a}{b} \cdot \frac{c}{d} = \frac{a \cdot c}{b \cdot d}")

        st.write("**C. División (Ley de Extremos y Medios o 'La Oreja')**")
        st.write("Dividir fracciones equivale a multiplicar por la primera fracción pero con la segunda invertida.")
        st.latex(r"\frac{\frac{a}{b}}{\frac{c}{d}} = \frac{a \cdot d}{b \cdot c}")
        st.markdown("</div>", unsafe_allow_html=True)

        st.subheader("IV. Decimales y Porcentajes: Distintos idiomas, mismo número")
        st.markdown("<div class='texto-profundo'>", unsafe_allow_html=True)
        st.write("""
        * **El Decimal:** Es solo una fracción cuyo denominador es siempre una potencia de 10 (10, 100, 1000). 
            Ejemplo: $0.75$ es matemáticamente igual a $\\frac{75}{100}$. Al simplificarlo (dividir arriba y abajo entre 25), nos da $\\frac{3}{4}$.
        * **El Porcentaje (%):** Es la herramienta universal para comparar cosas. Significa literalmente 'por cada cien'. Convertir todo a base 100 nos permite saber rápidamente qué cantidad es más grande sin importar el tamaño original.
        """)
        st.markdown("</div>", unsafe_allow_html=True)
