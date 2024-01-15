using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Tic_Tac_Toe
{
   
class Board : IBoard
    {
        private char[,] board;
        private int size;

        public Board(int boardSize)
        {
            size = boardSize;
            board = new char[size, size];
            InitializeBoard();
        }

        private void InitializeBoard()
        {
            for (int i = 0; i < size; i++)
            {
                for (int j = 0; j < size; j++)
                {
                    board[i, j] = ' ';
                }
            }
        }

        public void PrintBoard()
        {
            Console.Clear();
            Console.WriteLine("Current Board:");

            for (int i = 0; i < size; i++)
            {
                for (int j = 0; j < size; j++)
                {
                    Console.Write(board[i, j] + " ");
                }
                Console.WriteLine();
            }
        }

        public bool IsValidMove(int row, int col)
        {
            return row >= 0 && row < size && col >= 0 && col < size && board[row, col] == ' ';
        }

        public void MakeMove(int row, int col, char playerSymbol)
        {
            board[row, col] = playerSymbol;
        }

        public bool CheckWinner(char playerSymbol)
        {
            for (int i = 0; i < size; i++)
            {
                if (CheckRow(i, playerSymbol) || CheckColumn(i, playerSymbol))
                    return true;
            }

            return CheckDiagonals(playerSymbol);
        }

        private bool CheckRow(int row, char playerSymbol)
        {
            for (int i = 0; i < size; i++)
            {
                if (board[row, i] != playerSymbol)
                    return false;
            }
            return true;
        }

        private bool CheckColumn(int col, char playerSymbol)
        {
            for (int i = 0; i < size; i++)
            {
                if (board[i, col] != playerSymbol)
                    return false;
            }
            return true;
        }

        private bool CheckDiagonals(char playerSymbol)
        {
            bool leftDiagonal = true;
            bool rightDiagonal = true;

            for (int i = 0; i < size; i++)
            {
                leftDiagonal &= (board[i, i] == playerSymbol);
                rightDiagonal &= (board[i, size - 1 - i] == playerSymbol);
            }

            return leftDiagonal || rightDiagonal;
        }
    }
}
