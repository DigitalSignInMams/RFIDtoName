import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials

cred = credentials.Certificate('mass-academy-sign-in-system-60c92728ae76.json')
app = firebase_admin.initialize_app(cred)
db = firestore.client()

doc_ref = db.collection('test').document('tarunisfucking hot')
doc_ref.set({
    u'first': u'Ada',
    u'last': u'Lovelace',
    u'born': 1815
})