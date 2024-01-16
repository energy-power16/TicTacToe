using System;
using System.Threading;

namespace Tic_Tac_Toe
{
    class TimedSession : ISession
    {
        private Board board;
        private int boardSize;
        private char currentPlayer;
        private char player1Symbol;
        private char player2Symbol;
        private int player1TimeInSeconds;
        private int player2TimeInSeconds;
        private bool player1Lost;
        private bool player2Lost;

        public TimedSession(int boardSize, char player1Symbol, char player2Symbol, int player1TimeInSeconds, int player2TimeInSeconds)
        {
            this.boardSize = boardSize;
            board = new Board(boardSize);
            this.player1Symbol = player1Symbol;
            this.player2Symbol = player2Symbol;
            this.player1TimeInSeconds = player1TimeInSeconds;
            this.player2TimeInSeconds = player2TimeInSeconds;
            currentPlayer = player1Symbol;
            player1Lost = false;
            player2Lost = false;
        }

        public void StartGame()
        {
            var timer = new Timer(PrintBoardAndTime, null, 0, 5000); // Изменено на 5000 (5 секунд)

            do
            {
                MakeMove();
                SwitchPlayer();
            } while (!CheckGameOver());

            timer.Dispose();
            board.PrintBoard();

            if (player1Lost)
                Console.WriteLine($"Player {player1Symbol} runs out of time. Player {player2Symbol} wins!");
            else if (player2Lost)
                Console.WriteLine($"Player {player2Symbol} runs out of time. Player {player1Symbol} wins!");
            else
                Console.WriteLine($"Player {currentPlayer} wins!");
        }

        private void PrintBoardAndTime(object state)
        {
            Console.Clear();
            board.PrintBoard();

            if (currentPlayer == player1Symbol)
                Console.WriteLine($"Player 1 time left: {player1TimeInSeconds} seconds");
            else
                Console.WriteLine($"Player 2 time left: {player2TimeInSeconds} seconds");

            if (currentPlayer == player1Symbol)
                player1TimeInSeconds -= 5; 
            else
                player2TimeInSeconds -= 5; 

            if (player1TimeInSeconds <= 0 && currentPlayer == player1Symbol)
                player1Lost = true;

            if (player2TimeInSeconds <= 0 && currentPlayer == player2Symbol)
                player2Lost = true;
        }

        private void MakeMove()
        {
            int row, col;
            do
            {
                Console.WriteLine($"Player {currentPlayer}, enter your move (row and column, separated by space):");
                string[] input = Console.ReadLine().Split(' ');

                if (input.Length != 2 || !int.TryParse(input[0], out row) || !int.TryParse(input[1], out col))
                {
                    Console.WriteLine("Invalid input. Try again.");
                    continue;
                }

                // Уменьшено на 1 для нумерации с 1
                row--;
                col--;

                if (!board.IsValidMove(row, col))
                {
                    Console.WriteLine("Invalid move. Try again.");
                    continue;
                }

                board.MakeMove(row, col, currentPlayer);
                break;
            } while (true);
        }

        private void SwitchPlayer()
        {
            currentPlayer = (currentPlayer == player1Symbol) ? player2Symbol : player1Symbol;
        }

        private bool CheckGameOver()
        {
            if (board.CheckWinner(player1Symbol) || board.CheckWinner(player2Symbol) || player1Lost || player2Lost)
                return true;

            for (int i = 0; i < boardSize; i++)
            {
                for (int j = 0; j < boardSize; j++)
                {
                    if (board.IsValidMove(i, j))
                        return false;
                }
            }

            Console.WriteLine("It's a tie!");
            return true;
        }
    }
}
