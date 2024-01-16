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

        Console.Write("Enter player 1 game time in seconds: ");
        int player1TimeInSeconds = int.Parse(Console.ReadLine());

        Console.Write("Enter player 2 game time in seconds: ");
        int player2TimeInSeconds = int.Parse(Console.ReadLine());

        TimedSession ticTacToeSession = new TimedSession(boardSize, player1Symbol, player2Symbol, player1TimeInSeconds, player2TimeInSeconds);
        ticTacToeSession.StartGame();
    }
}
