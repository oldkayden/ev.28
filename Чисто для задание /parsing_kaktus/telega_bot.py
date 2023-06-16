import json
import telebot
from telebot import types
from pars import pars_news

token = '6080430388:AAG_RR_CTHa3aS3w30QHUt5mCQ12UkAo2Ek'
bot = telebot.TeleBot(token)

Keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = types.KeyboardButton('Foto')
btn2 = types.KeyboardButton('Description')
Keyboard.add(btn1, btn2)

def read_news():
    with open('data.json') as file:
        data = json.load(file)
    return data

@bot.message_handler(commands=['start'])
def start_parse(message):
    print('!!!!!')
    bot.send_message(message.chat.id, 'Hello, we started to parse some articles! Pls wait a few seconds...')
    print('started')
    pars_news()
    print('parsed')
    data = read_news()
    for x in data:
        print(x)
        bot.send_message(message.chat.id, f'{x} --> *{data[x]["title"]}*', parse_mode='Markdown')
    
    bot_message = bot.send_message(message.chat.id, 'Choice number of article for detail info(1-20): ')
    bot.register_next_step_handler(bot_message, check_number)

def check_number(message):
    nums = [str(x) for x in range(1,21)]
    if message.text not in nums:
        print(message.text)
        bot_message = bot.send_message(message.chat.id, 'Invalid number! You must choose number in range from 1 to 20:')
        bot.register_next_step_handler(bot_message, check_number)
    else:
        data = read_news()
        bot_message = bot.send_message(message.chat.id, f'{data[message.text]["title"]}\nYou caan see Description of this news and Photo', reply_markup=Keyboard)
        bot.register_next_step_handler(bot_message, show_info, message.text, data)

def show_info(message, number, data):
    if message.text.lower() == 'foto':
        bot.send_message(message.chat.id, data[number]['img'])
        bot_message = bot.send_message(message.chat.id, 'Choice number of article for detail info(1-20): ')
        bot.register_next_step_handler(bot_message, check_number)
    else:
        bot.send_message(message.chat.id, data[number]['desc'])
        bot_message = bot.send_message(message.chat.id, 'Choice number of article for detail info(1-20): ')
        bot.register_next_step_handler(bot_message, check_number)

bot.polling()






