import requests
from datetime import datetime
from pathlib import Path
from PIL import Image
from cv2 import resize, cvtColor, COLOR_RGB2BGR
from pickle import load
from numpy import array

import mysql.connector

config = {
  'host':'127.0.0.1',
  'user':'geovane',
  'password':'1.618_3,14',
  'database':'TCC_development'
}

conn = mysql.connector.connect(**config)

def search_pending_classification():
    cursor = conn.cursor()
    cursor.execute("SELECT id, image_path FROM classifications WHERE is_processed = false;")
    rows = cursor.fetchall()

    ids = []
    path_Images = []
    for row in rows:
        ids.append(row[0])
        path_Images.append(row[1])
    cursor.close()
    return ids, path_Images

def diseaseDictionary(num):
    disease = ''
    if num == 0:
        disease = 'Saudável'
    elif num == 1:
        disease = 'Ferrugem'
    else:
        disease = 'Outras'
        return disease

def pre_processing(img):
    imgResized = resize(cvtColor(array(img), COLOR_RGB2BGR), (200, 200))
    imgArray = imgResized.flatten()
    preProcessingImage = array([imgArray])
    return preProcessingImage


def randon_forest_classification(image):
    arquivoRNA = open('/home/dho/Documentos/CoffeePredictionAPI/app/services/ClassificationJob/redeRF.p', 'rb')
    randonForest = load(arquivoRNA)
    arquivoRNA.close()

    preProcessingImage = pre_processing(image)
    predict = randonForest.predict(preProcessingImage)
    return diseaseDictionary(predict[0])

def update_classification_register(id, healthy, disease):
    cursor = conn.cursor()
    sql = "UPDATE classifications SET healthy = %s, disease = %s,"
    sql += "is_processed = true, updated_at = %s WHERE id = %s;"

    cursor.execute(sql, (healthy, disease, datetime.now(), id))
    conn.commit()
    cursor.close()

def classification():
    ids_classifications, path_images = search_pending_classification()

    for i, path_image in enumerate(path_images):
        image = Image.open(path_image)
        predict = randon_forest_classification(image)
        healthy = predict == 'Saudável'
        disease = predict
        update_classification_register(ids_classifications[i], healthy, disease)
        print(healthy)
        print(predict)

classification()
conn.close()
