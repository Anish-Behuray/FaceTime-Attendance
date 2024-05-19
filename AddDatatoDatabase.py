import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://face-recognition-3f2a7-default-rtdb.firebaseio.com/"
})



ref = db.reference('Students')

data = {
    "123456":
        {
            "name": "Anish Behuray",
            "major": "Civil",
            "roll_number": '21CE30006',
            "total_attendance": 7,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "13579":
        {
            "name": "Minati Behuray",
            "major": "Everything",
            "roll_number": '21CE30006',
            "total_attendance": 7,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "321654":
        {
            "name": "Murtaza Hassan",
            "major": "Robotics",
            "roll_number": '21CE30006',
            "total_attendance": 7,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    # "654321":
    #     {
    #         "name": "Soumyashree Nayak",
    #         "major": "Mechnics",
    #         "roll_number": '21CE30006',
    #         "total_attendance": 7,
    #         "standing": "G",
    #         "year": 4,
    #         "last_attendance_time": "2022-12-11 00:54:34"
    #     },
    "852741":
        {
            "name": "Emly Blunt",
            "major": "Economics",
            "roll_number": '21CE30006',
            "total_attendance": 12,
            "standing": "B",
            "year": 1,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "963852":
        {
            "name": "Elon Musk",
            "major": "Physics",
            "roll_number": '21CE30006',
            "total_attendance": 7,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        }


}

for key, value in data.items():
    ref.child(key).set(value)