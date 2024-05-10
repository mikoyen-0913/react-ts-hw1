import os
import json
from firebase_admin import credentials, initialize_app


def initialize_firebase():
    # 从环境变量中读取凭证 JSON 字符串
    cred_json = os.getenv('FIREBASE_CREDENTIALS_JSON')
    if cred_json is None:
        raise ValueError("Firebase credentials not set in environment variables")

    # 将凭证 JSON 字符串转换为字典
    cred_dict = json.loads(cred_json)

    # 使用凭证初始化 Firebase
    cred = credentials.Certificate(cred_dict)
    initialize_app(cred)






