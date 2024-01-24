import telebot
from telebot import types

from TicTacToe.TttMenu import TttMenu

bot = telebot.TeleBot('6738924321:AAEMBZ8ajv3aj6r2whweA4o7vk5bN-qEt5k')
tic_tac_tie_game = TttMenu(bot)

@bot.message_handler(commands=['start'])
def handle_start(message):
  markup = types.InlineKeyboardMarkup()
  btn1 = types.InlineKeyboardButton('Tic Tac Toe', callback_data='help')
  markup.row(btn1)
  bot.send_message(message.chat.id, "Hi! I'm <em><b>GameBot!</b></em>", parse_mode='HTML')
  bot.send_message(message.chat.id, "<u>Select the game you want to play today:</u>", parse_mode='HTML', reply_markup=markup)

@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'help':
        bot.send_message(callback.from_user.id, "И чтобы начать играть, вы слово /jumanji должны прокричать!")
    else:
        tic_tac_tie_game.callback_message(callback)

@bot.message_handler(commands=['help'])
def handle_help(message):
  bot.send_message(message.from_user.id, "И чтобы начать играть, вы слово /jumanji должны прокричать!")

@bot.message_handler(commands=['jumanji'])
def handle_jumanji(message):
  tic_tac_tie_game.start_ttt_game(message)

bot.polling(none_stop=True, interval=0)
