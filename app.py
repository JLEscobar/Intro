import streamlit as st
from PIL import Image
st.title("mi primera app")

st.header("En este espacio comiezo a desarrollar mis aplicaciones para interfaces multimodales")
st.write("facilmente pudo realizar banked y fronted")
image = Image.open("Avatar_belial.png")


st.image(image, caption='Que pasa!!!!')

texto = st.text_input('my besto frendo', 'itadori yuji')
st.write('Solo quiero a Takada-chan y a',texto,' mi besto frendo')

st.subheader('breve anuncio')
col1,col2 = st.columns(2)

with col1:
  st.subheader('Esta es una columna')
  st.write('aplausos gente aplausos')
  resp = st.checkbox('belial es god?')
  if resp:
    st.write('efectivamente brodah')
    
with col2:
  st.subheader('Estas en peligro brodah')
  modo = st.radio('Si tuvieras que elegir uno cual escogerias', ('Yuri','Cammy','Zangief'))
                  
  if modo == 'Yuri':
      st.write('te gustan los niños y el fbi esta llegando, no para capturarte, sino para asesinarte')
  if modo == 'Cammy':
      st.write('Eres un hombre de gustos basicos y simples, pero que nadie te diga que esta mal, por que son buenos, todos vimos ese poto')
  if modo == 'Zangief':
      st.write('Eres o muy basado o te gusta comer crayones, no tienes puunto medio')
