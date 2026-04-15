import streamlit as st
import numpy as np

# Configuración de interfaz profesional
st.set_page_config(page_title="Ingeniero Pro - UMNG", layout="wide")

# Estilo visual de "Pizarra de Profesor"
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stMarkdown h1, h2, h3 { color: #1e3a8a; }
    .stAlert { border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- BARRA LATERAL (NAVEGACIÓN) ---
st.sidebar.title("🏗️ Menú de Aprendizaje")
st.sidebar.info("Estudiante: Hector Augusto\nMeta: Experto en Ing. Civil")

modulo = st.sidebar.radio("Selecciona tu Área de Estudio:", 
    ["1. Matemáticas (Desde la Suma)", "2. Física (Lógica del Movimiento)", "3. Química (Materiales de Obra)", "4. Laboratorio de Ejercicios"])

# --- MODULO 1: MATEMÁTICAS ---
if modulo == "1. Matemáticas (Desde la Suma)":
    st.header("🧮 Matemáticas: De la Aritmética al Cálculo")
    
    tab1, tab2, tab3 = st.tabs(["Lógica Inicial", "Álgebra (La Balanza)", "Cálculo (El Cambio)"])
    
    with tab1:
        st.subheader("El Origen: Suma y Resta")
        st.write("En ingeniería, la suma no es solo juntar números, es **Acumulación**. La resta es **Diferencia de Nivel**.")
        st.latex(r"\Delta h = h_{final} - h_{inicial}")
        st.info("**Explicación del Profesor:** Esta fórmula es la base de la Topografía. Si restas la altura de llegada menos la de salida, tienes el desnivel. Todo nace de una simple resta.")

    with tab2:
        st.subheader("Álgebra: ¿De dónde sale la 'X'?")
        st.write("La 'X' es simplemente el dato que te falta en la obra. El álgebra es el arte de mantener el **Equilibrio**.")
        st.latex(r"Ax + B = C")
        st.markdown("**Deducción Paso a Paso:**")
        st.write("1. Tienes una igualdad (una balanza equilibrada).")
        st.write("2. Si quieres despejar X, debes quitar lo que le estorba haciendo lo opuesto en ambos lados.")
        st.success("Fórmula: $x = (C - B) / A$. ¡No la memorices, solo mueve las pesas de la balanza!")

    with tab3:
        st.subheader("Cálculo: La Derivada")
        st.write("La derivada es la **Pendiente** de cualquier cosa.")
        st.latex(r"f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}")
        st.warning("**¿Por qué existe esta fórmula?** Porque en una carretera curva, la inclinación cambia a cada milímetro. La derivada mide ese cambio exacto.")

# --- MODULO 2: FÍSICA ---
elif modulo == "2. Física (Lógica del Movimiento)":
    st.header("🍎 Física Mecánica y Estática")
    
    st.subheader("La Fórmula Maestra: Fuerza")
    st.latex(r"F = m \cdot a")
    st.write("**Desglose:** F (Empuje), m (Masa/Material), a (Aceleración).")
    
    with st.expander("Deducción de la Estática (Para Edificios)"):
        st.write("Si quieres que un puente no se caiga, la aceleración debe ser cero ($a=0$).")
        st.latex(r"\sum F = 0")
        st.info("Esta es la 'Fórmula del Reposo'. Si la suma de fuerzas no da cero, tu estructura se está moviendo (y eso es un desastre).")

# --- MODULO 3: QUÍMICA ---
elif modulo == "3. Química (Materiales de Obra)":
    st.header("⚗️ Química de Materiales")
    st.subheader("La Reacción de Hidratación")
    st.write("El cemento no se seca por aire, se 'cura' por una reacción química con el agua.")
    st.latex(r"2Ca_3SiO_5 + 7H_2O \to 3CaO \cdot 2SiO_2 \cdot 4H_2O + 3Ca(OH)_2")
    st.write("**Explicación:** Esta fórmula explica cómo el polvo se convierte en piedra creando cristales que se amarran entre sí. Si echas mucha agua, los cristales quedan muy lejos y el concreto es débil.")

# --- MODULO 4: EJERCICIOS ---
elif modulo == "4. Laboratorio de Ejercicios":
    st.header("📝 Retos de Ingeniería")
    st.write("Pon a prueba tu lógica de experto.")
    
    problema = st.selectbox("Elige un reto:", ["Cálculo de Pendiente en Obra", "Dosificación de Mezcla"])
    
    if problema == "Cálculo de Pendiente en Obra":
        dist_h = st.number_input("Distancia Horizontal (metros):", value=10.0)
        dist_v = st.number_input("Altura que sube (metros):", value=2.0)
        pendiente = (dist_v / dist_h) * 100
        st.metric("Pendiente Calculada", f"{pendiente}%")
        st.write(f"**Análisis:** Si esto fuera una carretera, una pendiente del {pendiente}% requiere diseño especial según la norma.")

st.sidebar.markdown("---")
st.sidebar.write("✅ **App Lista para Estudiar**")
