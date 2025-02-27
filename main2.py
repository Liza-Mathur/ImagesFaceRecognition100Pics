import streamlit as st
from PIL import Image
import os
import requests
import time
import DeleteFaces as dfs

# API URLs
get_faces_url = "http://127.0.0.1:8000/get_faces"  
get_all_images_for_faces = "http://127.0.0.1:8000/get_person_images"  

# Folders
image_folder = "DATA/Images"
faces_folder = "StoredFaces"

# Initialize session state
if "clicked_image" not in st.session_state:
    st.session_state.clicked_image = None
if "selected_face" not in st.session_state:
    st.session_state.selected_face = None
if "images_for_faces_list" not in st.session_state:
    st.session_state.images_for_faces_list = []

# List images
image_files = [f for f in os.listdir(image_folder) if f.endswith(('.jpg', '.png', '.jpeg'))]

st.write("Click on an image to select it:")

columns_per_row = 5  
cols = st.columns(columns_per_row)

# Display main images
for idx, image_file in enumerate(image_files):
    img_path = os.path.join(image_folder, image_file)
    image = Image.open(img_path)
    
    with cols[idx % columns_per_row]:
        st.image(image, caption=image_file, use_column_width=True)
        if st.button(f"Open Image", key=image_file):
            st.session_state.clicked_image = image_file  # Store in session_state
            st.session_state.selected_face = None  # Reset face selection
            st.session_state.images_for_faces_list = []  # Reset previous images

# If an image is selected, process it
if st.session_state.clicked_image:
    clicked_image = st.session_state.clicked_image
    st.success(f"Processing: {clicked_image} ...")

    # Call API to get detected faces
    response = requests.get(get_faces_url, params={"image_name": clicked_image})
    face_files = [f for f in os.listdir(faces_folder) if f.endswith(('.jpg', '.png', '.jpeg'))]

    if response.status_code == 200:
        st.success("Faces detected successfully!")
        time.sleep(2)  

        if face_files:
            with st.popover("Detected Faces"):  # MODAL POPUP
                st.write(f"### Faces detected from: {clicked_image}")

                cols_faces = st.columns(5)
                for idx, face_file in enumerate(face_files):
                    face_path = os.path.join(faces_folder, face_file)
                    face_img = Image.open(face_path)
                    
                    with cols_faces[idx % 5]:
                        st.image(face_img, caption=face_file, use_column_width=True)
                        if st.button("Select Face", key=f"face_{face_file}"):
                            st.session_state.selected_face = face_file  # Store selected face
                            st.rerun()  # Refresh UI to show next step

# If a face is selected, fetch related images
if st.session_state.selected_face:
    face_file = st.session_state.selected_face
    face_fil_name = int(face_file.split('.')[0]) - 1 # Extract face ID

    # Call API to get similar images
    response = requests.get(get_all_images_for_faces, params={"personIdx": face_fil_name , "img_name" : clicked_image})
    st.session_state.images_for_faces_list = response.json()  # Store in session_state

    st.success(f"Showing images related to face {face_fil_name}")

    cols_related = st.columns(columns_per_row)
    for idx, img_name in enumerate(st.session_state.images_for_faces_list):
        img_path = os.path.join(image_folder, img_name)
        img = Image.open(img_path)
        
        with cols_related[idx % columns_per_row]:
            st.image(img, caption=img_name, use_column_width=True)

# Clean up detected faces
dfs.delete_stored_folder_contents(faces_folder)
