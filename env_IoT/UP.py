import streamlit as st
from google.cloud import firestore
import datetime
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from datetime import timezone
import threading
from time import sleep
import numpy as np
import pandas as pd
# With:
import json

#key_dict = json.loads(st.secrets["textkey"])
keyfile_data = json.loads(st.secrets["textkey"])

db = firestore.Client.from_service_account_json("firestore-key.json")
#Documento

class City(object):
    def __init__(self,tabla, dato1=[], dato2=[], dato3=[], dato4=[], dato5=[],
                 dato6=[]):
        self.tabla = tabla
        self.dato1 = dato1
        self.dato2 = dato2
        self.dato3 = dato3
        self.dato4 = dato4
        self.dato5 = dato5
        self.dato6 = dato6

    @staticmethod
    def from_dict(source):
        # [START_EXCLUDE]
        city = City(source[u'tabla1'])
        if u'dato1' in source:
            city.dato1 = source[u'dato1']
        if u'dato2' in source:
            city.dato2 = source[u'dato2']
        if u'dato3' in source:
            city.dato3 = source[u'dato3']
        if u'dato4' in source:
            city.dato4 = source[u'dato4']
        if u'dato5' in source:
            city.dato5 = source[u'dato5']
        if u'dato6' in source:
            city.dato6 = source[u'dato6']

        return city
        # [END_EXCLUDE]

    def to_dict(self):
        # [START_EXCLUDE]
        dest = {
	    u'tabla': self.tabla,
            u'dato1': self.dato1,
            u'dato2': self.dato2,
            u'dato3': self.dato3,
            u'dato4': self.dato4,
            u'dato5': self.dato5,
            u'dato6': self.dato6,
            #u'state': self.state,
           #u'country': self.country
        }      
        if self.dato1:
            dest[u'dato1'] = self.dato1

        if self.dato2:
            dest[u'dato2'] = self.dato2

        if self.dato3:
            dest[u'dato3'] = self.dato3

        if self.dato4:
            dest[u'dato4'] = self.dato4

        if self.dato5:
            dest[u'dato5'] = self.dato5

        if self.dato6:
            dest[u'dato6'] = self.dato6

        return dest
        # [END_EXCLUDE]

    def __repr__(self):
        return(
            f'City(\
                tabla={self.tabla}, \
                dato1={self.dato1}, \
                dato2={self.dato2}, \
                dato3={self.dato3}, \
                dato4={self.dato4}, \
                dato5={self.dato5}, \
                dato6={self.dato6},\
            )'
        )

cities_ref = db.collection(u'Laboratorio 3 2-11-2021')
cities_ref.document(u'Tabla 1').set(
    City(u'tabla1',[u'7.5',u'4',u'3.5'],[u'7.6',u'4.1',u'3.2'],[u'7.3',u'4',u'3.6'],[u'3.4',u'4.1',u'3.2'],[u'3.3',u'4',u'3.6'],[u'3.6',u'4.2',u'7.7']).to_dict())
cities_ref.document(u'Tabla 2').set(
    City(u'tabla2', [u'2.5',u'4',u'3.5'],[u'2.6',u'4.1',u'3.6'],[u'2.3',u'4',u'3.6'],[u'2.4',u'4.1',u'3.4'],[u'7.3',u'4',u'3.6'],[u'7.6',u'4.2',u'3.8']).to_dict())

cities_ref.document(u'Tabla 3').set(
    City(u'tabla3', [u'7.5',u'4',u'3.5'],[u'7.6',u'4.1',u'3.4'],[u'7.3',u'4.3',u'3.6'],[u'2.4',u'4.2',u'3.4'],[u'2.3',u'7.2',u'3.6'],[u'7.6',u'4.2',u'3.6']).to_dict())

