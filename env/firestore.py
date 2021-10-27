import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import datetime
# Use a service account
cred = credentials.Certificate('serviceAccountKey.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

db.collection('ID').add({'name':'Ale', "age":13})

# Create an initial document to update
frank_ref = db.collection(u'users').document(u'10410426')
frank_ref.set({
    u'name': u'Alejandro Núñez Arroyo',
    u'favorites': {
        u'food': u'Pizza',
        u'dateExample': datetime.datetime.now(),
        u'x_coordinate': [5.2, 3, 12.1],
        u'y_coordinate': [5.2, 3, 12.1],
    },
    u'age': 12
})

# Update age and favorite color
frank_ref.update({
    u'age': 13,
    u'favorites.color': u'Red'
})