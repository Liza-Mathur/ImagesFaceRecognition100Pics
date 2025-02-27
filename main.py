import streamlit as st
from PIL import Image
import os
import requests
import time
import DeleteFaces as dfs

get_faces_url = "http://127.0.0.1:8000/get_faces"  
get_all_images_for_faces = "http://127.0.0.1:8000/get_person_images"  

image_folder = "DATA/Images"
faces_folder = "StoredFaces"

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
    st.success(f"Processing: {clicked_image} ...")

    response = requests.get(get_faces_url, params={"image_name": clicked_image})
    face_files = [f for f in os.listdir(faces_folder) if f.endswith(('.jpg', '.png', '.jpeg'))]
    if response.status_code == 200:
        st.success(f"Faces detected successfully!")
        time.sleep(2)  # Wait for API to process the image

        # ---- GET CROPPED FACES FROM STORED FOLDER ----
        face_files = [f for f in os.listdir(faces_folder) if f.endswith(('.jpg', '.png', '.jpeg'))]

        if face_files:
            with st.popover("Detected Faces"):  # MODAL POPUP
                st.write(f"### Faces detected from: {clicked_image}")

                cols_faces = st.columns(5)
                for idx, face_file in enumerate(face_files):
                    face_path = os.path.join(faces_folder, face_file)
                    face_img = Image.open(face_path)
                    
                    with cols_faces[idx % 5]:
                        st.image(face_img, caption=face_file, use_column_width=True)
                        if st.button("Select Face", key=face_file):
                            selected_face = face_file
                            st.success(f"Selected Face: {face_file}")
    else:
        st.error("Error detecting faces. Try again.")

    if face_file:
        face_fil_name = int(face_file.split('.')[0])
        # print(face_fil_name)
        response = requests.get(get_all_images_for_faces, params={"personIdx": face_fil_name , "img_name" : clicked_image})
        images_for_faces_list = response.json()
        print("got imgs - ", images_for_faces_list)
        for imgs in images_for_faces_list:
            imgs_path = os.path.join(image_folder, imgs)
            img =  Image.open(imgs_path)
            
            with cols[idx % columns_per_row]:
                st.image(img, caption=imgs, use_column_width=True)


dfs.delete_stored_folder_contents(faces_folder)