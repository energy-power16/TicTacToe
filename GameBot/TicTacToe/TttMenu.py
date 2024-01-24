from telebot import types
from TicTacToe.Session import Session
class TttMenu:
  def __init__(self, bot):
    self.bot = bot

  def start_ttt_game(self, message):
    self.bot.send_message(message.chat.id, "Welcome to Tic-Tac-Toe!")
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('3x3', callback_data='3'))
    btn1 = types.InlineKeyboardButton('4x4', callback_data='4')
    btn2 = types.InlineKeyboardButton('5x5', callback_data='5')
    markup.row(btn1, btn2)
    self.bot.send_message(message.chat.id, "<b>Enter the size of the board: </b>", parse_mode='HTML', reply_markup=markup)

  def callback_message(self, callback):
    if callback.data == '3':
      self.bot.send_message(callback.from_user.id, "3")
    elif callback.data == '4':
      self.bot.send_message(callback.from_user.id, "4")
    elif callback.data == '5':
      self.bot.send_message(callback.from_user.id, "5")

    # Todo: Необходимо реализовать отображение поля после каждого хода и передавать в метод номер клетки и менять символ
    # Todo: Все последующие строки кода, а также сами файлы игрры требуют доработки

  def choose_board_size(self, message):
    global board_size
    board_size = int(message.text)
    self.bot.send_message(message.chat.id, "Enter player 1 symbol: ")
    self.bot.register_next_step_handler(message, self.choose_player1_symbol)

  def choose_player1_symbol(self, message):
    global player1_symbol
    player1_symbol = message.text[0]
    self.bot.send_message(message.chat.id, "Enter player 2 symbol: ")
    self.bot.register_next_step_handler(message, self.choose_player2_symbol)

  def choose_player2_symbol(self, message):
    player2_symbol = message.text[0]
    tic_tac_toe_session = Session(board_size, player1_symbol, player2_symbol, self.bot, message)
    tic_tac_toe_session.start_game(message)

