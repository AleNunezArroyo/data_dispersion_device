import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import datetime
from datetime import timezone
# Use a service account
cred = credentials.Certificate('/home/ale/Downloads/firestore-key.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

date = '2020-07-17'
genero = 'Masculino'
id = '10410425'
number = '1'
table = '1'
# Create an initial document to update
frank_ref = db.collection('laboratory').document(date)
frank_ref.set({
    number: {
        'data1': {
            'dateExample': datetime.datetime.now(timezone.utc),
            'x_coordinate': 1.1,
            'y_coordinate': 1.1,
            'distance_setpoint': 1.1,
        },
        'data2': {
            'dateExample': datetime.datetime.now(timezone.utc),
            'x_coordinate': 2.1,
            'y_coordinate': 2.2,
            'distance_setpoint': 2.3,
        },
        'data3': {
            'dateExample': datetime.datetime.now(timezone.utc),
            'x_coordinate': 3.1,
            'y_coordinate': 3.2,
            'distance_setpoint': 3.3,
        },
        'data4': {
            'dateExample': datetime.datetime.now(timezone.utc),
            'x_coordinate': 4.1,
            'y_coordinate': 4.2,
            'distance_setpoint': 4.3,
        },
    },
    '2': {
        'data1': {
            'dateExample': datetime.datetime.now(timezone.utc),
            'x_coordinate': 1.1,
            'y_coordinate': 1.2,
            'distance_setpoint': 1.3,
        },
        'data2': {
            'dateExample': datetime.datetime.now(timezone.utc),
            'x_coordinate': 2.1,
            'y_coordinate': 2.2,
            'distance_setpoint': 2.3,
        },
        'data3': {
            'dateExample': datetime.datetime.now(timezone.utc),
            'x_coordinate': 3.1,
            'y_coordinate': 3.2,
            'distance_setpoint': 3.3,
        },
        'data4': {
            'dateExample': datetime.datetime.now(timezone.utc),
            'x_coordinate': 4.1,
            'y_coordinate': 4.2,
            'distance_setpoint': 4.3,
        },
    },
})
# Add more value of attempt
# frank_ref.set({
#     'group': {
#         'group 1': {
#             'data6': {
#                 'dateExample': datetime.datetime.now(timezone.utc),
#                 'x_coordinate': 3.1,
#                 'y_coordinate': 5.1,
#                 'distance_setpoint': 5.1,
#             },
#         },
#     },
# }, merge=True)
