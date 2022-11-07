import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials

def initialize_student_info():
    cred = credentials.Certificate('mass-academy-sign-in-system-60c92728ae76.json')
    app = firebase_admin.initialize_app(cred)
    db = firestore.client()

    doc = json.load(open('students.json', 'r'))
    db.collection('student_info').document('students').set(doc)
