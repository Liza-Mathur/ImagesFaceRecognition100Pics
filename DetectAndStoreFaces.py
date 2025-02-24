import cv2
import os
import matplotlib.pyplot as plt

folder = 'StoredFace'
cascades = cv2.CascadeClassifier('DATA/HaarCascade/haarcascade_frontalface_default.xml')

def storeFaces(img, cascade):
    faces = cascade.detectMultiScale(img , 1.2, 5, minSize=(80, 80))
    for x,y,w,h in faces:
        roi = img[max(y-5 , 0):max(y+h+5 , 0) , max(0 , x-5):max(0, x+w+5)]
        plt.imshow(roi)
        plt.show()

img = cv2.imread('DATA/Images/IMG-20240218-WA0008.jpg')
storeFaces(img, cascades)
# Not gonna use this. Other one works better