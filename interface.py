import streamlit as st
from script import generate_sim

col1, col2 = st.columns([2,1])

with col1:

  st.header("The Sims Generator")

with col2:
  st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExMHA0eWh5Ym5lMzBmNjFiaTJwanM2cTg2cDZycDI1cmFqaDJzbTA5byZlcD12MV9naWZzX3NlYXJjaCZjdD1n/l2JJFTQqEB7phtZAc/giphy.gif", width=200)

st.subheader("Sorteie seu :gray[sim] único!")

gender = st.text_input("Escolha o gênero do seu primeiro sim: (Masculine/Female)")

if st.button("Gerar sim"):
    result = generate_sim(gender)

    st.code(result)
    
else:
   st.write("Digite __female__ ou __masculine__ para gerar o sim desejado")



