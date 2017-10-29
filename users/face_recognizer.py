import cv2
from django.conf import settings

recognizer = cv2.face.LBPHFaceRecognizer_create()

recognizer.read(settings.BASE_DIR + 'users/recognizer/training_set.yml')



def image_recognition(file):
    img = cv2.imread(settings.BASE_DIR+'/'+file)

    gray = cv2.imread(file, 0)

    x, y,  = 0, 0
    h, w, _ = img.shape[0], img.shape[1], img.shape[2]

    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    id_, conf = recognizer.predict(gray[y: y + h, x: x + w])

    if conf > 50:
        id_ = -1

    return id_


def capture_recognition():
    cam = cv2.VideoCapture(0)
    detector = cv2.CascadeClassifier(settings.BASE_DIR + 'users/haarcascade_frontalface_default.xml')

    while True:
        ret, img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = detector.detectMultiScale(gray, 1.3, 5)

        if len(faces) != 0:
            break

    x, y, w, h = faces[0]

    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    id_, conf = recognizer.predict(gray[y:y+h, x:x+w])

    if conf > 50:
        id_ = 'Unknown'

    cv2.putText(img, str(id_), (x, y + h), cv2.FONT_HERSHEY_SIMPLEX, 255,
                (255, 255, 255), 2, cv2.LINE_AA)

    cv2.imwrite("this_is_user_" + str(id_) + ".jpg", gray[y:y+h, x:x+w])

    cam.release()



