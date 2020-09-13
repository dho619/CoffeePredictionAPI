from io import BytesIO
from base64 import b64decode
from datetime import datetime
from pathlib import Path
from PIL import Image
from cv2 import resize, cvtColor, COLOR_RGB2BGR
from pickle import load
from numpy import array
from app import db
from ..models.Classifications import Classifications

def diseaseDictionary(num):
    disease = ''
    if num == 0:
        disease = 'Saudável'
    elif num == 1:
        disease = 'Ferrugem'
    else:
        disease = 'Outras'
    return disease


def preProcessing(img):
    imgResized = resize(cvtColor(array(img), COLOR_RGB2BGR), (200, 200))
    imgArray = imgResized.flatten()
    preProcessingImage = array([imgArray])
    return preProcessingImage

def randonForestClassification(preProcessingImage):
    arquivoRNA = open('./app/utils/redeRF.p',  'rb')
    randonForest = load(arquivoRNA)
    arquivoRNA.close()
    predict = randonForest.predict(preProcessingImage)
    return diseaseDictionary(predict[0])

def classificationImage(img_base64, id):
    if img_base64 == '':
        image = ''
    else:
        try:
            image = b64decode(str(img_base64))
            img = Image.open(BytesIO(image)) #transforma em uma imagem do PIL
        except Exception as e:
            print(e)
            image = ''
    preProcessingImage = preProcessing(img)
    predict = randonForestClassification(preProcessingImage)
    healthy = predict == 'Saudável'
    disease = predict
    classification = Classifications.query.get(id)
    classification.healthy = healthy
    classification.disease = disease
    db.session.commit()
