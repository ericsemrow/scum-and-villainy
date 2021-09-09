import os, json, firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

class Firestore(object):
  db = None

  def __init__(self):
    if not firebase_admin._apps:
      # Use the application default credentials
      cred = credentials.Certificate(json.loads(os.environ.get("FIREBASE_ADMIN_CREDENTIALS")))

      firebase_admin.initialize_app(cred)

    self.db = firestore.client()
  
  
  
