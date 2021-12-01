# *************** [GUI] ****************
import urllib.request
import streamlit as st
import datetime
import numpy as np
from PIL import Image
import pandas as pd
# **************************************
# ************* [Database] *************
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import datetime
from datetime import timezone
if not firebase_admin._apps:
    cred = credentials.Certificate('/home/ale/Downloads/firestore-key.json')
    firebase_admin.initialize_app(cred)
db = firestore.client()
# **************************************
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
    # print(st.session_state.init)
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
    # print(len(df.loc[:,"Eje X"]))
    st.subheader("Imagen de dispersión")
    for c in range (len(df)):
        image = Image.open('lab'+str(c+1)+'.png')
        st.image(image, caption='Dispersión dato: '+str(c+1))
    
    if state == True:
        if st.button('Cargar la información a internet', key = '1'):
            st.session_state.init = 1
            st.write('Laboratorio guardado en internet')
            frank_ref = db.collection('laboratory').document(str(d))
            for c in range (len(df)):
                frank_ref.set({
                    str(number): {
                        'data'+str(c+1): {
                            'x_coordinate': df.loc[c,"Eje X"],
                            'y_coordinate': df.loc[c,"Eje Y"],
                            'distance_setpoint': df.loc[c,"Distancia del centro"],
                        },
                    },
                }, merge=True)