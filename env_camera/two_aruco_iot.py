# import the OpenCV library for computer vision
import cv2
# from object_detector import *
from circle_detector import *
import numpy as np
import streamlit as st

# *************** [GUI] ***************
import urllib.request
import streamlit as st
import datetime
import numpy as np
from PIL import Image
import pandas as pd
# *************************************

# Load the dictionary that was used to generate the markers.
# There's different aruco marker dictionaries, this code uses 6x6
# dictionary = cv2.aruco.Dictionary_get(cv2.aruco.DICT_5X5_50)
dictionary = cv2.aruco.Dictionary_get(cv2.aruco.DICT_ARUCO_ORIGINAL)

# Initialize the detector parameters using default values
parameters = cv2.aruco.DetectorParameters_create()

# initialize the webcam as "camera" object
camera = cv2.VideoCapture(0)
# we dont use set for problems with camera 
# camera.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
# camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

# Load Object Detector
detector = HomogeneousBgDetectorCircle()

x_0 = x_1 = y_0 = y_1 = 0
bool_v = True
fun_counter = 0 
(mark_counter) = 0



# *************** [GUI] ***************
# Connec to internet
state = False
def connect(host='http://google.com'):
    try:
        urllib.request.urlopen(host) #Python 3.x
        return True
    except:
        return False
# is state == True, we have internet connection
if connect() == False:
    state = False
else:
    state = True
# Connection state internet 
# print(state)

# session_state information for create a lab
if 'create' not in st.session_state:
    st.session_state.create = 0
if 'init' not in st.session_state:
    st.session_state.init = 0
# *************************************
    
# *************** [GUI] ***************    
if state == True:
    st.sidebar.success('Hay conexión a internet')
    st.sidebar.warning('El experimento puede funcionar y los datos se guardan en línea.')
else:
    st.sidebar.error('No hay conexión a internet')
    st.sidebar.warning('El experimento puede funcionar pero los datos no se guardan.')

st.sidebar.markdown("# Crear nuevo laboratorio")
d = st.sidebar.date_input("Fecha de laboratorio",datetime.date(2021, 7, 6))
number = st.sidebar.number_input('Número de laboratorio', 1, 10, 1,1)

if st.sidebar.button('Crear laboratorio', key = '0'):
    st.session_state.create = 1
    st.sidebar.write('Laboratorio creado')
    


if st.session_state.create == 1:
    # Título
    st.header('Laboratorio número: '+ str(number) +' - Fecha: '+str(d))
    
    # Leer dato
    init_lecture = st.button('Tomar muestra', key = '1')
    if (init_lecture):
        st.session_state.init += 1
        st.write('Esperando caída '+str(st.session_state.init)+' de esfera: ...')
        
        run = st.checkbox('Run')
        FRAME_WINDOW = st.image([])

        while run:
            # creates an "img" var that takes in a camera frame
            _, img = camera.read()
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            FRAME_WINDOW.image(img)
            # img_circle = img
            # # Convert to grayscale
            # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            # # detect aruco tags within the frame
            # markerCorners, markerIds, rejectedCandidates = cv2.aruco.detectMarkers(gray, dictionary, parameters=parameters)

            # # draw box around aruco marker within camera frame
            # img = cv2.aruco.drawDetectedMarkers(img, markerCorners, markerIds)

            # # if a tag is found...
            # if markerIds is not None:
            #     # for every tag in the array of detected tags...
            #     for i in range(len(markerIds)):
            #         # _________________________________________________________
            #         # Values to convert pixel to radio.
            #         # Draw polygon around the marker
            #         int_corners = np.int0(markerCorners)
            #         cv2.polylines(img, int_corners, True, (0, 255, 0), 5)

            #         # Aruco Perimeter
            #         aruco_perimeter = cv2.arcLength(markerCorners[0], True)

            #         # Pixel to cm ratio convertion
            #         pixel_cm_ratio = aruco_perimeter / 8
            #         # pixel_cm_ratio = aruco_perimeter / 20
            #         # _________________________________________________________
                    
            #         (topLeft, topRight, bottomRight, bottomLeft) = markerCorners[i][0]
                    
            #         # convert each of the (x, y)-coordinate pairs to integers
            #         topRight = (int(topRight[0]), int(topRight[1]))
            #         bottomRight = (int(bottomRight[0]), int(bottomRight[1]))
            #         bottomLeft = (int(bottomLeft[0]), int(bottomLeft[1]))
            #         topLeft = (int(topLeft[0]), int(topLeft[1]))

            #         # draw the bounding box of the ArUCo detection
            #         cv2.line(img, topLeft, topRight, (0, 255, 0), 2)
            #         cv2.line(img, topRight, bottomRight, (0, 255, 0), 2)
            #         cv2.line(img, bottomRight, bottomLeft, (0, 255, 0), 2)
            #         cv2.line(img, bottomLeft, topLeft, (0, 255, 0), 2)

            #         # compute and draw the center (x, y)-coordinates of the ArUco
            #         # marker
            #         # cX = int((topLeft[0] + bottomRight[0]) / 2.0)
            #         # cY = int((topLeft[1] + bottomRight[1]) / 2.0)

            #         # Value of the marker
            #         object_width = ( ( ((topRight[0] - topLeft[0])**2) + ((topRight[1] - topLeft[1])**2) ) ** (1/2)) / pixel_cm_ratio
            #         object_height = ( ( ((topRight[0] - bottomRight[0])**2) + ((topRight[1] - bottomRight[1])**2) ) ** (1/2)) / pixel_cm_ratio

            #         # marker ids 
            #         if i == 0:
            #             cv2.putText(img, "Tag 0 Detected!", (25, 400), cv2.FONT_HERSHEY_COMPLEX, 0.7,
            #                         (0, 255, 0), 2)
            #             x_0 = topRight[0]
            #             y_0 = topRight[1]

            #         if i == 1:
            #             cv2.putText(img, "Tag 1 Detected!", (25, 425), cv2.FONT_HERSHEY_COMPLEX, 0.7,
            #                         (0, 255, 0), 2)
            #             x_1 = topRight[0]
            #             y_1 = topRight[1]
                        
            #         circles_im = np.copy(img_circle)
            #         # contours = detector.detect_objects(img)
                    
            #         # the code works when detec a circle 
            #         try: 
            #             circles = detector.circle_detector(img_circle)
            #             cv2.imshow('img_circle', img_circle) 
            #             medium_center_circle_x = 0
            #             medium_center_circle_y = 0
            #             counter = 0 
            #             for circle in circles[0,:]:
            #                 counter += 1
            #                 # draw the outer circle
            #                 cv2.circle(circles_im,(circle[0],circle[1]),circle[2],(255,0,0),2)
            #                 # draw the center of the circle
            #                 cv2.circle(circles_im,(circle[0],circle[1]),2,(0,0,255),3)
            #                 # average circle from ball
            #                 medium_center_circle_x = circle[0] + medium_center_circle_x
            #                 medium_center_circle_y = circle[1] + medium_center_circle_y
                        
            #             cv2.imshow('circles_im', circles_im) 

            #             medium_center_circle_x = medium_center_circle_x/counter
            #             medium_center_circle_y = medium_center_circle_y/counter
            #             # Draw space:
            #             centro_total_x = int((x_0 + x_1) / 2.0)
            #             centro_total_y = int((y_0 + y_1) / 2.0)

            #             diagonal_line = ( ( ((x_0 - x_1)**2) + ((y_0 - y_1)**2) ) ** (1/2)) / pixel_cm_ratio

            #             dif_line = ( ( ((centro_total_x - medium_center_circle_x)**2) + ((centro_total_y - medium_center_circle_y)**2) ) ** (1/2)) / pixel_cm_ratio

            #             print("center x", medium_center_circle_x, "center y", medium_center_circle_y, "distancia", dif_line)
            #             print("center circle: ", centro_total_x, centro_total_y)
            #             # Center circle 
            #             cv2.circle(img, (int(centro_total_x), int(centro_total_y)), 6, (0, 0, 255), -1)
            #             # Put value of detection
            #             # cv2.putText(img, "Width {} cm".format(round(object_width, 1)), (int(cX - 100), int(cY - 20)), cv2.FONT_HERSHEY_PLAIN, 2, (100, 200, 0), 2)
            #             # cv2.putText(img, "Height {} cm".format(round(object_height, 1)), (int(cX - 100), int(cY + 15)), cv2.FONT_HERSHEY_PLAIN, 2, (100, 200, 0), 2)
            #             # cv2.putText(img, "Diagonal {} cm".format(round(diagonal_line, 1)), (300, 400), cv2.FONT_HERSHEY_PLAIN, 2, (100, 200, 0), 2)
            #             cv2.putText(img, "Diferencia {} cm".format(round(dif_line, 1)), (300, 400), cv2.FONT_HERSHEY_PLAIN, 2, (100, 200, 0), 2)

            #             cv2.line(img, (x_0, y_0), (x_1, y_1), (255, 0, 0), 2)
            #             # cv2.line(img, (centro_total_x, centro_total_y), (medium_center_circle_x, medium_center_circle_y), (255, 0, 0), 2)
            #             # Draw the center of aruko marker
            #             # cv2.circle(img, (cX, cY), 4, (0, 0, 255), -1)
            #             if ((centro_total_x > 300 and centro_total_x < 320) and (centro_total_y > 244 and centro_total_y < 264)):
            #                 if fun_counter == 2:
            #                     print("entra condicion")
            #                     cv2.imwrite('opencv'+'0'+'.png', circles_im)
            #                     fun_counter += 1
            #                 else: 
            #                     fun_counter += 1
            #             # Show image 
                        
            #         except:
            #             run 
        else:
            st.write('Stopped')
    col1, col2 = st.columns([1, 1])
    data = np.random.randn(6, 2)

    col1.subheader("Gráfica de dispersión")

    v_x_coordinate = [1, 2, 3, 4, 5]
    v_y_coordinate = [1, 2, 3, 4, 5]
    
    df1 = pd.DataFrame({'Eje X': v_x_coordinate,
                'Eje Y': v_y_coordinate})
                        
    col1.vega_lite_chart(df1, {
        'mark': {'type': 'circle', 'tooltip': True},
        'encoding': {
            'x': {'field': 'Eje X', 'type': 'quantitative'},
            'y': {'field': 'Eje Y', 'type': 'quantitative'},
        },
    })
    col1.subheader("Medida")
    image = Image.open('/home/ale/Documents/GitHub/data_dispersion_device/env_camera/image_live.png')
    st.image(image, caption='Imagen de la lectura de datos')

    col2.subheader("Tabla de datos")
    col2.write(data)
    
# *************************************   


# When everything done, release the capture
camera.release()
cv2.destroyAllWindows()