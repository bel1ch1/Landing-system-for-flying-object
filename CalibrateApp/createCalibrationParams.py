# Скрипт создает калибровачные парамеры для камеры используя фото из cb_img
"""Чтобы использовать этот скрипт создайте фото через скрипт get_images.py"""


import numpy as np
import cv2 as cv
import glob
import pickle


chessboardSize = (7, 7)
frameSize = (640,480)

criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)


# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((chessboardSize[0] * chessboardSize[1], 3), np.float32)
objp[:,:2] = np.mgrid[0:chessboardSize[0],0:chessboardSize[1]].T.reshape(-1,2)
prev_img_shape = None


# size_of_chessboard_squares_mm = 160
# objp = objp * size_of_chessboard_squares_mm


# Arrays to store object points and image points from all the images.
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.


images = glob.glob('./cb_img/*.png')

for image in images:

    img = cv.imread(image)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # Find the chess board corners
    ret, corners = cv.findChessboardCorners(
        gray, chessboardSize, cv.CALIB_CB_ADAPTIVE_THRESH \
            + cv.CALIB_CB_FAST_CHECK + cv.CALIB_CB_NORMALIZE_IMAGE
        )

    # If found, add object points, image points (after refining them)
    if ret:

        objpoints.append(objp)
        corners2 = cv.cornerSubPix(gray, corners, (11,11), (-1,-1), criteria)
        imgpoints.append(corners2)

        # Draw and display the corners
        cv.drawChessboardCorners(img, chessboardSize, corners2, ret)
        cv.imshow('img', img)
        cv.waitKey(1000)


cv.destroyAllWindows()


ret, cameraMatrix, dist, rvecs, tvecs = cv.calibrateCamera(
    objpoints, imgpoints, frameSize, None, None
    )


# Save the camera calibration result for later use (we won't worry about rvecs / tvecs)
pickle.dump((cameraMatrix, dist), open(
    "cb_params\\calibration.pkl", "wb" ))

pickle.dump(cameraMatrix, open(
    "cb_params\\cameraMatrix.pkl", "wb" ))

pickle.dump(dist, open(
    "cb_params\\dist.pkl", "wb" ))
