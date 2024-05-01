import cv2
import numpy as np
import pickle

from constantes import MARKER_SIZE_M, ARUCO_PARAM

# Подгружаем данные для определения дистанции
with open('camera_params//dist.pkl', 'rb') as f:
    dist_coef = pickle.load(f)

with open('camera_params//cameraMatrix.pkl', 'rb') as g:
    cam_mat = pickle.load(g)


def pose_esitmation(frame, arucoDict):
    """Находит маркеры на кадре и возвращает координаты двух углов 1 и 3, дистанция до маркера"""

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Ищем маркеры
    corners, _, _ = cv2.aruco.detectMarkers(gray, arucoDict, parameters=ARUCO_PARAM)

    if corners:

        # Определяем сдвиг
        rvec, tvec, _ = cv2.aruco.estimatePoseSingleMarkers(
            corners, MARKER_SIZE_M, cam_mat, dist_coef
        )

         # Определяем дистанцию до маркера
        distance_to_marker = np.linalg.norm(tvec)


        # координаты маркера по X
        c1X = corners[0][0][0][0]
        c3X = corners[0][0][2][0]

        # координаты маркера по Y
        c1Y = corners[0][0][0][1]
        c3Y = corners[0][0][2][1]

        # дистанция до маркера
        d = distance_to_marker

        return {c1X, c1Y, c3X, c3Y, d}


def correction(c1X, c1Y, c3X, c3Y):
    """Отправляет симгналы в двигатели, для поворота"""
    pass


def decline(d):
    """Снижает высоту до маркера"""
    pass
