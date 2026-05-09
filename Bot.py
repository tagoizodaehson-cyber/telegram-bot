import telebot
import os
from flask import Flask
from threading import Thread

TOKEN = os.environ.get('BOT_TOKEN') 
bot = telebot.TeleBot(TOKEN)

app = Flask('')
@app.route('/')
def home():
    return "Bot is alive!"

def run():
  app.run(host='0.0.0.0',port=8080)

Thread(target=run).start()

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Салом Эҳсончон! Бот дар Render кор мекунад ✅")

bot.polling(non_stop=True)
