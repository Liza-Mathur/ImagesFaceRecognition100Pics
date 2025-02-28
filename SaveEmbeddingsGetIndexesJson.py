import os
import json
import numpy as np
import face_recognition

json_file = "face_embeddings.json"

def save_embeddings(embeddingsList , data=[]):
    embeddingsList = embeddingsList.tolist() if isinstance(embeddingsList, np.ndarray) else embeddingsList
    
    stored_embeddings = []
    stored_indexes = []
    img_indexes = []
    new_index = 0
    if not data:
        1+1
    else:
        for k in data:
            stored_embeddings.append(k['embeddings'])
            stored_indexes.append(k['pid'])
    
    # # Check if the JSON file exists
    # if os.path.exists(json_file):
    #     with open(json_file, "r") as file:
    #         try:
    #             data = json.load(file)
    #             for k in data:
    #                 stored_embeddings.append(k['embeddings'])
    #                 stored_indexes.append(k['pid'])
    #         except json.JSONDecodeError:
    #             data = []  # If the file is corrupt or empty, start fresh
    # else:
    #     data = []  # If file doesn't exist, create an empty list

    


    for new_emb in embeddingsList:
        print(f'New Emb - ')
        matches = face_recognition.compare_faces(stored_embeddings, new_emb)
        distances = face_recognition.face_distance(stored_embeddings, new_emb)

        if any(matches):  
            print("In matchess??????")
            best_match_index = np.argmin(distances)
            best_distance = distances[best_match_index]

            if best_distance <= 0.52:  # Means it's the same person
                print("In bedt distance   " , best_distance)
                print("Best match with - ", stored_indexes[best_match_index])
                existing_index = stored_indexes[best_match_index]
                print("BEST MATCH INDEX - ", best_match_index)
                print('EXISTING INDEX - ', existing_index)
                avg_embedding = np.mean([stored_embeddings[best_match_index], new_emb], axis=0).tolist()
                stored_embeddings[best_match_index] = avg_embedding
                img_indexes.append(existing_index)
            else:
                print("In two - where matched but best distance was less")
                print(best_distance)
                if not stored_indexes:
                    new_index = 1
                    stored_indexes.append(1)
                    stored_embeddings.append(new_emb)
                else: 
                    new_index = stored_indexes[-1]+1
                    stored_indexes.append(new_index)
                    stored_embeddings.append(new_emb)
                new_dict = {'pid':new_index , "embeddings":new_emb}
                data.append(new_dict)
                img_indexes.append(new_index)
        else:
            print("Not matched at all.....")
            if not stored_indexes:
                new_index = 1
                stored_indexes.append(1)
                stored_embeddings.append(new_emb)
            else: 
                new_index = stored_indexes[-1]+1
                stored_indexes.append(new_index)
                stored_embeddings.append(new_emb)
            new_dict = {'pid':new_index , "embeddings":new_emb}
            data.append(new_dict)
            img_indexes.append(new_index)
        print("Idx for new_emb = ", new_index)

    print(f"Saved embeddings for PID: {new_index}")
    
    # with open(json_file, "w") as file:
    #     json.dump(data, file)
    
    return (img_indexes , data)


# i, data = save_embeddings([np.array([-5.26507832e-02,  2.07226351e-03,  5.58310598e-02, -6.15257882e-02,
#        -7.93995261e-02,  4.34362292e-02, -8.20464864e-02, -6.47739768e-02,
#         1.91152051e-01, -1.34873390e-01,  1.52577117e-01, -7.54600298e-03,
#        -1.39607504e-01, -4.35129330e-02,  4.37743962e-03,  1.53815299e-01,
#        -1.57381862e-01, -1.70760617e-01,  4.33248281e-03, -1.86865628e-02,
#        -5.39391860e-02,  1.10390177e-02,  3.46380323e-02,  5.24139628e-02,
#        -1.47634268e-01, -3.79360616e-01, -7.96283707e-02, -9.50655267e-02,
#         3.63751054e-02, -3.00094336e-02, -2.32962444e-02,  8.25409219e-02,
#        -2.10806176e-01, -3.65199745e-02,  5.74979372e-02,  1.37125328e-01,
#        -2.35581882e-02, -9.58661139e-02,  2.10559830e-01,  2.31076721e-02,
#        -2.49496952e-01, -9.83852595e-02,  8.92764628e-02,  2.26065755e-01,
#         2.03479797e-01,  5.55119179e-02, -6.38655201e-03, -9.05567966e-03,
#         1.23708732e-01, -2.65749574e-01,  7.18927756e-02,  1.00102283e-01,
#         5.10668568e-03,  6.95272759e-02,  7.43410289e-02, -1.93592817e-01,
#         3.77515294e-02,  1.19089618e-01, -1.47620648e-01, -2.12571118e-04,
#        -7.95428678e-02, -2.88353860e-02,  4.53297943e-02,  4.10453137e-03,
#         3.16890121e-01,  1.00748129e-01, -7.30430186e-02, -1.01487935e-01,
#         2.75719553e-01, -1.07945427e-01,  1.44369341e-03,  8.64085704e-02,
#        -1.09331720e-01, -1.68297172e-01, -2.45031148e-01, -9.38418321e-03,
#         4.33753639e-01,  1.17000699e-01, -1.25193432e-01,  9.60652530e-02,
#        -5.52664734e-02, -7.10409433e-02,  4.22536135e-02,  1.64648011e-01,
#         1.20010786e-02,  4.54267375e-02, -1.56421810e-02, -1.94061045e-02,
#         2.33863816e-01,  2.86984220e-02, -1.88885462e-02,  2.14963347e-01,
#        -4.05550972e-02,  1.41938897e-02,  8.25252980e-02,  5.81550933e-02,
#        -7.04710856e-02,  8.93416442e-03, -1.88692272e-01, -1.04716241e-01,
#         7.61733502e-02, -1.05523318e-02,  2.99376138e-02,  1.98740900e-01,
#        -2.56070822e-01,  1.24954827e-01,  1.02904784e-02, -2.73931548e-02,
#         8.17527026e-02,  6.91297203e-02, -1.51534509e-02, -8.83683786e-02,
#         1.45618692e-01, -2.95251608e-01,  1.44571826e-01,  1.47519916e-01,
#        -7.97980838e-03,  1.96159184e-01,  3.68971154e-02,  8.93792212e-02,
#         3.92279215e-02, -7.12743774e-02, -1.88599080e-01, -5.87643497e-02,
#         3.92602291e-03, -2.49871425e-02,  1.88912880e-02,  8.77289474e-02]), np.array([-0.09404924,  0.1036533 ,  0.02024009, -0.09983964, -0.12264562,
#         0.04509725, -0.07857999, -0.06483378,  0.28673756, -0.19140211,
#         0.16169231, -0.00721704, -0.16069464, -0.00449329, -0.03821934,
#         0.17368828, -0.16997068, -0.17918618, -0.02768603, -0.1178067 ,
#        -0.03977917,  0.03205474, -0.04024791,  0.06949553, -0.18108332,
#        -0.309762  , -0.07124277, -0.08923129, -0.02864305, -0.07084702,
#        -0.01414287,  0.09155475, -0.18717954, -0.00908317,  0.0778254 ,
#         0.10613182, -0.03183487, -0.01563819,  0.19729853,  0.0610861 ,
#        -0.15282327, -0.11956781,  0.10848371,  0.20771177,  0.18967237,
#         0.08449033, -0.02299433, -0.0512161 ,  0.15772919, -0.20261694,
#        -0.01212563,  0.17377377,  0.05716773,  0.07784075,  0.10042351,
#        -0.19976969,  0.04677418,  0.06900771, -0.17424127, -0.02602062,
#         0.01394531, -0.09201328, -0.11053963, -0.01598832,  0.29959866,
#         0.11307744, -0.10867694, -0.13910271,  0.28018901, -0.13102612,
#        -0.03053895,  0.08653758, -0.08939876, -0.17521688, -0.20521732,
#        -0.01226168,  0.42161837,  0.16546829, -0.11323415,  0.05562158,
#        -0.00457291, -0.05680118,  0.00806009,  0.10223051, -0.10723714,
#         0.00512159, -0.00690771,  0.012629  ,  0.17640504,  0.0712047 ,
#        -0.00695465,  0.13208498, -0.03665617,  0.02452855,  0.03078735,
#         0.01782526, -0.12245109, -0.01969494, -0.14147368, -0.06663398,
#         0.02376666, -0.04011709, -0.01363474,  0.12760958, -0.20455073,
#         0.15656398, -0.03894465, -0.07941917, -0.10532542,  0.05738143,
#        -0.07355715,  0.01374264,  0.15689985, -0.27648479,  0.15216713,
#         0.11212401, -0.04048917,  0.2027152 ,  0.0549081 ,  0.09972151,
#        -0.00143356, -0.05519712, -0.15917645, -0.16047153, -0.00672749,
#        -0.10182777,  0.10087815,  0.00780184]), np.array([-0.13195491,  0.03173506,  0.03874169, -0.03293114, -0.08245333,
#        -0.01054408, -0.0342492 , -0.06999873,  0.18329151, -0.05356979,
#         0.1905919 , -0.01769633, -0.18701024, -0.15245679,  0.09397159,
#         0.13466059, -0.11659221, -0.17659882, -0.01137672, -0.1190206 ,
#        -0.03494377,  0.00060934,  0.02538687,  0.10988488, -0.24940319,
#        -0.3652325 , -0.03633214, -0.1455003 , -0.01593592, -0.07961237,
#        -0.02487541,  0.14179264, -0.19758327, -0.01524233,  0.0267408 ,
#         0.20343541,  0.03323508,  0.02492122,  0.17669551,  0.04423777,
#        -0.19971679,  0.01984833, -0.00802063,  0.26064354,  0.13734797,
#         0.03625886,  0.02202128,  0.04405634,  0.12756911, -0.23157841,
#         0.12716296,  0.16314262,  0.09007581, -0.05060564,  0.12085724,
#        -0.10691817, -0.04190931,  0.02659436, -0.24158847,  0.035976  ,
#         0.05996711, -0.01822469, -0.08750758, -0.11407738,  0.19733532,
#         0.17934901, -0.11704564, -0.10917306,  0.09795067, -0.14973146,
#        -0.05941709,  0.10712039, -0.12936006, -0.1666624 , -0.31831369,
#         0.09913252,  0.35196403,  0.12956282, -0.2081219 ,  0.02741951,
#         0.00877578, -0.01373094,  0.06550157,  0.04254632, -0.04409127,
#         0.06376737, -0.06975521,  0.05192461,  0.14083292,  0.06135168,
#        -0.06974365,  0.17344199, -0.04225943,  0.05964944,  0.01460445,
#         0.04394756, -0.05492421, -0.04115948, -0.11034903, -0.02002359,
#         0.10127749, -0.00626878,  0.0015103 ,  0.04951363, -0.1691269 ,
#         0.14241271, -0.02787059, -0.02920855, -0.04515012,  0.09349822,
#        -0.16978033, -0.00540711,  0.14022456, -0.29956329,  0.20570037,
#         0.12311371, -0.05703503,  0.1064813 ,  0.05702516,  0.01970604,
#        -0.03186678, -0.01589277, -0.10382995, -0.13107061,  0.07997935,
#        -0.07757676,  0.11509223,  0.03554676])])
                                                          
# print(i)
# print(type(data))
# print(type(data[0]))
# print(data[0])