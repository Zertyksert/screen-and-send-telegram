import pyscreenshot
import telebot
import keyboard
API_KEY = ""
chat_id = ''
bot = telebot.TeleBot(API_KEY)


def send_screenshot():
    image = pyscreenshot.grab()
    name = "temp.png"
    image.save(name)
    bot.send_document(chat_id = chat_id, document = open(name, "rb"))

keyboard.add_hotkey('ctrl+shift+a', send_screenshot, args=())





bot.infinity_polling()