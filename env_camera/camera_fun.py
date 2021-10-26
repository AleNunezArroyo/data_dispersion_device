from circle_detector import *
import cv2
import numpy as np

vid = cv2.VideoCapture(0)

detector = HomogeneousBgDetector()
while(True):
      
    # Capture the video frame
    # by frame
    _, frame = vid.read()
    
    cv2.imshow('frame', frame)

    # for drawing circles on
    circles_im = np.copy(frame)

    # draw each one
    circles = detector.circle_detector(frame)
    for circle in circles[0,:]:
        # draw the outer circle
        cv2.circle(circles_im,(circle[0],circle[1]),circle[2],(0,255,0),2)
        # draw the center of the circle
        cv2.circle(circles_im,(circle[0],circle[1]),2,(0,0,255),3)
    
    cv2.imshow('circles_im', circles_im)   
    print('Circles shape: ', circles.shape)

    # Display the resulting frame
    cv2.imshow('frame', frame)

    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
  
# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()