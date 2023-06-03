import telebot
import json
from telebot import types
from main import *

token = open('token').read()
bot = telebot.TeleBot(token)
bd = {}

def add_bd(bd):
    with open("bd.json", 'w') as write_file:
        json.dump(bd, write_file)

markups = []
for i in range(len(questions)):
    btns = []
    for j in range(len(questions[i]['varios'])):
        btns.append(types.KeyboardButton(questions[i]['varios'][j]))
    markups.append(types.ReplyKeyboardMarkup(resize_keyboard=True).add(*btns))

@bot.message_handler(commands=['start'])
def start_command(message):
    answers = []
    k = 0
    bot.register_next_step_handler(bot.send_message(message.chat.id, questions[k]['text'], reply_markup=markups[k]), new_text, k, answers)
    print(message)

def new_text(message, k, answers):
    if k == len(questions) - 1:
        answers.append(message.text)
        bd[message.from_user.username] = answers
        add_bd(bd)
        bot.send_message(message.chat.id, f'Вы набрали {scores(answers)} из 16 возможных')
    else:
        answers.append(message.text)
        k += 1
        bot.register_next_step_handler(bot.send_message(message.chat.id, questions[k]['text'], reply_markup=markups[k]),
                                       new_text, k, answers)


bot.infinity_polling()