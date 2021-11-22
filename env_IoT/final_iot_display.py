import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
import datetime
from datetime import timezone

# --- Conf Database ---

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# --- Connect to Database --- 
if not firebase_admin._apps:
    cred = credentials.Certificate('/home/ale/Downloads/datadispersiondevice-b2e58-firebase-adminsdk-w33zc-b52a8406e5.json')
    firebase_admin.initialize_app(cred)
db = firestore.client()

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
value_group = []
docs = info_lab.stream()
for doc in docs:
      # Get ID from database
      if select_id == doc.id:
          info = doc.to_dict()
        #   name = info['1']
          value_group = np.arange(1, len(info['2'])+1)

select_group = st.sidebar.selectbox('Busque el número de laboratorio:',
                                    value_group)


st.title('Data Dispersion Device')

st.write("Despliegue de datos")
st.write(pd.DataFrame({
    'Coordenada x': [1, 2, 3, 4],
    'Coordenada y': [10, 20, 30, 40],
    'Distancia del centro': [10, 20, 30, 40]
}))

df1 = pd.DataFrame({'Eje X': [1, 2, 3, 4],
                   'Eje Y': [10, 20, 30, 40]})
index_ = [4]
# print(df1)
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
