from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('XqsT5l6v1mrJJnFYmN+GgHhunvcjzcjAWbcBUPEuvwHT3UuDA2q9j0TtAv+FjzuQVOCx5R37Pgp3OnUW+F/+1C8o8C4WfofSjLUXPqmeax3x7Ny3/dsvXJzQ1HUhaBFeWscMMsGnpcw/7sWPiq6ihQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('7f7df77fc20331b72236e36c79f09af2')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        msg = event.message.text
        if msg == '你好':
            remsg = '今天天氣真好啊'
        else:
            remsg = '你很煩'
        event.reply_token,
        TextSendMessage(text=remsg)) # 回復使用者傳來的訊息  就回傳什麼


if __name__ == "__main__":
    app.run()
