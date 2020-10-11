from app import app
import uuid
from io import BytesIO
from base64 import b64decode
from datetime import datetime
from pathlib import Path
from PIL import Image

def create_guid():
    return str(uuid.uuid4())


def create_folder_if_not_exist(path):
    new_path = Path(path)
    new_path.mkdir(parents=True, exist_ok=True)

def open_base64_image(img_base64):
    image_b64Decode = b64decode(str(img_base64))
    image = Image.open(BytesIO(image_b64Decode))
    return image

def save_image(img_base64, user_id):
    if img_base64 == '':
        return '', 'No image reported'
    try:
        image = open_base64_image(img_base64)
        nameImage = user_id + '_' + str(datetime.now())[:-7].replace(' ', '_') + '.jpg'
        path = app.config['PATH_TO_SAVE_IMAGES']
        create_folder_if_not_exist(path)
        pathImage = path + '/' + nameImage
        image.save(pathImage)
        return pathImage, None
    except Exception as e:
        print(e)
        return '', 'Error saving image, check the given path'
