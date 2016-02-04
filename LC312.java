public class LC312
{
	public static void main(String[] args)
	{
	}

	// 312. Burst Balloons
	static int maxCoins(int[] nums)
	{
		int len = nums.length;
		int[] array = new int[len + 2];
		array[0] = 1;
		array[len + 1] = 1;
		for (int i = 1; i <= len; i++)
			array[i] = nums[i - 1];
        
		int[][] dp = new int[len + 2][len + 2];
        
		for (int i = 1; i <= len; i++)
			for (int j = 1; j <= len - i + 1; j++)
			{
				int max = 0;
				for (int k = j; k <= j + i - 1; k++)
					max = Math.max(max, dp[j][k - 1] + dp[k + 1][j + i - 1] + array[j - 1] * array[k] * array[j + i]);
				dp[j][j + i - 1] = max;
			}    
		return dp[1][len];
	}
}
