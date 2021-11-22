import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import datetime
from datetime import timezone
# Use a service account
cred = credentials.Certificate('/home/ale/Downloads/datadispersiondevice-b2e58-firebase-adminsdk-w33zc-b52a8406e5.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

date = '2019-07-17'
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
            'x_coordinate': 3.1,
            'y_coordinate': 5.1,
            'distance_setpoint': 5.1,
        },
    },
    '2': {
        'data1': {
            'dateExample': datetime.datetime.now(timezone.utc),
            'x_coordinate': 3.1,
            'y_coordinate': 5.1,
            'distance_setpoint': 5.1,
        },
        'data2': {
            'dateExample': datetime.datetime.now(timezone.utc),
            'x_coordinate': 3.1,
            'y_coordinate': 5.1,
            'distance_setpoint': 5.1,
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
