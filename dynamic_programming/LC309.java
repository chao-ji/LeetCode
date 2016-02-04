public class LC309
{
	public static void main(String[] args)
	{
	}

	// 309. Best Time to Buy and Sell Stock with Cooldown
	static int maxProfit(int[] prices)
	{
		int len = prices.length;
		if (len < 2)
			return 0;
		int[] dp = new int[len];
		int max = -prices[0];
		for (int i = 1; i < len; i++)
		{
			dp[i] = Math.max(dp[i - 1], prices[i] + max);
			int val = i - 2 >= 0 ? -prices[i] + dp[i - 2] : -prices[i];    
			max = max < val ? val : max;
		}
		return dp[len - 1];
	}
}
