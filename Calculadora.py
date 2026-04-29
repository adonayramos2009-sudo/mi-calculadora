import streamlit as st

## ...existing code...
def calcular_web():
    st.title("Calculadora Científica")
    st.write("Proyecto para software")
    n1 = st.number_input("Digite elprimer número: ")
    n2 = st.number_input("Digite el segundo número: ")
    if st.button("Calcular"):
        addition = n1 + n2
        subtraction = n1 - n2
        multiplication = n1 * n2
        division = n1 / n2
        power = n1 ** n2
        square_root_n1 = n1 ** 0.5
        if n2 >= 0:
            st.write("Suma: ", addition)
        st.write("Resta: ", subtraction)
        st.write("Multiplicación: ", multiplication)
        st.write("División: ", division)
        st.write("Potencia: ", power)
        st.write("Raíz cuadrada del primer número: ", square_root_n1)   
# ...existing code...