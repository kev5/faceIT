import cv2
from django.conf import settings

from users.models import User, Image

def face_detection(file):
    img = cv2.imread(settings.BASE_DIR+'/'+file)
    detector = cv2.CascadeClassifier(settings.BASE_DIR + '/users/haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = detector.detectMultiScale(gray, 1.3, 5)

    x, y, w, h = faces[0]

    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2.imwrite(file, gray[y: y + h, x: x + w])

import os

def update():
    files = [f for f in os.listdir(settings.BASE_DIR+'/media') if os.path.isfile(f)]
    for img in files:
        face_detection(img)

def create_data():
    files = [f for f in os.listdir(settings.BASE_DIR + '/media')]

    # for i in range(1,6):
    #     User.objects.create(id=i,username='test{0}'.format(i),first_name='test{0}'.format(i),last_name='test{0}'.format(i))

    for file in files:
        Image.objects.create(name=file,user_id=file.split('_')[1])
