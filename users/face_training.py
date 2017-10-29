import os
import cv2
import numpy
from PIL import Image


def get_data_set(directory):
    images = [numpy.array(Image.open(image_path).convert('L'))  for image_path
              in [os.path.join(directory, image) for image
                  in os.listdir(directory)]]

    ids = [int(image.split('_')[1]) for image in os.listdir(directory)]

    return images, ids


def placeholder(dictionary):
    images, ids = [], []

    for k, v in dictionary.items():
        ids.extend([int(k)] * len(v))
        images.extend(v)

    return images, ids


def train(faces, ids):
    recognizer.train(faces, numpy.array(ids))
    recognizer.write('recognizer/training_set.yml')


def main():
    train(*get_data_set('images'))


recognizer = cv2.face.LBPHFaceRecognizer_create()

if __name__ == '__main__':
    main()
