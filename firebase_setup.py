import firebase_admin
from firebase_admin import credentials, db

# 設定 Firebase 密鑰和數據庫 URL
# firebase_setup.py

import firebase_admin
from firebase_admin import credentials, db

def initialize_firebase():
    cred = credentials.Certificate('C:/Users/Su family/Downloads/foodparty-3c57b-firebase-adminsdk-otkb9-28ce32b1c9.json')
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://foodparty-3c57b-default-rtdb.firebaseio.com/'
    })

