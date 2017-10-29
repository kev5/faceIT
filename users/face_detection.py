import cv2


def face_detection(file):
    img = cv2.imread(file)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = detector.detectMultiScale(gray, 1.3, 5)

    x, y, w, h = faces[0]

    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2.imwrite(file, gray[y: y + h, x: x + w])


detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
