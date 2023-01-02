import base64
import streamlit as st
from widgets import *

# Title and Layout
st.title('Face Describer')

# Live Feed
live_analzyer()

# Image Analzyer
image_analzyer()

# Background
add_bg_from_local(image_file='background.jpg')

# Hide "Made with Streamlit"
add_bg_from_local('background.jpg')  

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
