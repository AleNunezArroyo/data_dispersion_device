import streamlit as st
from google.cloud import firestore
import datetime
#import firebase_admin
#from firebase_admin import credentials
#from firebase_admin import firestore
from datetime import timezone
import numpy as np
import pandas as pd
#import seaborn as sns
#import plotly.figure_factory as ff
#import matplotlib.pyplot as plt

# With:
import json


#key_dict = json.loads(st.secrets["textkey"])
keyfile_data = json.loads(st.secrets["textkey"])
#creds = ServiceAccountCredentials.from_json_keyfile_name(key-to-toml, scope)
#creds = ServiceAccountCredentials.from_json_keyfile_name(key_dict)
#creds = service_account.Credentials.from_service_account_info(key-to-toml, scope)
#creds = ServiceAccountCredentials.from_json_keyfile_dict(keyfile_data)
#db = firestore.Client(credentials=creds, project="streamlit-reddit")

db = firestore.Client.from_service_account_json("firestore-key.json")


apptitle = 'Data Dispersion Device'

st.set_page_config(page_title=apptitle, page_icon=":eyeglasses:")

st.title('Data Dispersion Device')




# -- Page sidebar
st.sidebar.markdown("# Seleccion de Laboratorio")
select_event = st.sidebar.selectbox('Laboratorio',['Laboratorio 1 31-10-2021','Laboratorio 2 1-11-2021', 'Laboratorio 3 2-11-2021'])
if select_event == 'Laboratorio 1 31-10-2021':
	coleccion='Laboratorio 1 31-10-2021'

if select_event == 'Laboratorio 2 1-11-2021':
	coleccion='Laboratorio 2 1-11-2021'	

if select_event == 'Laboratorio 3 2-11-2021':
	coleccion='Laboratorio 3 2-11-2021'	
	



# -- Default detector list
detectorlist = ['Laboratorio 3 2-11-2021','Laboratorio 3 2-11-2021', 'Laboratorio 3 2-11-2021']


posts_ref  = db.collection(coleccion).where(u'tabla', u'==', "tabla1")

for doc in posts_ref.stream():
	post = doc.to_dict()
	Adato_1 = post["dato1"]
	Adato_2 = post["dato2"]
	Adato_3 = post["dato3"]
	Adato_4 = post["dato4"]
	Adato_5 = post["dato5"]
	Adato_6 = post["dato6"]
	#url = post["url"]

	#print(1dato_1[0])
	#print(1dato_1[1])
	#print(1dato_1[2])
	#st.write(f":link: [{url}]({url})")


posts_ref  = db.collection(coleccion).where(u'tabla', u'==', "tabla2")

for doc in posts_ref.stream():
	post = doc.to_dict()
	Bdato_1 = post["dato1"]
	Bdato_2 = post["dato2"]
	Bdato_3 = post["dato3"]
	Bdato_4 = post["dato4"]
	Bdato_5 = post["dato5"]
	Bdato_6 = post["dato6"]

posts_ref  = db.collection(coleccion).where(u'tabla', u'==', "tabla3")

for doc in posts_ref.stream():
	post = doc.to_dict()
	Cdato_1 = post["dato1"]
	Cdato_2 = post["dato2"]
	Cdato_3 = post["dato3"]
	Cdato_4 = post["dato4"]
	Cdato_5 = post["dato5"]
	Cdato_6 = post["dato6"]



st.write(coleccion)
st.write("Tabla 1")
st.write(pd.DataFrame({
    'Cordenada x': [Adato_1[0], Adato_2[0], Adato_3[0], Adato_4[0],Adato_5[0],Adato_6[0]],
    'Cordenada y': [Adato_1[1], Adato_2[1], Adato_3[1], Adato_4[1],Adato_5[1],Adato_6[1]],
    'Distancia de centro': [Adato_1[2], Adato_2[2], Adato_3[2], Adato_4[2],Adato_5[2],Adato_6[2]],}))

df1 = pd.DataFrame({'Eje X':[Adato_1[0], Adato_2[0], Adato_3[0], Adato_4[0],Adato_5[0],Adato_6[0]],
                   'Eje Y':[Adato_1[1], Adato_2[1], Adato_3[1], Adato_4[1],Adato_5[1],Adato_6[1]]})
index_ = ['1', '2', '3', '4', '5','6']
st.vega_lite_chart(df1, {
    'mark': {'type': 'circle', 'tooltip': True},
    'encoding': {
        'x': {'field': 'Eje X', 'type': 'quantitative'},
	'y': {'field': 'Eje Y', 'type': 'quantitative'},
    },
}
)


st.write("Tabla 2")
st.write(pd.DataFrame({
    'Cordenada x': [Bdato_1[0], Bdato_2[0], Bdato_3[0], Bdato_4[0],Bdato_5[0],Bdato_6[0]],
    'Cordenada y': [Bdato_1[1], Bdato_2[1], Bdato_3[1], Bdato_4[1],Bdato_5[1],Bdato_6[1]],
    'Distancia de centro': [Bdato_1[2], Bdato_2[2], Bdato_3[2], Bdato_4[2],Bdato_5[2],Bdato_6[2]],
})
)

df2 = pd.DataFrame({'Eje X':[Bdato_1[0], Bdato_2[0], Bdato_3[0], Bdato_4[0],Bdato_5[0],Bdato_6[0]],
                   'Eje Y':[Bdato_1[1], Bdato_2[1], Bdato_3[1], Bdato_4[1],Bdato_5[1],Bdato_6[1]]})
index_ = ['1', '2', '3', '4', '5','6']
st.vega_lite_chart(df2, {
    'mark': {'type': 'circle', 'tooltip': True},
    'encoding': {
        'x': {'field': 'Eje X', 'type': 'quantitative'},
	'y': {'field': 'Eje Y', 'type': 'quantitative'},
    },
}
)

st.write("Tabla 3")
st.write(pd.DataFrame({
    'Cordenada x': [Cdato_1[0], Cdato_2[0], Cdato_3[0], Cdato_4[0],Cdato_5[0],Cdato_6[0]],
    'Cordenada y': [Cdato_1[1], Cdato_2[1], Cdato_3[1], Cdato_4[1],Cdato_5[1],Cdato_6[1]],
    'Distancia de centro': [Cdato_1[2], Cdato_2[2], Cdato_3[2], Cdato_4[2],Cdato_5[2],Cdato_6[2]],
})
)

df3 = pd.DataFrame({'Eje X':[Cdato_1[0], Cdato_2[0], Cdato_3[0], Cdato_4[0],Cdato_5[0],Cdato_6[0]],
                   'Eje Y':[Cdato_1[1], Cdato_2[1], Cdato_3[1], Cdato_4[1],Cdato_5[1],Cdato_6[1]]})
index_ = ['1', '2', '3', '4', '5','6']
st.vega_lite_chart(df3, {
    'mark': {'type': 'circle', 'tooltip': True},
    'encoding': {
        'x': {'field': 'Eje X', 'type': 'quantitative'},
	'y': {'field': 'Eje Y', 'type': 'quantitative'},
    },
}
)






