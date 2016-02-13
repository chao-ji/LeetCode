public class LC79
{
	public static void main(String[] args)
	{
	}

	// 79. Word Search
	static boolean exist(char[][] board, String word)
	{
		int m = board.length;
		if (m == 0)
			return false;
		int n = board[0].length;
		for (int i = 0; i < m; i++)
			for (int j = 0; j < n; j++)
				if (recursive(board, word, i, j))
					return true;
		return false;
	}

	static boolean recursive(char[][] board, String word, int i, int j)
	{
		if (word.length() == 1 || word.charAt(0) != board[i][j])
			return word.charAt(0) == board[i][j];
		char hold = board[i][j];
		board[i][j] = '*';
		if (j > 0 && board[i][j - 1] != '*')
			if (recursive(board, word.substring(1), i, j - 1))
				return true;
		if (i > 0 && board[i - 1][j] != '*')
			if (recursive(board, word.substring(1), i - 1, j))
				return true;
		if (j < board[0].length - 1 && board[i][j + 1] != '*')
			if (recursive(board, word.substring(1), i, j + 1))
				return true;
		if (i < board.length - 1 && board[i + 1][j] != '*')
			if (recursive(board, word.substring(1), i + 1, j))
				return true;
		board[i][j] = hold;
		return false;
	}
}
