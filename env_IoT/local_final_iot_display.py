import streamlit as st
from google.cloud import firestore
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
import datetime
from datetime import timezone
import json
# --- Conf Database ---

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

from google.oauth2 import service_account

# --- Connect to Database --- 
if not firebase_admin._apps:
    cred = credentials.Certificate('/home/ale/Downloads/firestore-key.json')
    firebase_admin.initialize_app(cred)
db = firestore.client()

# # --- Connect to Database --- 
# if not firebase_admin._apps:
#     key_dict = json.loads(st.secrets["textkey"])
#     creds = credentials.Certificate(key_dict)
#     firebase_admin.initialize_app(creds)
# db = firestore.client()


# --- Get data from Firestore ---
info_lab = db.collection('laboratory')
docs = info_lab.stream()
data_date = []
for doc in docs:
    # Get ID from database
    data_date.append(doc.id)

# -- Page sidebar
st.sidebar.markdown("# Selección de laboratorio")
st.sidebar.warning('Si no encuentra el laboratorio debe crearlo.')
select_id = st.sidebar.selectbox('Busque la fecha de laboratorio:',
                                    data_date)
name = ''
lab_number = []
docs = info_lab.stream()
for doc in docs:
    # Get ID from database
    if select_id == doc.id:
        lab_data = doc.to_dict()
        lab_number = np.arange(1, len(lab_data)+1)

select_number = st.sidebar.selectbox('Busque el número de laboratorio:',
                                    lab_number)
# Group the data in array
# Search all data in each lab number
v_x_coordinate = []
v_y_coordinate = []
v_d_coordinate = []

for i in (range(len(lab_data[str(select_number)]))):
    v_x_coordinate.append(lab_data[str(select_number)]['data'+str(i+1)]['x_coordinate'])
    v_y_coordinate.append(lab_data[str(select_number)]['data'+str(i+1)]['y_coordinate'])
    v_d_coordinate.append(lab_data[str(select_number)]['data'+str(i+1)]['distance_setpoint'])

st.title('Data Dispersion Device')
st.write("Despliegue de datos")

df1 = pd.DataFrame({'Eje X': v_x_coordinate,
                   'Eje Y': v_y_coordinate, 
                   'Distancia del centro': v_d_coordinate})

st.write(df1)

st.vega_lite_chart(df1, {
    'mark': {'type': 'circle', 'tooltip': True},
    'encoding': {
        'x': {'field': 'Eje X', 'type': 'quantitative'},
        'y': {'field': 'Eje Y', 'type': 'quantitative'},
    },
})

@st.cache
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')
csv = convert_df(df1)
st.download_button(
    label="Download data as CSV",
    data=csv,
    file_name='information_ddd.csv',
    mime='text/csv',
)
