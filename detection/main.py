import cv2


cap = cv2.VideoCapture(0)


while cap.isOpened():

    success, frame = cap.read()

    if not success:
        break

    pass

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
