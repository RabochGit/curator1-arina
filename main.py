import telebot
bot = telebot.TeleBot('6546016321:AAEZ9LfLwD--LH777WETkKWE8AuZ4d3oQKQ')

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, '*Привет*', parse_mode='Markdown')

@bot.message_handler(commands=['will'])
def main(message):
    bot.send_message(message.chat.id, '*Как дела?*', parse_mode='Markdown')

@bot.message_handler(commands=['home'])
def main(message):
    bot.send_message(message.chat.id, 'ЭТО [ССЫЛКА](gdz.ru)', parse_mode='Markdown')

bot.infinity_polling()