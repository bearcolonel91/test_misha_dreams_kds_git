import telebot

bot = telebot.TeleBot("6412983438:AAEZ8lnPtKC6UpZ9D4_JUgvFApfdg81s2w0")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
  bot.reply_to(message, "Привет, я эхо бот.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
  bot.reply_to(message, message.text)

bot.infinity_polling()
