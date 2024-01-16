using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Tic_Tac_Toe
{
    class Session : ISession
    {
        private Board board;
        private int boardSize;
        private char currentPlayer;
        private char player1Symbol;
        private char player2Symbol;

        public Session(int boardSize, char player1Symbol, char player2Symbol)
        {
            this.boardSize = boardSize;
            board = new Board(boardSize);
            this.player1Symbol = player1Symbol;
            this.player2Symbol = player2Symbol;
            currentPlayer = player1Symbol;
        }

        public void StartGame()
        {
            do
            {
                board.PrintBoard();
                MakeMove();
                SwitchPlayer();
            } while (!CheckGameOver());

            board.PrintBoard();
            if (currentPlayer == player1Symbol) 
            {
                Console.WriteLine($"Player {player2Symbol} wins!");
            }
            else
            {
                {
                    Console.WriteLine($"Player {player1Symbol} wins!");
                }
            } 
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
            if (board.CheckWinner(player1Symbol) || board.CheckWinner(player2Symbol))
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
