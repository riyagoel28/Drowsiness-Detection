import cv2
import dlib

detector = dlib.get_frontal_face_detector()

predictor = dlib.shape_predictor("../Files/shape_predictor_68_face_landmarks.dat")
cap = cv2.VideoCapture(0)