import os
import cv2
import numpy as np
import tensorflow as tf
from face_verification.model.l1dist import L1Dist


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, 'face_verification', 'model', 'siamesemodel1.h5')

VERIFICATION_PATH = os.path.join('face_verification', 'application_data', 'verification_images')
INPUT_IMAGE_PATH = os.path.join('face_verification', 'application_data', 'input_image', 'input.jpg')

model = tf.keras.models.load_model(MODEL_PATH, custom_objects={'L1Dist': L1Dist}) #type: ignore

def preprocess(file_path):
    byte_img = tf.io.read_file(file_path)
    img = tf.io.decode_jpeg(byte_img)
    img = tf.image.resize(img, (100, 100))
    return img / 255.0 # type: ignore

def verify_face(capture):
    os.makedirs(os.path.dirname(INPUT_IMAGE_PATH), exist_ok=True)

    ret, frame = capture.read()
    if not ret:
        return False

    face = frame[120:120+250, 200:200+250, :]
    cv2.imwrite(INPUT_IMAGE_PATH, face)

    input_img = preprocess(INPUT_IMAGE_PATH)
    results = []

    for image in os.listdir(VERIFICATION_PATH):
        validation_img = preprocess(os.path.join(VERIFICATION_PATH, image))
        input_img_exp = np.expand_dims(input_img, axis=0)
        validation_img_exp = np.expand_dims(validation_img, axis=0)
        result = model.predict((input_img_exp, validation_img_exp))


        results.append(result)

    detection_threshold = 0.7
    verification_threshold = 0.6
    detection = np.sum(np.array(results) > detection_threshold)
    verification = detection / len(results)

    return verification > verification_threshold
