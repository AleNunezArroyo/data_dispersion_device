import cv2
from object_detector import *
import numpy as np
import argparse


# pip install opencv-contrib-python
parameters = cv2.aruco.DetectorParameters_create()

aruco_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_5X5_50)

# Load Object Detector
detector = HomogeneousBgDetector()

# Load Cap
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

while True:
    _, img = cap.read()

    # Get Aruco marker
    corners, ids, rejected = cv2.aruco.detectMarkers(img, aruco_dict, parameters=parameters)

    # verify *at least* one ArUco marker was detected
    if ids is not None:
        # loop over the detected ArUCo corners
        
        for (markerCorner, markerID) in zip(corners, ids):
            
            # _________________________________________________________
            # Values to convert pixel to radio.
            # Draw polygon around the marker
            int_corners = np.int0(corners)
            cv2.polylines(img, int_corners, True, (0, 255, 0), 5)

            # Aruco Perimeter
            aruco_perimeter = cv2.arcLength(corners[0], True)

            # Pixel to cm ratio
            pixel_cm_ratio = aruco_perimeter / 20
            # _________________________________________________________
            
            corners = markerCorner.reshape((4, 2))
            (topLeft, topRight, bottomRight, bottomLeft) = corners

            # convert each of the (x, y)-coordinate pairs to integers
            topRight = (int(topRight[0]), int(topRight[1]))
            bottomRight = (int(bottomRight[0]), int(bottomRight[1]))
            bottomLeft = (int(bottomLeft[0]), int(bottomLeft[1]))
            topLeft = (int(topLeft[0]), int(topLeft[1]))
            
            # compute and draw the center (x, y)-coordinates of the ArUco
            # marker
            cX = int((topLeft[0] + bottomRight[0]) / 2.0)
            cY = int((topLeft[1] + bottomRight[1]) / 2.0)

            # Value of the marker
            object_width = ( ( ((topRight[0] - topLeft[0])**2) + ((topRight[1] - topLeft[1])**2) ) ** (1/2)) / pixel_cm_ratio
            object_height = ( ( ((topRight[0] - bottomRight[0])**2) + ((topRight[1] - bottomRight[1])**2) ) ** (1/2)) / pixel_cm_ratio

            cv2.putText(img, "Width {} cm".format(round(object_width, 1)), (int(cX - 100), int(cY - 20)), cv2.FONT_HERSHEY_PLAIN, 2, (100, 200, 0), 2)
            cv2.putText(img, "Height {} cm".format(round(object_height, 1)), (int(cX - 100), int(cY + 15)), cv2.FONT_HERSHEY_PLAIN, 2, (100, 200, 0), 2)

            cv2.circle(img, (cX, cY), 4, (0, 0, 255), -1)
            


            contours = detector.detect_objects(img)
            # Draw objects boundaries
            for cnt in contours:
                # Get rect
                rect = cv2.minAreaRect(cnt)
                (x, y), (w, h), angle = rect
                # Get Width and Height of the Objects by applying the Ratio pixel to cm
                object_width = w / pixel_cm_ratio
                object_height = h / pixel_cm_ratio

                if ( ( (object_width <= 2.5 and object_width >= 1.0) and (object_height <= 2.5 and object_height >= 1.0) ) ):
                    # Display rectangle
                    box = cv2.boxPoints(rect)
                    box = np.int0(box)

                    cv2.circle(img, (int(x), int(y)), 5, (0, 0, 255), -1)
                    cv2.polylines(img, [box], True, (255, 0, 0), 2)
                    cv2.putText(img, "Width {} cm".format(round(object_width, 1)), (int(x - 100), int(y - 20)), cv2.FONT_HERSHEY_PLAIN, 2, (100, 200, 0), 2)
                    cv2.putText(img, "Height {} cm".format(round(object_height, 1)), (int(x - 100), int(y + 15)), cv2.FONT_HERSHEY_PLAIN, 2, (100, 200, 0), 2)



    cv2.imshow("Image", img)
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()