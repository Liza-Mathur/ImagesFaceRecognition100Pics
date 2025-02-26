import os
import numpy as np
import pandas as pd
import face_recognition

EXCEL_FILE = "face_embeddings.xlsx"

def saveEmbeddings(embeddingsList):
    if os.path.exists(EXCEL_FILE):
        try:
            df = pd.read_excel(EXCEL_FILE)
        except Exception as e:
            print("Error reading Excel file:", e)
            df = pd.DataFrame(columns=["Index", "Embedding"])
    else:
        df = pd.DataFrame(columns=["Index", "Embedding"])

    new_indexes = []
    embeddingsList = embeddingsList.tolist() if isinstance(embeddingsList, np.ndarray) else embeddingsList
    if df.empty:
    # First time saving, assign indexes from 1
        emb = embeddingsList[0]
        emb = emb.tolist() if isinstance(emb, np.ndarray) else emb
        print("EMB")
        print(emb)
        df = pd.DataFrame({"Index": 1, "Embedding": emb})
        print(df)
        new_indexes.append(1)
    else:
        # Load stored embeddings and indexes
        stored_embeddings = df["Embedding"].tolist() # Convert string to list
        stored_indexes = df["Index"].tolist()
        
        for new_emb in embeddingsList:
            print('New Emb - {new_emb}')
            matches = face_recognition.compare_faces(stored_embeddings, new_emb)
            distances = face_recognition.face_distance(stored_embeddings, new_emb)

            if any(matches):  
                best_match_index = np.argmin(distances)
                best_distance = distances[best_match_index]

                if best_distance <= 0.1:  # Means it's the same person
                    print(best_distance)
                    existing_index = stored_indexes[best_match_index]
                    avg_embedding = np.mean([stored_embeddings[best_match_index], new_emb], axis=0).tolist()

                    df.loc[df["Index"] == existing_index, "Embedding"] = list(avg_embedding)
                    new_indexes.append(existing_index)
                else:
                    print("In two - ")
                    print(best_distance)
                    new_index = max(stored_indexes) + 1
                    df.loc[len(df)] = [new_index, new_emb]
                    new_indexes.append(new_index)
            else:
                new_index = max(stored_indexes) + 1
                df.loc[len(df)] = [new_index, new_emb]
                new_indexes.append(new_index)

    df.to_excel(EXCEL_FILE, index=False)
    return new_indexes

# def saveEmbeddings(embeddingList):
    