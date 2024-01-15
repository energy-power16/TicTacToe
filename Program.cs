using Tic_Tac_Toe;

class Program
{
    static void Main()
    {
        Console.WriteLine("Welcome to Tic-Tac-Toe!");
        Console.Write("Enter the size of the board: ");
        int boardSize = int.Parse(Console.ReadLine());

        Console.Write("Enter player 1 symbol: ");
        char player1Symbol = char.Parse(Console.ReadLine());

        Console.Write("Enter player 2 symbol: ");
        char player2Symbol = char.Parse(Console.ReadLine());

        Session ticTacToeSession = new Session(boardSize, player1Symbol, player2Symbol);
        ticTacToeSession.StartGame();
    }
}