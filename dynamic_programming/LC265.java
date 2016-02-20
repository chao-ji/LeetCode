public class LC265
{
	public static void main(String[] args)
	{
	}

	// 265. Paint House II
	static int minCostII(int[][] costs)
	{
		if (costs.length == 0)
			return 0;

		int n = costs.length;
		int k = costs[0].length;
		int[][] dp = new int[n][k];
		int[] minFwd = new int[k];
		int[] minBwd = new int[k];

		for (int j = 0; j < k; j++)
			dp[0][j] = costs[0][j];
		for (int j = 0; j < k - 1; j++)    
			minFwd[j] = j == 0 ? dp[0][j] : Math.min(dp[0][j], minFwd[j - 1]);
		for (int j = k - 1; j > 0; j--)
			minBwd[j] = j == k - 1 ? dp[0][j] : Math.min(dp[0][j], minBwd[j + 1]);

		for (int i = 1; i < n; i++)
		{
			for (int j = 0; j < k; j++)
				if (j == 0)
					dp[i][j] = costs[i][j] + minBwd[1];
				else if (j == k - 1)
					dp[i][j] = costs[i][j] + minFwd[k - 2];
				else    
					dp[i][j] = costs[i][j] + Math.min(minFwd[j - 1], minBwd[j + 1]);
			for (int j = 0; j < k - 1; j++)
				minFwd[j] = j == 0 ? dp[i][j] : Math.min(dp[i][j], minFwd[j - 1]);
			for (int j = k - 1; j > 0; j--)
				minBwd[j] = j == k - 1 ? dp[i][j] : Math.min(dp[i][j], minBwd[j + 1]);
		}

		int min = 0;
		for (int j = 0; j < k; j++)
			min = min == 0 ? dp[n - 1][j] : Math.min(min, dp[n - 1][j]);
		return min;    
	}
}
