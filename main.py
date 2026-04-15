elif capitulo == "1.2 Fracciones, Decimales y Porcentajes":
        st.markdown("<div class='subtitulo-profundo'>1.2 El Dominio de las Partes: Racionales y Proporciones</div>", unsafe_allow_html=True)

        # --- SECCIÓN 1: FILOSOFÍA DE LA FRACCIÓN ---
        st.markdown("<div class='texto-profundo'>", unsafe_allow_html=True)
        st.write("""
        ### I. ¿Por qué inventamos las fracciones?
        Los números enteros sirven para contar objetos completos. Pero la aritmética de los enteros se rompe cuando quieres medir algo continuo (como el agua) o repartir. 
        Ahí nace el conjunto de los **Números Racionales ($\mathbb{Q}$)**. 
        
        Una fracción no es un número extraño, es una **división pausada** o "congelada". Es la relación exacta entre la parte y el todo.
        """)
        st.markdown("</div>", unsafe_allow_html=True)

        # --- SECCIÓN 2: ANATOMÍA ---
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

        # --- SECCIÓN 3: LAS OPERACIONES EXPLICADAS ---
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

        # --- SECCIÓN 4: DECIMALES Y PORCENTAJES ---
        st.subheader("IV. Decimales y Porcentajes: Distintos idiomas, mismo número")
        st.markdown("<div class='texto-profundo'>", unsafe_allow_html=True)
        st.write("""
        * **El Decimal:** Es solo una fracción cuyo denominador es siempre una potencia de 10 (10, 100, 1000). 
            Ejemplo: $0.75$ es matemáticamente igual a $\\frac{75}{100}$. Al simplificarlo (dividir arriba y abajo entre 25), nos da $\\frac{3}{4}$.
        * **El Porcentaje (%):** Es la herramienta universal para comparar cosas. Significa literalmente 'por cada cien'. Convertir todo a base 100 nos permite saber rápidamente qué cantidad es más grande sin importar el tamaño original.
        """)
        st.markdown("</div>", unsafe_allow_html=True)
