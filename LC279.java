public class LC279
{
	public static void main(String[] args)
	{
	}

	// 279. Perfect Squares
	static int numSquares(int n)
	{
		int[] dp = new int[n + 1];
		for (int i = 1; i <= n; i++)
		{
			dp[i] = i;
			for (int j = 1; j * j <= i; j++)
				dp[i] = dp[i] > 1 + dp[i - j * j] ? 1 + dp[i - j * j] : dp[i];
		}
		return dp[n];
	}
}
