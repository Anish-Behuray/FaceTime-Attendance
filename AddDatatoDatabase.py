import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': ""
})



ref = db.reference('Students')

data = {
    "id1":
        {
            "name": "",
            "major": "",
            "roll_number": '',
            "total_attendance": ,
        },
    "id2":
        {
            "name": "",
            "major": "",
            "roll_number": '',
            "total_attendance": ,
        }

}

for key, value in data.items():
    ref.child(key).set(value)
