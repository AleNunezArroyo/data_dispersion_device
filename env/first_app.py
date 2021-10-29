import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd

# -- Page sidebar
st.sidebar.markdown("# Configuración de experimento")

st.sidebar.warning('Si no encuentra su cuenta, debe crearla.')
select_id = st.sidebar.selectbox('Busque su ID (CI):',
                                    [10410426, 123, 321])
select_group = st.sidebar.selectbox('Busque el grupo:',
                                    [1, 2, 3])
st.sidebar.success('Alejandro Núñez Arroyo')


st.sidebar.markdown("# Crear cuenta")
title = st.sidebar.text_input('Nombre completo')
number = st.sidebar.number_input('Carnet de Identidad (CI)', 0, 100100100, 10010010,1)
genre = st.sidebar.radio(
  "¿Cuál es su género?",
('Masculino', 'Femenino', 'Prefiero no decirlo'))

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


# option = st.selectbox('Which number do you like best?')


# option = st.sidebar.selectbox('Which number do you like best?')


left_column, right_column = st.columns(2)
pressed = left_column.button('Press me?')
if pressed:
  right_column.write("Woohoo!")

expander = st.expander("FAQ")
expander.write("Here you could put in some really, really long explanations...")


import time
'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

'...and now we\'re done!'