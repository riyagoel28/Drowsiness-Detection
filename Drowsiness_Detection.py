from scipy.spatial import distance
from imutils import face_utils
import cv2
import dlib
from pygame import mixer
import time

#Initialize Pygame and load music
mixer.init()
mixer.music.load('Files/alarm.wav')

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("Files/shape_predictor_68_face_landmarks.dat")
cap = cv2.VideoCapture(0)

#Extract indexes of facial landmarks for mouth
(Start, End) = face_utils.FACIAL_LANDMARKS_IDXS['mouth']

counter = 0  # Counter to initialize yawn_timer
count_yawn = 0  # Total number of yawns
elapsed = 0
timer_start = 0
yawn_timer = 0

#Extract indexes of facial landmarks for left and right eye
(lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS['left_eye']
(rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS['right_eye']

#This function calculates and return eye aspect ratio
def eye_aspect_ratio(eye):
    A = distance.euclidean(eye[1], eye[5])
    B = distance.euclidean(eye[2], eye[4])
    C = distance.euclidean(eye[0], eye[3])

    ear = (A+B) / (2*C)
    return ear

#Minimum threshold of eye aspect ratio below which alarm is triggerd
EYE_ASPECT_RATIO_THRESHOLD = 0.3
time_start=0
#Minimum consecutive frames for which eye ratio is below threshold for alarm to be triggered
EYE_ASPECT_RATIO_CONSEC_FRAMES = 100

#COunts no. of consecutuve frames below threshold value
COUNTER = 0