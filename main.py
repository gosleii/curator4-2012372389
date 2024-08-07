import telebot

bot = telebot.TeleBot("7312344398:AAGag83XVQ6guClkR32XhwK-pKie885djgE")

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'здарвствуйте что бы открыть вики напишите /wiki', parse_mode='Markdown')

@bot.message_handler(commands=['wki'])
def main(message):
    bot.send_message(message.chat.id, 'https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0', parse_mode='Markdown')

bot.infinity_polling()