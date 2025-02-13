import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import base64
import os

# Function to add background image
def add_bg_from_local(image_file):
    with open(image_file, "rb") as f:
        encoded_string = base64.b64encode(f.read()).decode()
    bg_image = f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{encoded_string}");
        background-size: cover;
        background-position: center;
    }}
    </style>
    """
    st.markdown(bg_image, unsafe_allow_html=True)

# Set background
background_path = "background.jpg"  # Ensure the correct path
add_bg_from_local(background_path)

# Load the trained model
@st.cache_resource
def load_model():
    model = tf.keras.models.load_model("models/potato_disease_model.keras")
    return model

model = load_model()

# Define class labels
CLASS_NAMES = ["Early Blight", "Healthy", "Late Blight"]

# Function to preprocess the image
def preprocess_image(image):
    image = image.resize((128, 128))  # Resize to match model input
    image = np.array(image) / 255.0  # Normalize pixel values
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    return image

# Streamlit UI
st.title("🍃 Potato Disease Detection")
st.subheader("Upload an image to predict the disease")

# Upload Image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Show uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Predict button
    if st.button("Predict"):
        with st.spinner("🔍 Analyzing... Please wait!"):
            processed_image = preprocess_image(image)
            prediction = model.predict(processed_image)
            predicted_class = CLASS_NAMES[np.argmax(prediction)]

        # Display result
        st.subheader("Prediction:")
        st.write(f"🌿 *{predicted_class}*")