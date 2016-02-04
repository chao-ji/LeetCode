public class LC198
{
	public static void main(String[] args)
	{
	}

	// 198. House Robber
	static int rob(int[] nums)
	{
		int len = nums.length;
		int[] dp = new int[len];
		for (int i = 0; i < len; i++)
			if (i == 0)
				dp[i] = nums[i];
			else if (i == 1)
				dp[i] = Math.max(nums[i], dp[i - 1]);
			else
				dp[i] = Math.max(nums[i] + dp[i - 2], dp[i - 1]);
                
		return len == 0 ? 0 : dp[len - 1];        
	}
}
