import streamlit as st
import numpy as np
import cv2
from tensorflow.keras.models import load_model
from PIL import Image

# ==========================
# Load Model
# ==========================

model = load_model("model/emotion_model.h5")

emotion_labels = ['Angry','Disgust','Fear','Happy','Sad','Surprise','Neutral']

st.title("😊 Intelligent Emotion Recognition System")

uploaded_file = st.file_uploader("Upload a facial image", type=['jpg','png','jpeg'])

if uploaded_file is not None:
    
    image = Image.open(uploaded_file).convert('L')
    image = image.resize((48,48))
    
    img_array = np.array(image)/255.0
    img_array = img_array.reshape(1,48,48,1)
    
    prediction = model.predict(img_array)
    emotion = emotion_labels[np.argmax(prediction)]
    
    st.image(uploaded_file, caption="Uploaded Image")
    st.success(f"Predicted Emotion: {emotion}")