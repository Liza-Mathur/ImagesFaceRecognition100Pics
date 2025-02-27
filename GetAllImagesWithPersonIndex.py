import os
from openpyxl import load_workbook
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import cv2



def getImagesWithPersonIndex(personIdx , imageName):
    # indexes_str = ",".join(map(str, indexList))
    # try:
    #     df = pd.read_excel(excel_file, engine="openpyxl")
    # except FileNotFoundError:
    #     df = pd.DataFrame(columns=["Image", "Indexes"])

    # # Append new data
    # new_data = pd.DataFrame({"Image": [images], "Indexes": [indexes_str]})
    # df = pd.concat([df, new_data], ignore_index=True)

    # # Save back to Excel
    # df.to_excel(excel_file, index=False, engine="openpyxl")

    # print(f"Saved: {images} -> {indexList}")

    excel_file = "image_indexes.xlsx"
    try:
        df = pd.read_excel(excel_file , engine="openpyxl")
        print("In try")
    except FileNotFoundError:
        print('In Except')
        return None
    
    images = df['Image'].tolist()
    indexes = df['Indexes'].apply(getList)
    # if images:
        # print(images)
    # print('images - ', images)
    # print('indexes - ', indexes)
    imagesWithPersonIdx = []
    personIdx = int(personIdx)
    # print('Person idx type - ', type(personIdx))
    for i, image in enumerate(images):
        if image == imageName:
            print("img == image_name, so continue")
            continue
        # print(indexes[i])
        # print(type(indexes[i]))
        for k in indexes[i]:
            # print(f"in {k} - k getting index - {indexes[i]}")
            if k == personIdx:
                print(f"Adding image - {image} becuase it has indexes - {k}")
                imagesWithPersonIdx.append(image)
    return imagesWithPersonIdx
     
def getList(string):
    lists = []
    s = string.split(',')
    for k in s:
        lists.append(int(k))
    return lists

# folder = 'Data/Images'
# img_name = '20201026_131428.jpg'
# personIdx = 2
# x = getImagesWithPersonIndex(personIdx, img_name)
# if x != None:
#     for k in x:
#         print("In K")
#         filepath = os.path.join(folder, k)
#         img = cv2.cvtColor(cv2.imread(filepath) , cv2.COLOR_BGR2GRAY)
#         plt.imshow(img, cmap='gray')
#         plt.show()