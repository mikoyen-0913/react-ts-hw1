import sys
import firebase_admin
from firebase_admin import credentials, db
from flask import Flask, request, abort

from linebot.v3 import WebhookHandler
from linebot.v3.messaging import Configuration, ApiClient, MessagingApi, ReplyMessageRequest
from linebot.v3.messaging.models import TextMessage
from linebot.v3.exceptions import InvalidSignatureError
from linebot.v3.webhooks import MessageEvent, TextMessageContent

print("Python 版本:", sys.version)
print("系統路徑:", sys.path)

from firebase_setup import initialize_firebase

app = Flask(__name__)

initialize_firebase()

# 使用固定的访问令牌和密钥
configuration = Configuration(access_token='7biRawnBMOp3JyWIGzD871MVN2ybSYqZ41Dbhr1e8JBq4z6r0w4RNAEfApWRwdWjoSJliOdPThve2hgX2OK3PWOM48Grs9F4rCT7Hvd0IU3eQKsJ3CW/K5qYXOuCw9Rj2q9oEGEpWnC2c9wzz60SaAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('8057f2e5cc3db80ebc636a3c235d12c7')

@app.route('/')
def home():
    return "歡迎來到 Line Bot Webhook 接收器"

@app.route('/favicon.ico')
def favicon():
    return '', 204

@app.route("/callback", methods=['POST'])
def callback():
    簽名 = request.headers['X-Line-Signature']
    請求內容 = request.get_data(as_text=True)

    try:
        handler.handle(請求內容, 簽名)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@handler.add(MessageEvent, message=TextMessageContent)
def handle_message(event):
    with ApiClient(configuration) as api_client:
        line_bot_api = MessagingApi(api_client)
        user_id = event.source.user_id  # 獲取發送訊息的用戶 ID
        text = event.message.text
        args = text.split()
        command = args[0].lower()

        if command == 'add':
            restaurants = args[1:]
            for restaurant in restaurants:
                db.reference(f"users/{user_id}/restaurants/{restaurant}").set(True)
            response_text = f"已添加餐廳: {', '.join(restaurants)}"
        elif command == 'remove':
            restaurants = args[1:]
            for restaurant in restaurants:
                db.reference(f"users/{user_id}/restaurants/{restaurant}").delete()
            response_text = f"已移除餐廳: {', '.join(restaurants)}"
        elif command == 'get':
            restaurants_ref = db.reference(f"users/{user_id}/restaurants")
            restaurants = restaurants_ref.get() or {}
            response_text = f"您的餐廳列表: {', '.join(restaurants.keys())}"
        elif command == 'search':
            search_query = args[1]
            restaurants_ref = db.reference(f"users/{user_id}/restaurants")
            all_restaurants = restaurants_ref.get() or {}
            matched_restaurants = {name: True for name in all_restaurants if
                                   search_query in name}
            response_text = f"搜尋結果: {', '.join(matched_restaurants.keys())}"

        line_bot_api.reply_message_with_http_info(
            ReplyMessageRequest(
                reply_token=event.reply_token,
                messages=[TextMessage(text=response_text)]
            )
        )

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

