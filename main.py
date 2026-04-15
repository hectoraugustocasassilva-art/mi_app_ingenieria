import streamlit as st

# Configuración de página para máxima lectura
st.set_page_config(page_title="Enciclopedia Universal de Ciencias", layout="wide")

# --- DISEÑO DE INTERFAZ ---
st.markdown("""
    <style>
    .titulo-tomo { color: #1e3a8a; font-size: 40px; font-weight: bold; border-bottom: 3px solid #1e3a8a; }
    .seccion-lectura { background-color: #ffffff; padding: 30px; border-radius: 10px; line-height: 1.6; font-size: 18px; }
    .destaque { background-color: #e0f2fe; padding: 15px; border-radius: 5px; border-left: 5px solid #0369a1; margin: 20px 0; }
    </style>
    """, unsafe_allow_html=True)

# --- SISTEMA DE NAVEGACIÓN ---
st.sidebar.title("📚 Biblioteca Total")
tomo = st.sidebar.selectbox("Seleccionar Tomo:", 
    ["Tomo I: Aritmética (El origen)", "Tomo II: Álgebra (Generalización)", "Tomo III: Geometría", "Tomo IV: Física", "Tomo V: Química"])

# --- CONTENIDO DEL TOMO I: ARITMÉTICA ---
if tomo == "Tomo I: Aritmética (El origen)":
    st.markdown("<div class='titulo-tomo'>Tomo I: El Arte de Contar y la Lógica Numérica</div>", unsafe_allow_html=True)
    
    capitulo = st.sidebar.radio("Capítulos del Tomo I:", [
        "1.1 Filosofía de la Unidad", 
        "1.2 Sistemas de Numeración (Historia y Lógica)", 
        "1.3 Operaciones Fundamentales (Deducción)", 
        "1.4 Fracciones y la Partición del Todo",
        "1.5 Potenciación y Radicación desde Cero"
    ])

    if capitulo == "1.1 Filosofía de la Unidad":
        st.write("## 1.1 ¿Qué es un número? El origen de la abstracción")
        st.markdown("""
        <div class='seccion-lectura'>
        Las matemáticas no nacen con la escritura, nacen con la capacidad del cerebro de separar un objeto del resto. 
        A esto lo llamamos <b>Unidad</b>. 
        
        ### El Concepto de Conjunto
        Antes de sumar, el ser humano tuvo que entender que varios objetos pueden ser vistos como un solo grupo. 
        Si tienes tres piedras, la mente hace un salto increíble: deja de ver "piedra, piedra, piedra" y empieza a ver el concepto "3".
        
        ### La Recta Numérica: El Mapa del Universo
        La recta es el fundamento de todo. Imagina una línea que no tiene fin en ninguna dirección. 
        - El <b>Cero (0)</b>: No es "nada", es el punto de origen, el equilibrio.
        - Los <b>Positivos</b>: Representan lo que "es" o lo que avanza.
        - Los <b>Negativos</b>: Representan la dirección opuesta, la deuda o lo que falta.
        </div>
        """, unsafe_allow_html=True)
        st.latex(r"x \in \mathbb{R} \quad \text{donde } -\infty < x < +\infty")

    elif capitulo == "1.3 Operaciones Fundamentales (Deducción)":
        st.write("## 1.3 Deducción de las Operaciones")
        
        with st.expander("Deducción de la Suma y la Resta", expanded=True):
            st.write("""
            La suma es **acumulación**. Si defines $1+1=2$, estás definiendo que dos unidades juntas crean una nueva categoría.
            
            **La Resta:** No existe como operación independiente. Restar es simplemente sumar un número negativo.
            """)
            st.latex(r"a - b = a + (-b)")
            st.info("Fundamento: Por eso las reglas de los signos funcionan. Restar una deuda es lo mismo que recibir dinero.")

        with st.expander("Deducción de la Multiplicación", expanded=True):
            st.write("""
            La multiplicación es una **suma abreviada**. 
            """)
            st.latex(r"a \cdot n = \underbrace{a + a + \dots + a}_{n \text{ veces}}")
            st.write("Si entiendes esto, entiendes por qué cualquier número multiplicado por 0 es 0: porque estás sumando algo 'cero veces'.")

    elif capitulo == "1.4 Fracciones y la Partición del Todo":
        st.write("## 1.4 Fracciones: La Lógica de la Parte")
        st.markdown("""
        <div class='seccion-lectura'>
        Una fracción no es un número extraño, es un <b>Operador</b>. 
        - El <b>Denominador</b> (el de abajo): Te dice en cuántas partes cortaste la unidad.
        - El <b>Numerador</b> (el de arriba): Te dice cuántas de esas partes tienes en la mano.
        
        ### ¿Por qué no se pueden sumar fracciones con distinto denominador directamente?
        Porque no puedes sumar "peras con manzanas". Si tienes 1/2 (media naranja) y 1/3 (un tercio de naranja), los trozos son de distinto tamaño. 
        Necesitas el <b>Mínimo Común Múltiplo</b> para cortar todos los trozos del mismo tamaño antes de juntarlos.
        </div>
        """, unsafe_allow_html=True)
        st.latex(r"\frac{a}{b} + \frac{c}{d} = \frac{ad + bc}{bd}")

# --- (ESPACIO PARA TOMO II, III, IV, V) ---
# Aquí iremos pegando los "Libros" completos de Álgebra, Física y Química.

elif tomo == "Tomo II: Álgebra (Generalización)":
    st.write("# Tomo II: Álgebra - El Lenguaje de los Símbolos")
    st.write("Contenido en construcción: Aquí cargaremos el libro completo de Álgebra.")

st.sidebar.markdown("---")
st.sidebar.write("🧪 **Fuentes:** Stewart, Baldor, Resnick, Serway.")
