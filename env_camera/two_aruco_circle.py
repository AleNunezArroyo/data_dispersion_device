# import the OpenCV library for computer vision
import cv2
from object_detector import *
import numpy as np

# Load the dictionary that was used to generate the markers.
# There's different aruco marker dictionaries, this code uses 6x6
# dictionary = cv2.aruco.Dictionary_get(cv2.aruco.DICT_5X5_50)
dictionary = cv2.aruco.Dictionary_get(cv2.aruco.DICT_ARUCO_ORIGINAL)

# Initialize the detector parameters using default values
parameters = cv2.aruco.DetectorParameters_create()

# initialize the webcam as "camera" object
camera = cv2.VideoCapture(0)
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
# loop that runs the program forever
# at least until the "q" key is pressed

# Load Object Detector
detector = HomogeneousBgDetector()

x_0 = x_1 = y_0 = y_1 = 0

while True:

    # creates an "img" var that takes in a camera frame
    _, img = camera.read()

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # detect aruco tags within the frame
    markerCorners, markerIds, rejectedCandidates = cv2.aruco.detectMarkers(gray, dictionary, parameters=parameters)

    # draw box around aruco marker within camera frame
    img = cv2.aruco.drawDetectedMarkers(img, markerCorners, markerIds)

    # if a tag is found...
    if markerIds is not None:
        # for every tag in the array of detected tags...
        for i in range(len(markerIds)):
            # _________________________________________________________
            # Values to convert pixel to radio.
            # Draw polygon around the marker
            int_corners = np.int0(markerCorners)
            cv2.polylines(img, int_corners, True, (0, 255, 0), 5)

            # Aruco Perimeter
            aruco_perimeter = cv2.arcLength(markerCorners[0], True)

            # Pixel to cm ratio
            pixel_cm_ratio = aruco_perimeter / 8
            # pixel_cm_ratio = aruco_perimeter / 20
            # _________________________________________________________
            
            (topLeft, topRight, bottomRight, bottomLeft) = markerCorners[i][0]
            # convert each of the (x, y)-coordinate pairs to integers
            topRight = (int(topRight[0]), int(topRight[1]))
            bottomRight = (int(bottomRight[0]), int(bottomRight[1]))
            bottomLeft = (int(bottomLeft[0]), int(bottomLeft[1]))
            topLeft = (int(topLeft[0]), int(topLeft[1]))

            # draw the bounding box of the ArUCo detection
            cv2.line(img, topLeft, topRight, (0, 255, 0), 2)
            cv2.line(img, topRight, bottomRight, (0, 255, 0), 2)
            cv2.line(img, bottomRight, bottomLeft, (0, 255, 0), 2)
            cv2.line(img, bottomLeft, topLeft, (0, 255, 0), 2)

            # compute and draw the center (x, y)-coordinates of the ArUco
            # marker
            cX = int((topLeft[0] + bottomRight[0]) / 2.0)
            cY = int((topLeft[1] + bottomRight[1]) / 2.0)

            # Value of the marker
            object_width = ( ( ((topRight[0] - topLeft[0])**2) + ((topRight[1] - topLeft[1])**2) ) ** (1/2)) / pixel_cm_ratio
            object_height = ( ( ((topRight[0] - bottomRight[0])**2) + ((topRight[1] - bottomRight[1])**2) ) ** (1/2)) / pixel_cm_ratio

            # print(markerIds[0])
            # if 0 in markerIds:
            if i == 0:
                cv2.putText(img, "Tag 0 Detected!", (25, 400), cv2.FONT_HERSHEY_COMPLEX, 0.7,
                            (0, 255, 0), 2)
                x_0 = bottomLeft[0]
                y_0 = bottomLeft[1]
                print("Valor x_0: ", x_0)
                print("Valor y_0: ", y_0)
                print(bottomLeft)
                print("________")
            if i == 1:
                cv2.putText(img, "Tag 1 Detected!", (25, 425), cv2.FONT_HERSHEY_COMPLEX, 0.7,
                            (0, 255, 0), 2)
                x_1 = topRight[0]
                y_1 = topRight[1]
                print("Valor x_1: ", x_1)
                print("Valor y_1: ", y_1)
                print(topRight)
                print("________")
            
            contours = detector.detect_objects(img)
            # Draw objects boundaries
            for cnt in contours:
                # Get rect
                rect = cv2.minAreaRect(cnt)
                (x, y), (w, h), angle = rect
                # Get Width and Height of the Objects by applying the Ratio pixel to cm
                object_width = w / pixel_cm_ratio
                object_height = h / pixel_cm_ratio

                if ( ( (object_width <= 5 and object_width >= 1.2) and (object_height <= 5 and object_height >= 1.2) ) ):
                    # Display rectangle
                    box = cv2.boxPoints(rect)
                    box = np.int0(box)

                    cv2.circle(img, (int(x), int(y)), 5, (0, 0, 255), -1)
                    cv2.polylines(img, [box], True, (255, 0, 0), 2)
                    cv2.putText(img, "Width {} cm".format(round(object_width, 1)), (int(x - 100), int(y - 20)), cv2.FONT_HERSHEY_PLAIN, 2, (100, 200, 0), 2)
                    cv2.putText(img, "Height {} cm".format(round(object_height, 1)), (int(x - 100), int(y + 15)), cv2.FONT_HERSHEY_PLAIN, 2, (100, 200, 0), 2)
            
            # Draw space:
            centro_total_x = int((x_0 + x_1) / 2.0)
            centro_total_y = int((y_0 + y_1) / 2.0)

            diagonal_line = ( ( ((x_0 - x_1)**2) + ((y_0 - y_1)**2) ) ** (1/2)) / pixel_cm_ratio

            cv2.circle(img, (int(centro_total_x), int(centro_total_y)), 20, (0, 0, 255), -1)

            cv2.putText(img, "Width {} cm".format(round(object_width, 1)), (int(cX - 100), int(cY - 20)), cv2.FONT_HERSHEY_PLAIN, 2, (100, 200, 0), 2)
            cv2.putText(img, "Height {} cm".format(round(object_height, 1)), (int(cX - 100), int(cY + 15)), cv2.FONT_HERSHEY_PLAIN, 2, (100, 200, 0), 2)
            cv2.putText(img, "Diagonal {} cm".format(round(diagonal_line, 1)), (300, 400), cv2.FONT_HERSHEY_PLAIN, 2, (100, 200, 0), 2)

            cv2.line(img, (x_0, y_0), (x_1, y_1), (255, 0, 0), 2)
            cv2.circle(img, (cX, cY), 4, (0, 0, 255), -1)
            




    # Display the resulting frame
    cv2.imshow('frame', img)

    # handler to press the "q" key to exit the program
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
camera.release()
cv2.destroyAllWindows()