import cv2
import pickle


from constantes import MARKER_SIZE_M, ARUCO_PARAM


# Подгружаем данные для определения дистанции
with open('camera_params//dist.pkl', 'rb') as f:
    dist_coef = pickle.load(f)

with open('camera_params//cameraMatrix.pkl', 'rb') as g:
    cam_mat = pickle.load(g)


def pose_esitmation(frame, arucoDict):
    """Находит маркеры на кадре и возвращает координаты маркера относительно камеры,
    дистанцию до маркера, отклонение по X и по Y"""

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Ищем маркеры
    corners, _, _ = cv2.aruco.detectMarkers(gray, arucoDict, parameters=ARUCO_PARAM)

    if corners:

        # Определяем сдвиг
        rvec, tvec, _ = cv2.aruco.estimatePoseSingleMarkers(
            corners, MARKER_SIZE_M, cam_mat, dist_coef
        )

        # поворот по X
        turn_X = rvec[0][0][0]
        # поворот по Y
        turn_Y = rvec[0][0][1]

        # координата маркера по X
        X_coord = tvec[0][0][0]
        # координаты маркера по Y
        Y_coord = tvec[0][0][0]
        # дистанция до маркера (Z)
        distance_to_marker = tvec[0][0][2]
        return {X_coord, Y_coord, distance_to_marker, turn_X, turn_Y}
    else:
        return None


def getting_into_position(X_coord, Y_coord):
    """Направляет коптер на центр маркера"""
    pass


def correction(turn_X, turn_Y):
    """Поварачивает коптер по маркеру"""
    pass


def decline(status, distance):
    """Снижает высоту до маркера"""
    pass
