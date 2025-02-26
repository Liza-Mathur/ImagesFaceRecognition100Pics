import os
from openpyxl import load_workbook
import pandas as pd

excel_file = "image_indexes.xlsx"

def save_images_indexes(indexList, images):
    indexes_str = ",".join(map(str, indexList))
    try:
        df = pd.read_excel(excel_file, engine="openpyxl")
    except FileNotFoundError:
        df = pd.DataFrame(columns=["Image", "Indexes"])

    # Append new data
    new_data = pd.DataFrame({"Image": [images], "Indexes": [indexes_str]})
    df = pd.concat([df, new_data], ignore_index=True)

    # Save back to Excel
    df.to_excel(excel_file, index=False, engine="openpyxl")

    print(f"Saved: {images} -> {indexList}")


