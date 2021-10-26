
# import the opencv library
import cv2
  
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
    ret, frame = vid.read()
    
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