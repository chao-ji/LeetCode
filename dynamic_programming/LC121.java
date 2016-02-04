public class LC121
{
	public static void main(String[] args)
	{
	}

	// 121. Best Time to Buy and Sell Stock
	static int maxProfit(int[] prices)
	{
		int len = prices.length;
		int min = Integer.MAX_VALUE;
		int profit = 0;
		for (int i = 0; i < len; i++)
		{
			min = min > prices[i] ? prices[i] : min;
			profit = prices[i] - min > profit ? prices[i] - min : profit; 
		}
		return profit;
	}
}
