import requests, sys, cv2
from datetime import datetime
from pathlib import Path
from PIL import Image
from pickle import load
import numpy as np

import mysql.connector

config = {
  'host':'127.0.0.1',
  'user':'geovane',
  'password':'1.618_3,14',
  'database':'TCC_development'
}
try:
    conn = mysql.connector.connect(**config)
except Exception as e:
    print('Erro durante a conexão com o banco de dados')
    print('Erro:')
    print(e)
    sys.exit()

ids_classifications = []
path_images = []
images = []
pre_processed_images = np.array([])
predictions = []
classification_results = []

def diseaseDictionary(num):
    disease = ''
    if num == 0:
        disease = 'Saudável'
    elif num == 1:
        disease = 'Ferrugem'
    else:
        disease = 'Outras'
        return disease

def search_pending_classification():
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT id, image_path FROM classifications WHERE is_processed = false;")
        rows = cursor.fetchall()
    except:
        print('Erro durante a busca de classificações pedentes!')

    for row in rows:
        ids_classifications.append(row[0])
        path_images.append(row[1])
    cursor.close()

def load_images():
    for i, path_image in enumerate(path_images):
        try:
            image = frame = cv2.imread(path_image)
            images.append(image)
        except Exception as e:
            print('Erro ao carregar imagem {}, localizada em: {}'.format(ids_classifications[i], path_image))
            print('Erro:')
            print(e)

def pre_processing_images():
    global pre_processed_images
    array_images = []
    for image in images:
        imgResized = cv2.resize(cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR), (200, 200))
        imgArray = imgResized.flatten()
        array_images.append(imgArray)
    pre_processed_images = np.array(array_images)

def randon_forest_classification():
    global predictions
    try:
        arquivoRNA = open('/home/dho/Documentos/CoffeePredictionAPI/app/services/ClassificationJob/redeRF.p', 'rb')
        randonForest = load(arquivoRNA)
        arquivoRNA.close()
        predictions = randonForest.predict(pre_processed_images)
    except Exception as e:
        print('Erro durante a classificação!')
        print('Erro:')
        print(e)

def labeling_classifications():
    for predict in predictions:
        classification_results.append(diseaseDictionary(predict))

def update_classification_register():
    cursor = conn.cursor()
    for i, classification in enumerate(classification_results):
        healthy = classification == 'Saudável'

        sql = "UPDATE classifications SET healthy = %s, disease = %s,"
        sql += "is_processed = true, updated_at = %s WHERE id = %s;"
        try:
            cursor.execute(sql, (healthy, classification, datetime.now(), ids_classifications[i]))
            conn.commit()
            result = 'Saudável' if healthy else 'Doente'
            if not healthy:
                result+= ', com a doença ' + classification
            print('Classificação com id: {}, encontrasse {}!'.format(ids_classifications[i], result))
        except Exception as e:
            print('Erro ao atualizar registro: ' + ids_classifications[i])
            print('Erro:')
            print(e)
    cursor.close()

def classification():
    search_pending_classification()
    if len(path_images) > 0:
        load_images()
        pre_processing_images()
        randon_forest_classification()
        labeling_classifications()
        update_classification_register()
        print()
        print(datetime.now())
        print(50*'*')
        print()
    else:
        print(50*'*')
        print('Nenhuma classificação pendente as {}'.format(datetime.now()))
        print(50*'*')


classification()
conn.close()
