import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import datetime
# Use a service account
cred = credentials.Certificate('/home/ale/Desktop/serviceAccountKey.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

# room_a_ref = db.collection(u'user').document(u'10410426')
# message_ref = room_a_ref.collection(u'1').document(u'message1')
# message_ref.set({
#     u'name': u'Alejandro Núñez Arroyo',
#     u'Intento': {
#         u'dateExample': datetime.datetime.now(),
#         u'x_coordinate': [5.2, 3, 12.1],
#         u'y_coordinate': [5.2, 3, 12.1],
#     },
# })

nombre = 'ale nunes'
genero = 'Masculino'
id = '10410426'
# Create an initial document to update
frank_ref = db.collection('users').document(id)
frank_ref.set({
    
    'name': nombre,
    'gender': genero,
    'group': {
        '1': {
            'food': 'Pizza',
            'color': 'Blue',
            'subject': 'Recess',
            '1': {
                'dateExample': datetime.datetime.now(),
                'x_coordinate': [5.2, 3, 12.1],
                'y_coordinate': [5.2, 3, 12.1],
            },
            '2': {
                'dateExample': datetime.datetime.now(),
                'x_coordinate': [5.2, 3, 12.1],
                'y_coordinate': [5.2, 3, 12.1],
            },
            '3': {
                'dateExample': datetime.datetime.now(),
                'x_coordinate': [5.2, 3, 12.1],
                'y_coordinate': [5.2, 3, 12.1],
            },
        },
        '2': {
            'food': 'Pizza',
            'color': 'Blue',
            'subject': 'Recess',
        },
    },
})

frank_ref.set({
    'group': {
        '3': {
            'food': 'Pizza',
            'color': 'Blue',
            'subject': 'Recess',
        },
    },
}, merge=True)




# attempts1 = 'attempts6'
# # Update age and favorite color
# frank_ref.update({
#     'group.'+attempts1: {
#             'food': 'Pizza',
#             'color': 'Blue',
#             'subject': 'Recess',
#         },
# })
