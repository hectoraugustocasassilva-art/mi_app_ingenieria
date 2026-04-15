import streamlit as st

st.set_page_config(page_title="Academia de Ciencias Básicas", layout="wide")

st.title("📚 Academia de Ciencias: De lo Básico a lo Avanzado")
st.markdown("---")

# Menú lateral por niveles de aprendizaje
nivel = st.sidebar.selectbox("Selecciona tu Nivel:", 
    ["1. Aritmética (El origen de los números)", 
     "2. Álgebra (El lenguaje de los símbolos)", 
     "3. Geometría y Trigonometría",
     "4. Física General (Leyes del Universo)",
     "5. Química General (La Materia)"])

if nivel == "1. Aritmética (El origen de los números)":
    st.header("🔢 Nivel 1: Aritmética")
    
    with st.expander("La Lógica de los Signos (¿Por qué menos por menos es más?)", expanded=True):
        st.write("No es una regla caprichosa. Imagina una recta numérica:")
        st.latex(r"(-1) \cdot (-1) = 1")
        st.write("**Explicación:** Multiplicar por -1 significa 'dar media vuelta' en la recta. Si multiplicas por -1 una vez, miras a la izquierda. Si vuelves a multiplicar por -1, das otra media vuelta y terminas mirando a la derecha (el lado positivo).")

    with st.expander("Fracciones: Partiendo la Unidad"):
        st.write("Una fracción es una división indicada. De aquí nace todo el cálculo.")
        st.latex(r"\frac{a}{b} + \frac{c}{d} = \frac{ad + bc}{bd}")
        st.write("**Deducción:** No podemos sumar cosas de distinto tamaño (denominador). Esta fórmula busca un 'tamaño común' para poder juntar las piezas.")

elif nivel == "2. Álgebra (El lenguaje de los símbolos)":
    st.header("📐 Nivel 2: Álgebra General")
    
    st.subheader("Potenciación y sus Leyes")
    st.write("¿De dónde sale que cualquier número elevado a la 0 es 1?")
    st.latex(r"x^0 = 1")
    st.write("**Deducción:** Si sabemos que $x^a / x^a = 1$ (porque cualquier cosa dividida entre sí misma es 1), y por leyes de exponentes restamos: $a - a = 0$. Por lo tanto, $x^0$ debe ser 1.")

    st.subheader("Productos Notables")
    st.latex(r"(a + b)^2 = a^2 + 2ab + b^2")
    st.info("💡 **Visualización:** Imagina un cuadrado de lado (a+b). Su área total es un cuadrado grande ($a^2$), un cuadrado pequeño ($b^2$) y dos rectángulos ($ab$).")

elif nivel == "3. Geometría y Trigonometría":
    st.header("📐 Nivel 3: El estudio del espacio")
    
    st.subheader("Teorema de Pitágoras (Deducción Real)")
    st.latex(r"a^2 + b^2 = c^2")
    st.write("Este teorema no es solo una fórmula; es la relación de áreas. El área del cuadrado construido sobre la hipotenusa es igual a la suma de las áreas de los cuadrados de los catetos.")
    
    st.subheader("Trigonometría: El círculo unitario")
    st.latex(r"\sin^2(\theta) + \cos^2(\theta) = 1")
    st.write("Esta es la identidad fundamental. Sale directamente de Pitágoras cuando el radio del círculo es 1.")

elif nivel == "4. Física General (Leyes del Universo)":
    st.header("🌌 Nivel 4: Física desde Cero")
    
    st.subheader("Cinemática: ¿Cómo medimos el movimiento?")
    st.write("Antes de ver fuerzas, hay que entender la distancia y el tiempo.")
    st.latex(r"v = \frac{\Delta d}{\Delta t}")
    st.write("**Deducción:** La velocidad es el cambio de posición en un intervalo de tiempo. Si recorres 100 metros en 10 segundos, tu razón de cambio es 10 m/s.")

elif nivel == "5. Química General (La Materia)":
    st.header("🧪 Nivel 5: Química Básica")
    
    st.subheader("El Átomo y la Tabla Periódica")
    st.write("Todo lo que ves está hecho de Protones, Neutrones y Electrones.")
    st.latex(r"A = Z + N")
    st.write("**Fórmula de Masa Atómica:** A (Masa) es igual a Z (Protones) más N (Neutrones).")

st.sidebar.markdown("---")
st.sidebar.write("📖 **Estado:** Aprendizaje General")
