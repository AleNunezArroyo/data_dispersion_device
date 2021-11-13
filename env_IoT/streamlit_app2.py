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

users_ref = db.collection(u'Informacion')
docs = users_ref.stream()
koo=[]
for doc in docs:
	ko=(f'{doc.id}')
	koo.append(ko)
jk=len (koo)

print(koo)

	
st.sidebar.markdown("# Seleccion de Laboratorio")
select_event = st.sidebar.selectbox('Laboratorio',koo)
for l in range(jk):
	if select_event == koo[l]:
		coleccion=koo[l]
	



# -- Default detector list
#detectorlist = ['Laboratorio 3 2-11-2021','Laboratorio 3 2-11-2021', 'Laboratorio 3 2-11-2021']

posts_ref2  = db.collection(coleccion).where(u'tabla', u'==', "tabla1")
docs = posts_ref2.stream()
for doc in docs:
	post = doc.to_dict()
po=len(post)

posts_ref3  = db.collection(coleccion).where(u'tabla', u'==', "tabla2")
docs = posts_ref3.stream()
for doc in docs:
	post2 = doc.to_dict()
po2=len(post2)

posts_ref4  = db.collection(coleccion).where(u'tabla', u'==', "tabla3")
docs = posts_ref4.stream()
for doc in docs:
	post3 = doc.to_dict()
po3=len(post3)


posts_ref  = db.collection(coleccion).where(u'tabla', u'==', "tabla1")
n=1
Adato_nn= ['44', '44', '44']
for doc in posts_ref.stream():
	for i in range(po-1):
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

n2=1
Adato_nn2= ['44', '44', '44']
for doc in posts_ref.stream():
	for i in range(po2-1):
		post = doc.to_dict()
		DAT=("dato"+(str(n2)))
		DOT=(''+DAT+'')
		DUT=("Bdato_"+(str(n2)))
		DUT = post[DOT]
		#dic3 = (Adato_nn | DUT)
		Adato_nn2=Adato_nn2+DUT
		#Adato_nn.update(DUT)
		#print ('"'+DAT+'"')
		n2=n2+1
#print(DUT)
Adato_nn2.remove('44')
Adato_nn2.remove('44')
Adato_nn2.remove('44')

posts_ref  = db.collection(coleccion).where(u'tabla', u'==', "tabla3")
n3=1
Adato_nn3= ['44', '44', '44']
for doc in posts_ref.stream():
	for i in range(po3-1):
		post = doc.to_dict()
		DAT=("dato"+(str(n3)))
		DOT=(''+DAT+'')
		DUT=("Cdato_"+(str(n3)))
		DUT = post[DOT]
		#print(DUT)

		#dic3 = (Adato_nn | DUT)
		Adato_nn3=Adato_nn3+DUT
		#Adato_nn.update(DUT)
		#print ('"'+DAT+'"')
		n3=n3+1
#print(DUT)
Adato_nn3.remove('44')
Adato_nn3.remove('44')
Adato_nn3.remove('44')


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

df1 = pd.DataFrame({'Eje X':Corden1,
                   'Eje Y':Corden2})
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
a=0
b=1
c=2
sep=0
lenin=(len(Adato_nn2)/3)
lenin2=int(float(lenin))
print(lenin)

Corden1=[]
Corden2=[]
Corden3=[]
conti=[]
for j in range(lenin2):
	print(a)
	Cord1 = Adato_nn2[a]
	co1=float(Cord1)
	Corden1.append(co1)
	print(Corden1)
	Cord2 = Adato_nn2[b]
	co2=float(Cord2)
	Corden2.append(co2)
	Cord3 = Adato_nn2[c]
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

df1 = pd.DataFrame({'Eje X':Corden1,
                   'Eje Y':Corden2})
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

st.write("Tabla 3")
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
	Cord1 = Adato_nn3[a]
	co1=float(Cord1)
	Corden1.append(co1)
	print(Corden1)
	Cord2 = Adato_nn3[b]
	co2=float(Cord2)
	Corden2.append(co2)
	Cord3 = Adato_nn3[c]
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

df1 = pd.DataFrame({'Eje X':Corden1,
                   'Eje Y':Corden2})
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





