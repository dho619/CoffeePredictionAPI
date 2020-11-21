import requests, sys, cv2
from datetime import datetime
from pathlib import Path
from PIL import Image
from pickle import load
import numpy as np

import mysql.connector

from config_job import host, user, password, database
from sendNotification import send_push_message

config = {
  'host': host,
  'user': user,
  'password': password,
  'database': database
}
try:
    conn = mysql.connector.connect(**config)
except Exception as e:
    print('Erro durante a conexão com o banco de dados')
    print('Erro:')
    print(e)
    sys.exit()

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
    classifications = []
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT id, image_path, tokenPush FROM classifications WHERE is_processed = false;")
        rows = cursor.fetchall()
    except Exception as e:
        print('Erro durante a busca de classificações pedentes!')
        print(e)

    for row in rows:
        classifications.append({"id": row[0], "path_image": row[1], "tokenPush": row[2]})
    cursor.close()
    return classifications

def load_images(classifications):
    images = []
    for i, classification in enumerate(classifications):
        try:
            image = cv2.imread(classification["path_image"])
            images.append(image)
        except Exception as e:
            print('Erro ao carregar imagem {}, localizada em: {}'.format(classification["id"], classification["path_image"]))
            print('Erro:')
            print(e)
    return images

def pre_processing_images(images):
    array_images = []
    for image in images:
        imgResized = cv2.resize(cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR), (200, 200))
        imgArray = imgResized.flatten()
        array_images.append(imgArray)
    pre_processed_images = np.array(array_images)
    return pre_processed_images

def randon_forest_classification(pre_processed_images):
    try:
        arquivoRNA = open('/home/dho/Documentos/CoffeePredictionAPI/app/services/ClassificationJob/redeRF.p', 'rb')
        randonForest = load(arquivoRNA)
        arquivoRNA.close()
        predictions = randonForest.predict(pre_processed_images)
        return predictions
    except Exception as e:
        print('Erro durante a classificação!')
        print('Erro:')
        print(e)
    p

def labeling_classifications(predictions):
    classification_results = []
    for predict in predictions:
        classification_results.append(diseaseDictionary(predict))
    return classification_results

def update_classification_register(classification_results, classifications):
    cursor = conn.cursor()
    for i, classification in enumerate(classification_results):
        healthy = classification == 'Saudável'

        sql = "UPDATE classifications SET healthy = %s, disease = %s,"
        sql += "is_processed = true, updated_at = %s WHERE id = %s;"
        try:
            cursor.execute(sql, (healthy, classification, datetime.now(), classifications[i]["id"]))
            conn.commit()
            result = 'Saudável' if healthy else 'Doente'
            if not healthy:
                result+= ', com a doença ' + classification
            print('Classificação com id: {}, encontrasse {}!'.format(classifications[i]["id"], result))
        except Exception as e:
            print('Erro ao atualizar registro: ' + classifications[i]["id"])
            print('Erro:' + e)
    cursor.close()

def sendNotifications(classifications):
    devices = {}
    for classification in classifications:
        try:
            devices[classification["tokenPush"]] = devices[classification["tokenPush"]] + 1
        except:
            devices[classification["tokenPush"]] = 1

    for key in devices.keys():
        message = 'As {} folhas enviadas por você, já foram analisadas. Clique aqui para visualizar os resultados!'.format(devices[key])
        tokenPush = key
        send_push_message(message, tokenPush)

def classification():
    classifications = search_pending_classification()
    if len(classifications) > 0:
        images = load_images(classifications)
        pre_processed_images = pre_processing_images(images)
        predictions = randon_forest_classification(pre_processed_images)
        classification_results = labeling_classifications(predictions)
        update_classification_register(classification_results, classifications)
        sendNotifications(classifications)
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
