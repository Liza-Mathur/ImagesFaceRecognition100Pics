import streamlit as st
from PIL import Image
import os

image_folder = "DATA/Images"
faces_folder = "L:/FaceSearchWebApp/StoredFaces"

image_files = [f for f in os.listdir(image_folder) if f.endswith(('.jpg', '.png', '.jpeg'))]

image_paths = [os.path.join(image_folder, img) for img in image_files]

st.write("Click on an image to select it:")

columns_per_row = 5  
cols = st.columns(columns_per_row)

clicked_image = None

for idx, image_file in enumerate(image_files):
    img_path = os.path.join(image_folder, image_file)
    image = Image.open(img_path)
    
    with cols[idx % columns_per_row]:
        st.image(image, caption=image_file, use_column_width=True)
        if st.button(f"Open Image", key=image_file):
            clicked_image = image_file
            

if clicked_image:
    st.success(f"You selected: {clicked_image}")
