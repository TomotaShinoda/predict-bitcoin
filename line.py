from linebot import LineBotApi
from linebot.models import TextSendMessage
from assets.database import db_session
from assets.models import Data

# LINE BOTを作成する
# チャンネルアクセストークンを指定しBOTを作成
CHANNEL_ACCESS_TOKEN = "Sg+stNUrfwuTCC4XxsoXsEAzc2gIFkNdxTQcyhVC0pmHiqCU2at/kaXtXBa2WY5FC3dpjeAUu9HWFbFGHMwkSJqWDCBT/KJRUt0Q3LwAao3KyZgXiCQGU7diJkCUdz2ytUo9OixDmKk/f3MByR8ufQdB04t89/1O/w1cDnyilFU="
line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)

# メッセージを送信する関数を作成
def push():
    # DBから必要なデータを取得
    today = db_session.query(Data).all()[-2].date
    nextday = db_session.query(Data).all()[-1].date
    price_today = db_session.query(Data).all()[-2].real_price
    price_nextday = db_session.query(Data).all()[-1].pred_price

    # 送信するメッセージを記述
    text = (
        "おはようございます！🌅 \n本日のビットコイン相場予測配信です！💹\n\n"
        f"{today.strftime('%Y-%m-%d %H:%M')}の実際相場\n"
        f"￥{price_today} (BTC/JPY)\n\n"
        f"{nextday.strftime('%Y-%m-%d %H:%M')}の予測相場\n"
        f"￥{price_nextday} (BTC/JPY)\n\n"
        "アプリケーションのURL \n"
        "https://predict-bitcoin.herokuapp.com/"
    )       
    messages = TextSendMessage(text=text)

    # アカウントを追加している全ユーザーにメッセージを送信
    line_bot_api.broadcast(messages=messages)
    
# メインで実行される関数
if __name__ == "__main__":
    push()