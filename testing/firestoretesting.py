import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials
import json
from datetime import *
import datetime
import os

today = date.today()
time = datetime.datetime.now()

day_file_name = f'{today.year}-{today.month}-{today.day}'

cred = credentials.Certificate('mass-academy-sign-in-system-60c92728ae76.json')
app = firebase_admin.initialize_app(cred)
db = firestore.client()

#get the day document on firestore
doc_ref = db.collection('test').document(day_file_name)
doc = doc_ref.get()

#input name
if doc.exists:
    print("Exists")
    doc = doc.to_dict()
    name = input().strip()
    if name in doc:
        if len(doc[name]) in (0, 1):
            doc[name].append(f'{time.hour}:{time.minute}')
            print("Signed in!")
        else:
            doc[name][1] = f'{time.hour}:{time.minute}'
            print("Signed out!")
    else:
        print('Not valid name!')
    doc_ref.set(doc)
else:
    # create document
    id_file = open("ids.json", "r")
    id_file_contents = json.load(id_file)
    names = []
    for id in id_file_contents:
        names.append(id_file_contents[id])
    names.sort()
    day = {}
    for name in names:
        day[name]=[]
    db.collection(u'test').document(day_file_name).set(day)