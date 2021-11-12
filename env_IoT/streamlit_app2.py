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

db = firestore.Client.from_service_account_json(".streamlit/firestore-key.json")


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

n=1
Adato_nn= ['44', '44', '44']

for doc in posts_ref.stream():
	for i in range(6):
		post = doc.to_dict()
		DAT=("dato"+(str(n)))
		DOT=(''+DAT+'')
		DUT=("Adato_"+(str(n)))
		DUT = post[DOT]
		#print(DUT)

		#dic3 = (Adato_nn | DUT)
		Adato_nn=Adato_nn+DUT
		#Adato_nn.update(DUT)
		#print ('"'+DAT+'"')
		n=n+1
#print(DUT)
Adato_nn.remove('44')
Adato_nn.remove('44')
Adato_nn.remove('44')
print(Adato_nn)
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
a=0
b=1
c=2
sep=0
lenin=(len(Adato_nn)/3)
lenin2=int(float(lenin))
print(lenin)

Corden1=[]
Corden2=[]
Corden3=[]
conti=[]
for j in range(lenin2):
	print(a)
	Cord1 = Adato_nn[a]
	co1=float(Cord1)
	Corden1.append(co1)
	print(Corden1)
	Cord2 = Adato_nn[b]
	co2=float(Cord2)
	Corden2.append(co2)
	Cord3 = Adato_nn[c]
	co3=float(Cord3)
	Corden3.append(co3)
	conti.append(j+1)
	a=a+3
	b=b+3
	c=c+3
	sep=sep+1
print(conti)
st.write(pd.DataFrame({
    	'Cordenada x': Corden1,
    	'Cordenada y': Corden2,
	'Distancia de centro': Corden3,}))

df1 = pd.DataFrame({'Eje X':[Corden1],
                   'Eje Y':[Corden2]})
index_ = [conti]
print(df1)
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






