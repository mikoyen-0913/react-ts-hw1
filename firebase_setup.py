import os
from dotenv import load_dotenv
import firebase_admin
from firebase_admin import credentials, initialize_app

# 加載 .env 文件中的環境變量
load_dotenv()

def initialize_firebase():
    # 從環境變量獲取 Firebase 證書路徑，如果環境變量未設置，使用預設路徑
    cred_path = os.getenv('FIREBASE_CREDENTIALS', 'E:/pythoncode/FirebaseProject/secrets/foodparty-3c57b-firebase-adminsdk-otkb9-28ce32b1c9.json')
    database_url = os.getenv('FIREBASE_DATABASE_URL', 'https://foodparty-3c57b-default-rtdb.firebaseio.com/')

    # 初始化 Firebase 應用
    cred = credentials.Certificate(cred_path)
    firebase_admin.initialize_app(cred, {
        'databaseURL': database_url
    })




