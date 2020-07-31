from io import BytesIO
from os import urandom
from base64 import b64decode
from datetime import datetime
from PIL import Image

def classificationImage(img_base64):
    if img_base64 == '':
        image = ''
    else:
        try:
            image = b64decode(str(img_base64)) # decodifica a base64
            fileName = str(datetime.now()) + '.jpg'#nome do arquivo
            pathImg = './app/temp/' + fileName #caminho para salvar temporariamente
            img = Image.open(BytesIO(image)) #transforma em um imagem do PIL
            img.save(pathImg, 'jpeg') #salva a imagem
        except Exception as e:
            print(e)
            image = ''
    healthy = False
    disease = 'Teste'
    return urandom(1), healthy, disease
