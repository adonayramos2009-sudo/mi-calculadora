import streamlit as st

st.set_page_config(page_title="Calculadora Científica", page_icon="🧮")

st.title(" Calculadora Científica")
st.write("Proyecto Modulo 1.1")

n1 = st.number_input("Digite el primer número:", value=0.0)
n2 = st.number_input("Digite el segundo número:", value=0.0)

st.divider()

if st.button("Calcular Resultados"):
    addition = n1 + n2
    subtraction = n1 - n2
    multiplication = n1 * n2
    
    if n2 != 0:
        division = n1 / n2
    else:
        division = "Error: División por cero"
        
    power = n1 ** n2
    square_root_n1 = n1 ** 0.5

    st.subheader("Resultados:")
    st.success(f"Suma: {addition}")
    st.success(f"Resta: {subtraction}")
    st.success(f"Multiplicación: {multiplication}")
    
    if n2 != 0:
        st.success(f"División: {division}")
    else:
        st.error(division)
        
    st.info(f"Potencia: {power}")
    st.info(f"Raíz cuadrada del primer número: {square_root_n1}")
