import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials
import json

def initialize_student_info(cred, app, db):
    doc = json.load(open('students.json', 'r'))
    db.collection('student_info').document('students').set(doc)
    db.close()

