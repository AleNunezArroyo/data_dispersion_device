import urllib.request
import streamlit as st
import datetime
import numpy as np
from PIL import Image
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
print(state)

if state == True:
    st.sidebar.success('Hay conexión a internet')
    st.sidebar.warning('El experimento puede funcionar y los datos se guardan en línea.')
else:
    st.sidebar.error('No hay conexión a internet')
    st.sidebar.warning('El experimento puede funcionar pero los datos no se guardan.')

st.sidebar.markdown("# Crear nuevo laboratorio")
d = st.sidebar.date_input("Fecha de laboratorio",datetime.date(2021, 7, 6))
number = st.sidebar.number_input('Número de laboratorio', 1, 10, 1,1)
state_new_lab = 0
if st.sidebar.button('Crear laboratorio', key="1"):
    state_new_lab = 1
    st.sidebar.write('Laboratorio creado')

state_button = 0
if state_new_lab == 1:
    # Título
    st.info('Laboratorio número: '+ str(number) +' - Fecha: '+str(d))
    # Leer dato
    if st.button('Iniciar lectura de datos', key="2"):
        state_button += 2
        st.write('Esperando caida de esfera')
    
    if state_button % 2 == 0:
        col1, col2 = st.columns([3, 1])
        data = np.random.randn(10, 1)

        col1.subheader("A wide column with a chart")
        col1.line_chart(data)
        image = Image.open('/home/ale/Documents/GitHub/data_dispersion_device/env_camera/opencv0.png')
        st.image(image, caption='Imagen de la lectura de datos')

        col2.subheader("Información")
        col2.write(data)

print(state_new_lab)  