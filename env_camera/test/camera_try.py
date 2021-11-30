
# import the opencv library
import cv2
import numpy as np
  
# define a video capture object
vid = cv2.VideoCapture(0)
  
while(True):
      
    # Capture the video frame
    # by frame
    ret, frame = vid.read()
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    def max_mask(h, s, v):
        lower = (h, s, v)
        upper = (153, 255, 115)
        # upper = (180, 255, 255)
        mask = cv2.inRange(hsv, lower, upper)
        center = mask[:,0:int(frame.shape[1]*1)]
        center_total = np.array([np.sum(center)])
        center_total = np.max(center_total)
        return(center_total, mask)

    g_mask = max_mask(85, 57, 0)
    print('Valor mascara: ', g_mask[0])
    cv2.imshow("g_mask", (g_mask[1]))
    
    # Display the resulting frame
    cv2.imshow('frame', frame)
    cv2.imshow('hsv', hsv)



    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
  
# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()