import os

def classificationImage(imageBase64):
    if imageBase64 == '':
        image = os.urandom(1)
        healthy = True
        disease = 'Nenhuma imagem passada'
    else:
        try:
            image = imageBase64.decode('base64')
        except:
            image = os.urandom(1)
        healthy = False
        disease = 'Teste'

    return image, healthy, disease
