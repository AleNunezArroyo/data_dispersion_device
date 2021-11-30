import cv2
import numpy as np

class HomogeneousBgDetectorCircle():
    def __init__(self):
        pass

    def circle_detector(self, frame):
        minRadius = 18
        maxRadius = 30
        # Initial values
        # minRadius = 18 
        # maxRadius = 50
        # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # gray_blur = cv2.GaussianBlur(gray, (3, 3), 0)
        minRadius = 18 #@param {type:"slider", min:0, max:100, step:1}
        maxRadius = 30 #@param {type:"slider", min:0, max:100, step:1}

        circles = cv2.HoughCircles(frame, 
                                cv2.HOUGH_GRADIENT, 
                                1, 
                                minDist=90,
                                param1=70,
                                param2=11,
                                minRadius=minRadius,
                                maxRadius=maxRadius)

        # convert circles into expected type
        circles = np.uint16(np.around(circles))
        return circles

    # def get_objects_rect(self):
    #     box = cv2.boxPoints(rect)  # cv2.boxPoints(rect) for OpenCV 3.x
    #     box = np.int0(box)