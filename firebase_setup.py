import os
import json
from firebase_admin import credentials, initialize_app, db


def initialize_firebase():
    # 从环境变量中读取凭证 JSON 字符串
    cred_json = os.getenv('FIREBASE_CREDENTIALS_JSON')
    if cred_json is None:
        raise ValueError("Firebase credentials not set in environment variables")

    # 将凭证 JSON 字符串转换为字典
    cred_dict = json.loads(cred_json)

    # 从环境变量获取数据库 URL
    database_url = os.getenv('FIREBASE_DATABASE_URL')
    if database_url is None:
        raise ValueError("Firebase database URL not set in environment variables")

    # 使用凭证和数据库 URL 初始化 Firebase
    cred = credentials.Certificate(cred_dict)
    app = initialize_app(cred, {
        'databaseURL': database_url
    })

    # 你现在可以使用 app 进行其他操作，例如访问数据库等
    # 示例：db.reference('some/path').get()







