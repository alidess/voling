import telebot

bot = telebot.TeleBot("594854573:AAHXuBfCIJ-hoiEjF__nvbaMUZqc2BehMOs")


@bot.message_handler(commands=["start"])
def send_welcome(message):

    bot.send_message(message.chat.id, "hello")


bot.polling()
