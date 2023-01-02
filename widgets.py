import os
import base64
import streamlit as st
from deepface import DeepFace


def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )


def image_analzyer():
    uploaded_file = st.file_uploader("Upload an image file")

    if uploaded_file is not None:
        # Show Image
        st.image(uploaded_file, caption='Uploaded Image')
        st.write("Note: Running for the first time will download models. This will take some time.")
        
        open(os.path.join("tempDir",uploaded_file.name),"wb").write(uploaded_file.getbuffer())

        # Analyze Face
        results = DeepFace.analyze(img_path='tempDir/'+uploaded_file.name)

        # Print results
        st.write(results)

def live_analzyer():
    if st.button('Click to enable live analysis'):
        DeepFace.stream()
