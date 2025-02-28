import cv2
import face_recognition
import os
import matplotlib.pyplot as plt

folder = 'StoredFaces'

def storeFaces(img):
    face_locs = face_recognition.face_locations(img, model='hog')
    plt.imshow(img, cmap='gray')
    plt.show()
    embeddings = face_recognition.face_encodings(img, face_locs)
    return embeddings
    # for top, right, bottom, left in face_locs:
    #     # cv2.rectangle(img, (left, top), (right, bottom), (0, 255, 0), 2)
    #     # left - x, to - y , right - x+w , bottom - y+h
    #     face = img[max(top-5 , 0):max(bottom+5 , 0) , max(0 , left-5):max(0, right+5)]
    #     embeddings = face_recognition.face_e
    #     cv2.imwrite(os.path.join(folder, f"{i}.jpg"), face)
    #     i += 1
        
# img = cv2.imread('DATA/Images/20221113_222918.jpg')
# storeFaces(img)