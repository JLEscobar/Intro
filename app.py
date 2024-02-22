import streamlit as st
from PIL import Image
st.title("mi primera app")

st.header("En este espacio comiezo a desarrollar mis aplicaciones para interfaces multimodales")
st.write("facilmente pudo realizar banked y fronted")
image = Image.open("Avatar_belial.png")


st.image(image, caption='Que pasa!!!!')

texto = st.text_input('my besto frendo', 'itadori iuji')
st.write('vira goes brrr',texto)

st.subheader('breve anuncio')
col1,col2 = st.columns(2)

with col1:
  st.subheader('Esta es una columna')
  st.write('aplausos gente aplausos')
  resp = st.checkbox('belial es god')
  if resp:
    st.write('correcto')
