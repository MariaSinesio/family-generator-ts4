import streamlit as st
from script import generate_sim


st.markdown("<h1 style='color: #1C83E1; font-size: 3em;'>The Sims Generator</h1>", unsafe_allow_html=True) # Texto estilizado e unsafe 

col1, col2, col3 = st.columns([1, 3, 1])

with col2:
 st.video("video/video.mp4", width=300, autoplay=True, loop=True)

st.subheader("Sorteie seu :blue[sim] único!")

gender = st.text_input("Escolha o gênero do seu primeiro sim: (Masculine/Female)")

if st.button("Gerar sim"):
    result = generate_sim(gender)

    st.code(result)




