import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd

# --- Conf Database ---

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# --- Connect to Database --- 
if not firebase_admin._apps:
    cred = credentials.Certificate('/home/ale/Desktop/serviceAccountKey.json')
    firebase_admin.initialize_app(cred)
db = firestore.client()

# --- Get data from Firestore ---

info_user = db.collection('users')
docs = info_user.stream()
data_ci = []
for doc in docs:
      # Get ID from database
      data_ci.append(doc.id)

# -- Page sidebar
st.sidebar.markdown("# Configuración de experimento")

st.sidebar.warning('Si no encuentra su cuenta, debe crearla.')
select_id = st.sidebar.selectbox('Busque su ID (CI):',
                                    data_ci)
name = ''
value_group = []
docs = info_user.stream()
for doc in docs:
      # Get ID from database
      if select_id == doc.id:
          info = doc.to_dict()
          name = info['name']
          value_group = np.arange(1, len(info['group'])+1)

select_group = st.sidebar.selectbox('Busque el grupo:',
                                    value_group)
st.sidebar.success(name)


st.sidebar.markdown("# Crear cuenta")
title = st.sidebar.text_input('Nombre completo')
number = st.sidebar.number_input('Carnet de Identidad (CI)', 0, 100100100, 10010010,1)

if st.sidebar.button('Crear cuenta'):
      st.sidebar.write('Cuenta creada, puede buscar su ID.')



st.title('My first app')

st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))


chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)


map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)


if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data
