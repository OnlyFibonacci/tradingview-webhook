from flask import Flask, request
import json
import telebot
from binance.spot import Spot as Client



app = Flask(__name__)




@app.route("/webhook", methods=['POST'])
def webhook():

    try:
        data = json.loads(request.data)
        ticker = data['ticker']
        exchange = data['exchange']
        price = data['price']
        side = data['side']
        quantity = data['quantity']
        telegramBotApi = data['telegramBotApi']
        telegramUserId = data['telegramUserId']
        binanceApiKey = data['binanceApiKey']
        binanceSecretKey = data['binanceSecretKey']
        params = {
            "symbol": ticker,
            "side": side,
            "type": "MARKET",
            "quantity": quantity,
        }
        Client(binanceApiKey, binanceSecretKey).new_order(**params)
        telebot.TeleBot(telegramBotApi).send_message(telegramUserId,
                                                     f"{ticker} {side}ING on {exchange} \nQuantity : {quantity} ")
    except:
        pass
    return {
        "code": "success",



    }










