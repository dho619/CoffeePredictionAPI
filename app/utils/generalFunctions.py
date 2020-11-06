from app import app
import uuid
from io import BytesIO
from base64 import b64decode, b64encode
from datetime import datetime
from pathlib import Path
from PIL import Image
import requests

def create_guid():
    return str(uuid.uuid4())

def create_folder_if_not_exist(path):
    new_path = Path(path)
    new_path.mkdir(parents=True, exist_ok=True)

def image_to_base64(url):
    image = Image.open(url)
    img_base64 = b64encode(image.tobytes())
    return img_base64

def open_base64_image(img_base64):
    image_b64Decode = b64decode(str(img_base64))
    image = Image.open(BytesIO(image_b64Decode))
    return image

def save_image(img_base64, user_id):
    if img_base64 == '':
        return '', 'No image reported'
    try:
        image = open_base64_image(img_base64)
        nameImage =  str(datetime.now())[:-7].replace(' ', '_') + '.jpg'
        path = app.config['PATH_TO_SAVE_IMAGES']
        create_folder_if_not_exist(path)
        pathUser = path + '/' + user_id
        create_folder_if_not_exist(pathUser)
        pathImage = pathUser + '/' + nameImage
        image.save(pathImage)
        return pathImage, None
    except Exception as e:
        print(e)
        return '', 'Error saving image, check the given path'
