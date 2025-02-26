import cv2
import os
import matplotlib.pyplot as plt
import StoreAndDetectFaces_FaceRecog as sadf
import SaveEmbeddingsGetIndexesJson as getIndex
import SaveImageWithIndexes as saveImage
import DeleteFaces as df

folder = 'DATA/Images'
file = os.listdir(folder)
embeddings_data_list = []
for i, images in enumerate(file):
    print(i)
    filename = os.path.join(folder , images)
    image = cv2.imread(filename)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    # Now I will get embeddings for each face in the image
    embeddings = sadf.storeFaces(image_rgb)
    # print(embeddings) 
    print(type((embeddings[0])))
    print('got embeddings')
    indexList, embeddings_data_list = getIndex.save_embeddings(embeddings, embeddings_data_list)
    print('saved embeddings')
    saveImage.save_images_indexes(indexList, images)
    print('saved images with indexes')
    df.delete_stored_folder_contents('DATA/StoredFaces')
    if i==20:
        # print(embeddings_data_list)
        break
    
# Need to implement logic - if no embeddings found - from line 18 - then skip rest loop and continue