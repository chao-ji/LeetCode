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
		boolean[][] dp = new boolean[m][n];
		for (int i = 0; i < m; i++)
			for (int j = 0; j < n; j++)
				if (recursive(board, dp, word, i, j))
					return true;
		return false;
	}

	static boolean recursive(char[][] board, boolean[][] dp, String word, int i, int j)
	{
		if (word.length() == 1 || word.charAt(0) != board[i][j])
			return word.charAt(0) == board[i][j];
		dp[i][j] = true;
		if (j > 0 && dp[i][j - 1] == false)
			if (recursive(board, dp, word.substring(1), i, j - 1))
				return true;
		if (i > 0 && dp[i - 1][j] == false)
			if (recursive(board, dp, word.substring(1), i - 1, j))
				return true;
		if (j < board[0].length - 1 && dp[i][j + 1] == false)
			if (recursive(board, dp, word.substring(1), i, j + 1))
				return true;
		if (i < board.length - 1 && dp[i + 1][j] == false)
			if (recursive(board, dp, word.substring(1), i + 1, j))
				return true;
		dp[i][j] = false;
		return false;
	}
}
