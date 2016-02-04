public class LC188
{
	public static void main(String[] args)
	{
	}

	// 188. Best Time to Buy and Sell Stock IV
	static int maxProfit(int k, int[] prices)
	{
		int len = prices.length;
		if (k >= len / 2)
		{
			int profit = 0;
			for (int i = 0; i < len - 1; i++)
				if (prices[i + 1] > prices[i])
					profit += (prices[i + 1] - prices[i]);
			return profit;        
		}
        
		int[][] dp = new int[k + 1][len];
        
		for (int i = 1; i <= k; i++)
		{
			int max = dp[i - 1][0] - prices[0];
			for (int j = 1; j < len; j++)
			{
				max = Math.max(max, dp[i - 1][j - 1] - prices[j - 1]);
				dp[i][j] = Math.max(max + prices[j], dp[i][j - 1]);
			}
		}
        
		return dp[k][len - 1];
	}
}
