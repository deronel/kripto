import requests
from datetime import datetime
import telebot
from auth_data import token


def get_data():
    req = requests.get("https://yobit.net/api/3/ticker/btc_usd")
    response = req.json()
    sell_priсe = response["btc_usd"]["sell"]
    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nSell BTC priсe: {sell_priсe}")


def telegram_bot(token):
    bot = telebot.TeleBot(token)
    
    @bot.message_handler(commands=["start"])
    def start_message(massage):
        bot.send_message(massage.chat.id, "Hello friend! Write the 'priсe' to find out")

    @bot.message_handler(content_types=["text"])
    def send_text (message):
        if message.text.lower() == "price":
            try:
                req = requests.get("https://yobit.net/api/3/ticker/btc_usd")
                response = req.json()
                sell_price = response["btc_usd"]["sell"]
                bot.send_message(
                    message.chat.id,
                    f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nSell BTC priсe: {sell_price}"
                )
            except Exception as ex:
                print(ex)
                bot.send_message(
                    message.chat.id,
                    "Что то пошло не так"
                )
        else:
            bot.send_message(message.chat.id, "Уточните  какую комманду нужно выбрать")
    
    bot.polling()    


if __name__ == '__main__':
    # get_data()
    telegram_bot(token)