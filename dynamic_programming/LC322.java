public class LC322
{
	public static void main(String[] args)
	{
	}

	// 322. Coin Change
	static int coinChange(int[] coins, int amount)
	{
		int len = coins.length;
		int[] dp = new int[amount + 1];
		for (int i = 1; i <= amount; i++)
		{
			dp[i] = Integer.MAX_VALUE;
			for (int j = 0; j < len; j++)
				if (i >= coins[j])
					dp[i] = Math.min(dp[i], dp[i - coins[j]]);
			dp[i] = dp[i] != Integer.MAX_VALUE ? dp[i] + 1 : dp[i];        
		}
		return dp[amount] == Integer.MAX_VALUE ? -1 : dp[amount];
	}
}
