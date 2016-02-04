public class LC130
{
	public static void main(String[] args)
	{
	}
	
	// 130. Surrounded Regions
	static void solve(char[][] board)
	{
		if (board == null || board.length <= 2 || board[0].length <= 2)
			return ;
		int m = board.length;
		int n = board[0].length;
		for (int i = 0; i < m; i++)
		{
			fill(board, i, 0);
			fill(board, i, n - 1);
		}
		for (int j = 1; j < n - 1; j++)
		{
			fill(board, 0, j);
			fill(board, m - 1, j);
		}
		for (int i = 0; i < m; i++)
			for (int j = 0; j < n; j++)
				if (board[i][j] == 'I')
					board[i][j] = 'O';
				else if (board[i][j] == 'O')
					board[i][j] = 'X';
	}

	static void fill(char[][] board, int i, int j)
	{
		if (board[i][j] == 'O')
			board[i][j] = 'I';
		else
			return;
		int m = board.length;
		int n = board[0].length;
		if (i - 1 > 0)
			fill(board, i - 1, j);
		if (j + 1 < n - 1)
			fill(board, i, j + 1);
		if (i + 1 < m - 1)
			fill(board, i + 1, j);
		if (j - 1 > 0)
			fill(board, i, j - 1);
	}
}
