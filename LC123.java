public class LC123
{
	public static void main(String[] args)
	{
	}

	// 123. Best Time to Buy and Sell Stock III
	static int maxProfit(int[] prices)
	{
		int len = prices.length;
		int min = Integer.MAX_VALUE;
		int[] profit = new int[len];
		for (int i = 0; i < len; i++)
		{
			min = min > prices[i] ? prices[i] : min;
			profit[i] = i > 0 ? profit[i - 1] : profit[i];
			profit[i] = prices[i] - min > profit[i] ? prices[i] - min : profit[i];
		}
        
		int max = Integer.MIN_VALUE;
		int val = 0;
		for (int i = len - 1; i >= 0; i--)
		{
			max = max < prices[i] ? prices[i] : max;
			val = val < profit[i] + max - prices[i] ? profit[i] + max - prices[i] : val; 
		}
		return val;
	}
}
