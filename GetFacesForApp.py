import os
import face_recognition 
import cv2

def storeFaces(img):
    face_locs = face_recognition.face_locations(img, model='hog')
    i=1
    folder = 'StoredFaces'
    for top, right, bottom, left in face_locs:
        # cv2.rectangle(img, (left, top), (right, bottom), (0, 255, 0), 2)
        # left - x, to - y , right - x+w , bottom - y+h
        face = img[max(top-5 , 0):max(bottom+5 , 0) , max(0 , left-5):max(0, right+5)]
        cv2.imwrite(os.path.join(folder, f"{i}.jpg"), face)
        i += 1
        
# print(storeFaces(img))
# storeFaces(img)