import telebot
from telebot import types

from config import TOKEN

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message: types.Message):
    bot.send_message(message.chat.id, 'Hey! to see information about your profile type /info')


@bot.message_handler(commands=['info'])
def info(message: types.Message):
    first = message.from_user.first_name
    full = message.from_user.full_name
    nick = message.from_user.username
    idd = message.from_user.id
    lang = message.from_user.language_code

    bot.send_message(message.chat.id, 'Your data:')
    bot.send_message(message.chat.id,
                     f'id - {idd}, \nnick - {nick}, \nfirstname - {first}, \nfullname - {full}, \nregion - {lang}')


if __name__ == '__main__':
    bot.polling(none_stop=True)
