from fastapi import FastAPI
from typing import List
import cv2
import numpy as np
import face_recognition
import os
import GetFacesForApp as gffa
import GetAllImagesWithPersonIndex as gaiwpi
app = FastAPI()

@app.get('/get_faces')
def get_faces(image_name : str):
    img = os.path.join('DATA/Images', image_name)
    img = cv2.imread(img)
    gffa.storeFaces(img)
    
    # IDK if its working or not. So do 1 thing, make a api call from jupyter notebook - check in chatgpt there u already have how to do this, and then check if its storing faces in StoredFaces folder or not
    return None

@app.get('/get_person_images')
def get_person_images(personIdx, img_name):
    folder = 'Data/Images'
    images_list = gaiwpi.getImagesWithPersonIndex(personIdx, img_name)
    if images_list != None:
        print("In If app")
        print("app - ", images_list)
        return images_list 
    # This images_list will be a list of images names with .jpg at the end - it'll be a string
    else:
        print("In else app")
        return None