import streamlit as st
from script import generate_sim
from script import generate_family

st.set_page_config(page_title="PersonaGen", layout="wide")

# st.markdown("<h1 style='color: #1C83E1; font-size: 3em;'>PersonaGen</h1>", unsafe_allow_html=True) # Texto estilizado e unsafe 

col1, col2, col3 = st.columns([1, 3, 1])

with col1:
   st.markdown("<h1 style='color: #1C83E1; font-size: 3em;'>PersonaGen</h1>", unsafe_allow_html=True) # Texto estilizado e unsafe 

with col2:
 st.video("video/video.mp4", width=120, autoplay=True, loop=True)

# st.subheader("Sorteie seu :blue[sim] único!")

with st.container(horizontal=False):
    st.subheader("Sorteie seu :blue[sim] único!")
    st.space("small")
    st.markdown("<p style: ffd166; text-align: center><em>Esse é um projeto feito de fã para fã!</em></p>", unsafe_allow_html=True)
    st.space("small")

gender = st.text_input("Escolha o gênero do seu primeiro sim: (Masculine/Female)")

if st.button("Gerar sim"):
    result_sim = generate_sim(gender)
    result_family = generate_family()
    st.code(result_sim)
    st.code(result_family)


