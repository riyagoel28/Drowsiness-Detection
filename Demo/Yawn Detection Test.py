from scipy.spatial import distance
from imutils import face_utils
import cv2
import dlib
from pygame import mixer
import time

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("../Files/shape_predictor_68_face_landmarks.dat")
cap = cv2.VideoCapture(0)
counter = 0  # Counter to initialize yawn_timer
count_yawn = 0  # Total number of yawns
elapsed = 0
timer_start = 0
yawn_timer = 0

#Extract indexes of facial landmarks for mouth
(Start, End) = face_utils.FACIAL_LANDMARKS_IDXS['mouth']