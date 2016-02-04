public class LC221
{
	public static void main(String[] args)
	{
	}

	// 221. Maximal Square
	static int maximalSquare(char[][] matrix)
	{
		int m = matrix.length;
		if (m == 0)
			return 0;
		int n = matrix[0].length;
        
		int max = 0;
		int[][] dp = new int[m][n];
		for (int i = 0; i < m; i++)
		{
			dp[i][0] = matrix[i][0] == '1' ? 1 : 0;
			max = max < dp[i][0] ? dp[i][0] : max;
		}
		for (int j = 1; j < n; j++)
		{
			dp[0][j] = matrix[0][j] == '1' ? 1 : 0;
			max = max < dp[0][j] ? dp[0][j] : max;
		}
        
		for (int i = 1; i < m; i++)
			for (int j = 1; j < n; j++)
				if (matrix[i][j] == '1')
				{
					dp[i][j] = Math.min(Math.min(dp[i][j - 1], dp[i - 1][j]), dp[i - 1][j - 1]) + 1;
					max = max < dp[i][j] ? dp[i][j] : max;
				}

		return max * max;
	}
}
