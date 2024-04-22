import telebot
from telebot import types
from googletrans import Translator
from langdetect import detect


bot = telebot.TeleBot('6733673868:AAGpJrHb7mjM5ug-b-QtPlKTMMec5lypNm8')


@bot.message_handler(commands=['start'])
def main(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton('ENGLISH', callback_data='question1')
    item2 = types.InlineKeyboardButton('italian', callback_data='question2')
    buttons = types.InlineKeyboardButton('<-', callback_data='None')
    markup.add(item1, item2)
    bot.send_message(message.chat.id, f'Привет, Какой язык ты хочешь выбрать? {message.from_user.first_name} {message.from_user.last_name}', reply_markup=markup)


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, '<b>help</b>', parse_mode='html')


translator = Translator()


# Определяем функцию для обработки сообщений
@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    if call.message:
        if call.data == 'question1':
            bot.send_message(call.message.chat.id, 'Вы выбрали English')
        if call.data == 'question2':
            bot.send_message(call.message.chat.id, 'Вы выбрали Italian')




bot.polling(none_stop=True)