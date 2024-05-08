import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth

# 初始化 Firebase Admin
cred = credentials.Certificate('C:/Users/Su family/Downloads/foodparty-3c57b-firebase-adminsdk-otkb9-28ce32b1c9.json')
firebase_admin.initialize_app(cred)


# 生成自定義令牌
def generate_custom_token(user_id):
    try:
        custom_token = auth.create_custom_token(user_id)
        print('Token:', custom_token)
    except Exception as e:
        print('Error creating custom token:', e)


# 替換 'your-user-id' 為你的 Line Bot 的使用者標識符
generate_custom_token('Uc962490416f861403f5088071feeb3ac')
