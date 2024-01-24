class Board:
  def __init__(self, board_size, bot, message):
    self.size = board_size
    self.bot = bot
    self.message = message
    self.board = [[' ' for _ in range(self.size)] for _ in range(self.size)]
    self.initialize_board()

  def initialize_board(self):
    for i in range(self.size):
      for j in range(self.size):
        self.board[i][j] = ' '

  def print_board(self, message):
    self.bot.send_message(message.chat.id, "Current Board:")
    for i in range(self.size):
      for j in range(self.size):
        self.bot.send_message(message.chat.id, self.board[i][j])
      self.bot.send_message(message.chat.id, '\n')

  def is_valid_move(self, row, col):
    return 0 <= row < self.size and 0 <= col < self.size and self.board[row][col] == ' '

  def make_move(self, row, col, player_symbol):
    self.board[row][col] = player_symbol

  def check_winner(self, player_symbol):
    for i in range(self.size):
      if self.check_row(i, player_symbol) or self.check_column(i, player_symbol):
        return True
    return self.check_diagonals(player_symbol)

  def check_row(self, row, player_symbol):
    for i in range(self.size):
      if self.board[row][i] != player_symbol:
        return False
    return True

  def check_column(self, col, player_symbol):
    for i in range(self.size):
      if self.board[i][col] != player_symbol:
        return False
    return True

  def check_diagonals(self, player_symbol):
    left_diagonal = all(self.board[i][i] == player_symbol for i in range(self.size))
    right_diagonal = all(self.board[i][self.size - 1 - i] == player_symbol for i in range(self.size))
    return left_diagonal or right_diagonal
