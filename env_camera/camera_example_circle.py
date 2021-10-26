
# import the opencv library
import cv2
import numpy as np
# define a video capture object
# pip3 install opencv-python
# pip3 install opencv-python 

# sudo apt-get install libatlas-base-dev 

# sudo apt-get install libjasper-dev 

# sudo apt-get install libqtgui4 

# sudo apt-get install python3-pyqt5 

# sudo apt install libqt4-test

vid = cv2.VideoCapture(0)
  
while(True):
      
    # Capture the video frame
    # by frame
    _, frame = vid.read()
    
    cv2.imshow('frame', frame)

    # for drawing circles on
    circles_im = np.copy(frame)

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
    # draw each one
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