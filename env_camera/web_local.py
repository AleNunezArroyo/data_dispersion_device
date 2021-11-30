# import the OpenCV library for computer vision
import cv2
# from object_detector import *
from circle_detector import *
import numpy as np
import streamlit as st

import cv2
import streamlit as st

# *************** [GUI] ***************
import urllib.request
import streamlit as st
import datetime
import numpy as np
from PIL import Image
import cv2
import pandas as pd

# print (two_aruco_circle.x)

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
# *************************************

if st.session_state.create == 1:
    # Título
    st.header('Laboratorio número: '+ str(number) +' - Fecha: '+str(d))
    
    # Leer dato
    init_lecture = st.button('Tomar muestra', key = '1')
    if (init_lecture):
        st.session_state.init += 1
        st.write('Esperando caída '+str(st.session_state.init)+' de esfera: ...')
        st.write('Esperando caída '+str(st.session_state.init)+' de esfera: ...')
        import two_aruco_circle
        print (two_aruco_circle.dif_line)
        
        
        # while(st.session_state.init % 2 == 0):
        
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
    image = Image.open('opencv0.png')
    st.image(image, caption='Imagen de la lectura de datos')

    col2.subheader("Tabla de datos")
    col2.write(data)