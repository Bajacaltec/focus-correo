import streamlit as st
from streamlit_lottie import st_lottie
import requests


st.title('Gracias por ponerte en contacto con nosotros')
st.subheader('En breve recibiras un correo electrónico de nuestra parte')

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
gracias=load_lottieurl('https://assets2.lottiefiles.com/packages/lf20_vzy3decs.json')
st_lottie(gracias,height=250)
