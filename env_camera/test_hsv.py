import cv2
import numpy as np
from circle_detector import *
detector = HomogeneousBgDetectorCircle()
cap = cv2.VideoCapture(0)
bool_v = True
while(bool_v):
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Basic
    # lower_red = np.array([94, 48, 68])
    # upper_red = np.array([150, 197, 255])
    # Noche
    lower_red = np.array([95, 47, 138])
    upper_red = np.array([179, 255, 255])
    
    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(frame,frame, mask= mask)

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    
    try: 
        circles = detector.circle_detector(res)
        print(circles)
        for circle in circles[0,:]:

            # draw the outer circle
            cv2.circle(frame,(circle[0],circle[1]),circle[2],(255,0,0),2)
            # draw the center of the circle
            cv2.circle(frame,(circle[0],circle[1]),2,(0,0,255),3)
            # average circle from ball
            
        cv2.imshow('circles_im', frame) 
    except:
        bool_v           
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()