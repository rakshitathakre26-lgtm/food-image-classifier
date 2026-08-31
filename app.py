import streamlit as st
from google import genai
from PIL import Image
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

st.title("🍔 Food Image Classifier")

st.write("Upload an image of food and Gemini will identify it.")

uploaded_file = st.file_uploader(
    "Upload a food image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.image(image, caption="Uploaded Food Image", use_container_width=True)

    if st.button("Identify Food"):

        with st.spinner("Identifying food..."):

            response = client.models.generate_content(
                model="gemini-3.6-flash",
                contents=[
                    image,
                    "Identify the food in this image. Give the most likely food name and briefly explain what it is."
                ]
            )

            st.subheader("Result")
            st.write(response.text)