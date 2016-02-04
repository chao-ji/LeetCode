public class LC37
{
	public static void main(String[] args)
	{
	}

	// 37. Sudoku Solver
	static void solveSudoku(char[][] board)
	{
		isSolvable(board);
	}

	static boolean isSolvable(char[][] board)
	{
		for (int i = 0; i < 9; i++)
			for (int j = 0; j < 9; j++)
				if (board[i][j] == '.')
				{
					for (char k = '1'; k <= '9'; k++)
						if (isValid(board, i, j, k))
						{
							board[i][j] = k;
							if (isSolvable(board))
								return true;
							else
								board[i][j] = '.';
						}
					return false;
				}
		return true;
	}

	static boolean isValid(char[][] board, int x, int y, int val)
	{
		for (int i = 0; i < 9; i++)
			if (i != x && board[i][y] == val)
				return false;
		for (int j = 0; j < 9; j++)
			if (j != y && board[x][j] == val)
				return false;
		for (int i = (x / 3) * 3; i < (x / 3) * 3 + 3; i++)
			for (int j = (y / 3) * 3; j < (y / 3) * 3 + 3; j++)
				if ((i != x || j != y) && board[i][j] == val)
					return false;
		return true;            
	}

}
