# import the OpenCV library for computer vision
import cv2
# from object_detector import *
from circle_detector import *
from two_aruco_fun import *
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
detector = response_code_python()
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
    print(st.session_state.init)
    if (st.session_state.init%2 == 0):
        print("el pepe")
        # while(st.session_state.init % 2 == 0):
    # else:
    #     import two_aruco_circle
    #     print (two_aruco_circle.state_dif_line, 'eliminado')
    #     del (two_aruco_circle.state_dif_line)
        
        
    # elpepe = detector.value_out(st.session_state.init)
    # print(elpepe)
    



    st.subheader("Medida de dispersión")

    df = pd.read_csv("experiment.csv") 
    st.write(df)         
    st.subheader("Gráfica de dispersión")
    st.vega_lite_chart(df, {
        'mark': {'type': 'circle', 'tooltip': True},
        'encoding': {
            'x': {'field': 'Eje X', 'type': 'quantitative'},
            'y': {'field': 'Eje Y', 'type': 'quantitative'},
        },
    })
    
    # image = Image.open('opencv0.png')
    # st.image(image, caption='Imagen de la lectura de datos')