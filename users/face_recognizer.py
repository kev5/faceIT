import cv2


def image_recognition(file):
    img = cv2.imread(file)

    gray = cv2.imread(file, 0)

    x, y, h, w, _ = 0, 0, *img.shape

    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    id_, conf = recognizer.predict(gray[y: y + h, x: x + w])

    if conf > 50:
        id_ = -1

    return id_


def capture_recognition():
    cam = cv2.VideoCapture(0)

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


def main():
    recognizer.read('recognizer/training_set.yml')
    # capture_recognition()
    # image_recognition('this_is_user_1.jpg')


recognizer = cv2.face.LBPHFaceRecognizer_create()
detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

if __name__ == '__main__':
    main()
