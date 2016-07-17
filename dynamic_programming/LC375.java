public class LC375
{
	public static void main(String[] args)
	{
	}

	// 375. Guess Number Higher or Lower II
	static int getMoneyAmount(int n)
	{
		int[][] dp = new int[n + 1][n + 1];
		for (int l = 2; l <= n; l++)
			for (int i = 1; i + l - 1 <= n; i++)
			{
				dp[i][i + l - 1] = Integer.MAX_VALUE;
				for (int j = i; j <= i + l - 1; j++)
				{
					int val = j;
					if (j == i)
						val += dp[j + 1][i + l - 1];
					else if (j == i + l - 1)
						val += dp[i][j - 1];
					else
						val += Math.max(dp[i][j - 1], dp[j + 1][i + l - 1]);
					dp[i][i + l - 1] = Math.min(dp[i][i + l - 1], val);    
				}
			}   
		return dp[1][n];        
	}	
}
