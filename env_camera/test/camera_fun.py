from circle_detector import *
import cv2
import numpy as np

vid = cv2.VideoCapture(0)
detector = HomogeneousBgDetectorCircle()
bool_v = True
while(bool_v):
      
    # Capture the video frame
    # by frame
    _, frame = vid.read()
    
    ## convert to hsv
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_range = np.array([61, 48, 116])
    upper_range = np.array([94, 186, 214])
        
    ## mask of green (36,0,0) ~ (70, 255,255)
    mask1 = cv2.inRange(hsv, lower_range, upper_range)
    
    cv2.imshow('frame', frame) 
    cv2.imshow('mask1', mask1) 
    try:
        circles = detector.circle_detector(mask1)

        for circle in circles[0,:]:
        # draw the outer circle
            cv2.circle(frame,(circle[0],circle[1]),circle[2],(0,255,0),2)
            # draw the center of the circle
            cv2.circle(frame,(circle[0],circle[1]),2,(0,0,255),3)
            
        
        cv2.imshow('final frame', frame)   
        print('Circles shape: ', circles.shape)

        # the 'q' button is set as the
        # quitting button you may use any
        # desired button of your choice
        
    except:
        bool_v
    if cv2.waitKey(1) & 0xFF == ord('q'):
            break
  
# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()