import cv2

from detection import pose_esitmation, correction, decline
from constantes import ARUCO_DICT

cap = cv2.VideoCapture(0)


while cap.isOpened():

    success, frame = cap.read()

    if not success:
        break

    position = pose_esitmation(frame, ARUCO_DICT)

    if position:
        correction()
        decline()


    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
