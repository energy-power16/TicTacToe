using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Tic_Tac_Toe
{
    public interface IBoard
    {
        void PrintBoard();
        bool IsValidMove(int row, int col);
        void MakeMove(int row, int col, char playerSymbol);
        bool CheckWinner(char playerSymbol);
    }
}
