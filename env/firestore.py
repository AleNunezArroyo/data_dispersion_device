import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import datetime
from datetime import timezone
# Use a service account
cred = credentials.Certificate('/home/ale/Downloads/datadispersiondevice-b2e58-firebase-adminsdk-w33zc-b52a8406e5.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

nombre = 'valdi nunes'
genero = 'Masculino'
id = '10410425'
# Create an initial document to update
frank_ref = db.collection('users').document(id)
frank_ref.set({
    'name': nombre,
    'group': {
        'group 1': {
            'attempt 1': {
                'dateExample': datetime.datetime.now(timezone.utc),
                'x_coordinate': 3.1,
                'y_coordinate': 5.1,
                'distance_setpoint': 5.1,
            },
            'attempt 2': {
                'dateExample': datetime.datetime.now(timezone.utc),
                'x_coordinate': 3.1,
                'y_coordinate': 5.1,
                'distance_setpoint': 5.1,
            },
            'attempt 3': {
                'dateExample': datetime.datetime.now(timezone.utc),
                'x_coordinate': 3.1,
                'y_coordinate': 5.1,
                'distance_setpoint': 5.1,
            },
        },
        'group 2': {
            'attempt 1': {
                'dateExample': datetime.datetime.now(timezone.utc),
                'x_coordinate': 3.1,
                'y_coordinate': 5.1,
                'distance_setpoint': 5.1,
            },
        },
    },
})
# Add more value of attempt
frank_ref.set({
    'group': {
        'group 1': {
            'attempt 6': {
                'dateExample': datetime.datetime.now(timezone.utc),
                'x_coordinate': 3.1,
                'y_coordinate': 5.1,
                'distance_setpoint': 5.1,
            },
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
