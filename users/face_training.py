import os
import cv2
import numpy
from PIL import Image as Im
from django.conf import settings
from users.models import Image

def get_data_set(directory):
    images=[]
    ids= []
    for image in Image.objects.all():
        images.append(numpy.array(Im.open(settings.BASE_DIR+settings.MEDIA_URL+ str(image.name)).convert('L')))
        ids.append(int(image.user_id))
    return images, ids

def train(faces, ids):
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.train(faces, numpy.array(ids))
    recognizer.write(settings.BASE_DIR + '/users/recognizer/training_set.yml')

def main():
    train(get_data_set('images'))

if __name__ == '__main__':
    main()
