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
if st.sidebar.button('Crear laboratorio'):
    st.sidebar.write('Laboratorio creado')
    

col1, col2 = st.columns([3, 1])
data = np.random.randn(10, 1)

col1.subheader("A wide column with a chart")
col1.line_chart(data)
image = Image.open('/home/ale/Documents/GitHub/data_dispersion_device/env_camera/opencv0.png')
st.image(image, caption='Sunrise by the mountains')

col2.subheader("Información")
col2.write(data)

st.info('This is a purely informational message')