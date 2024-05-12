import cv2
import pickle


ARUCO_DICT = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_5X5_50)
MARKER_SIZE_M = 0.165 # Размер маркера
ARUCO_PARAM = cv2.aruco.DetectorParameters()
cap = cv2.VideoCapture(0)


# Подгружаем данные для определения дистанции
with open('camera_params//dist.pkl', 'rb') as f:
    dist_coef = pickle.load(f)

with open('camera_params//cameraMatrix.pkl', 'rb') as g:
    cam_mat = pickle.load(g)


while True:
    ret, frame = cap.read()

    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Ищем маркеры
    corners, _, _ = cv2.aruco.detectMarkers(gray, ARUCO_DICT, parameters=ARUCO_PARAM)

    if corners:

        # Определяем сдвиг
        rvec, tvec, _ = cv2.aruco.estimatePoseSingleMarkers(
            corners, MARKER_SIZE_M, cam_mat, dist_coef
        )



    cv2.imshow("frame", frame)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
