from TicTacToe.Board import Board


class Session:
  def __init__(self, board_size, player1_symbol, player2_symbol, bot, message):
    self.board_size = board_size
    self.bot = bot
    self.message = message
    self.board = Board(board_size, bot, message)
    self.player1_symbol = player1_symbol
    self.player2_symbol = player2_symbol
    self.current_player = player1_symbol

  def start_game(self, message):
    while not self.check_game_over():
      self.board.print_board(message)
      self.bot.send_message(message.chat.id, f"Player {self.current_player}, enter your move (row and column, separated by space): ")
      self.make_move(message)
      self.switch_player()

    self.board.print_board()
    self.bot.send_message(self.message.chat.id, f"Player {self.current_player} wins!")

  def make_move(self, message):
    while True:
        lst = list(map(int, message.text.split()))
        row = lst[0], col = lst[1]
        if not self.board.is_valid_move(row, col):
            self.bot.send_message(message.chat.id, "Invalid move. Try again.")
            continue

        self.board.make_move(row, col, self.current_player)
        break

  def switch_player(self):
    self.current_player = self.player2_symbol if self.current_player == self.player1_symbol else self.player1_symbol

  def check_game_over(self):
    if self.board.check_winner(self.player1_symbol) or self.board.check_winner(self.player2_symbol):
      return True

    for i in range(self.board_size):
      for j in range(self.board_size):
        if self.board.is_valid_move(i, j):
          return False

    self.bot.send_message(self.message.chat.id, "It's a tie!")
    return True
