import cv2
import numpy as np

class HomogeneousBgDetector():
    def __init__(self):
        pass

    def circle_detector(self, frame):
        minRadius = 40 
        maxRadius = 50
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray_blur = cv2.GaussianBlur(gray, (3, 3), 0)
        circles = cv2.HoughCircles(gray_blur, 
                                cv2.HOUGH_GRADIENT, 
                                1, 
                                minDist=1,
                                param1=80,
                                param2=32,
                                minRadius=minRadius,
                                maxRadius=maxRadius)
        # convert circles into expected type
        circles = np.uint16(np.around(circles))
        return circles

    # def get_objects_rect(self):
    #     box = cv2.boxPoints(rect)  # cv2.boxPoints(rect) for OpenCV 3.x
    #     box = np.int0(box)