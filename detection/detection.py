import cv2
import numpy
import pickle

from constantes import MARKER_SIZE_M, ARUCO_PARAM

# Подгружаем данные для определения дистанции
with open('calibration_params//dist.pkl', 'rb') as f:
    dist_coef = pickle.load(f)

with open('calibration_params//cameraMatrix.pkl', 'rb') as g:
    cam_mat = pickle.load(g)
