import cv2
import face_recognition
import os
import matplotlib.pyplot as plt



def storeFaces(img):
    face_locs = face_recognition.face_locations(img, model='hog')
    plt.imshow(img, cmap='gray')
    plt.show()
    for top, right, bottom, left in face_locs:
        # cv2.rectangle(img, (left, top), (right, bottom), (0, 255, 0), 2)
        # left - x, to - y , right - x+w , bottom - y+h
        roi = img[max(top-5 , 0):max(bottom+5 , 0) , max(0 , left-5):max(0, right+5)]
        plt.imshow(roi)
        plt.show()
