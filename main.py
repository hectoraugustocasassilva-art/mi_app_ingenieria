if capitulo == "1.1 Los Signos y la Lógica Operativa (Completo)":
        st.markdown("<div class='subtitulo-profundo'>1.1 El Dominio de los Signos: Más allá de las reglas</div>", unsafe_allow_html=True)
        
        # --- SECCIÓN 1: INTRODUCCIÓN FILOSÓFICA ---
        st.markdown("<div class='texto-profundo'>", unsafe_allow_html=True)
        st.write("""
        ### I. La Naturaleza de la Dualidad Numérica
        En matemáticas, el signo no es un objeto, es un **operador de simetría**. Todo número real $a$ tiene un gemelo opuesto $-a$, tal que al juntarse recuperan el equilibrio original: el **Cero**.
        
        Esta relación se basa en el **Axioma del Inverso Aditivo**. Sin este fundamento, no existiría el álgebra, ya que no podríamos "cancelar" términos de un lado a otro de una ecuación.
        """)
        st.markdown("</div>", unsafe_allow_html=True)

        # --- SECCIÓN 2: LEYES DE LA ADICIÓN Y PROPIEDADES ---
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

        # --- SECCIÓN 3: DEDUCCIÓN PROFUNDA DE LA MULTIPLICACIÓN ---
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

        # --- SECCIÓN 4: CASOS COMPLEJOS Y ERRORES COMUNES ---
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

        # --- SECCIÓN 5: APLICACIÓN PRÁCTICA ---
        st.subheader("V. Resumen de Ejecución para el Estudiante")
        st.info("""
        1. **Para Sumar:** Si los signos pelean (son diferentes), gana el más grande y se llevan la diferencia.
        2. **Para Multiplicar:** Cuenta los signos negativos. Si el total de negativos es PAR, el resultado es POSITIVO. Si es IMPAR, es NEGATIVO.
        """)
