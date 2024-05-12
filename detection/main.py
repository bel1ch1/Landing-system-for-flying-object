import cv2

from detection import pose_estmition, getting_into_position, correction, decline
from constantes import ARUCO_DICT

cap = cv2.VideoCapture(0)


while True:

    success, frame = cap.read()

    if not success:
        break

    #X_coord, Y_coord, distance_to_marker, turn_X, turn_Y
    pose_params = pose_estmition(frame, ARUCO_DICT)

    if pose_params != None:
        getting_into_position(pose_params[0], pose_params[1])
        correction(pose_params[-2], pose_params[-1])
        decline(pose_params[2])
    else:
        print("Not found")

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
