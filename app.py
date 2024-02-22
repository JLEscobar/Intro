import streamlit as st
from PIL import Image
st.title("mi primera app")

st.header("En este espacio comiezo a desarrollar mis aplicaciones para interfaces multimodales")
st.write("facilmente pudo realizar banked y fronted")
image = Image.open("Avatar_balial.png")

st.image(image, caption'Avatar belial')
