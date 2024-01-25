from telebot import types
from TicTacToe.Session import Session


class TttMenu:
    def __init__(self, bot):
        self.bot = bot
        self.size = 0
    def start_ttt_game(self, message):
        self.bot.send_message(message.chat.id, "Welcome to Tic-Tac-Toe!")
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('3x3', callback_data='3'))
        btn1 = types.InlineKeyboardButton('4x4', callback_data='4')
        btn2 = types.InlineKeyboardButton('5x5', callback_data='5')
        markup.row(btn1, btn2)
        self.bot.send_message(message.chat.id, "<b>Enter the size of the board: </b>", parse_mode='HTML',
                              reply_markup=markup)

    def callback_message(self, callback):
      call_move = []
      if(callback.data.isdigit()):
        self.size = callback.data
        self.board = [[0] * int(self.size) for _ in range(int(self.size))]
      else:
        call_move = callback.data.split(" ")
        self.board[int(call_move[0]) - 1][int(call_move[1]) - 1] = 1
      board_size = int(self.size)
      markup = self.create_board_markup(board_size)
      self.bot.send_message(callback.from_user.id, "Choose a cell:", reply_markup=markup)

    def create_board_markup(self, size):
      markup = types.InlineKeyboardMarkup()
      for i in range(size):
        row = []
        for j in range(size):
          if(self.board[i][j] == 1):
              cell_text = f'X'  # You can customize this text as needed
              row.append(types.InlineKeyboardButton(cell_text, callback_data=f'{i + 1} {j + 1}'))
          else:
              cell_text = f'{i + 1},{j + 1}'  # You can customize this text as needed
              row.append(types.InlineKeyboardButton(cell_text, callback_data=f'{i + 1} {j + 1}'))
        markup.row(*row)
      return markup

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
