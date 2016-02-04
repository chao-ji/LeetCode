public class LC213
{
	public static void main(String[] args)
	{
	}

	// 213. House Robber II
	static int rob(int[] nums)
	{
		int len = nums.length;
		if (len < 2)
			return len == 0 ? 0 : nums[0];
		int[] dp = new int[len];
		for (int i = 0; i < len - 1; i++)
			if (i == 0)
				dp[i] = nums[i];
			else if (i == 1)
				dp[i] = Math.max(nums[i], dp[i - 1]);
			else
				dp[i] = Math.max(nums[i] + dp[i - 2], dp[i - 1]);
        
		int max = dp[len - 2];
        
		dp = new int[len];
		for (int i = 1; i < len; i++)
			if (i == 1)
				dp[i] = nums[i];
			else if (i == 2)
				dp[i] = Math.max(nums[i], dp[i - 1]);
			else
				dp[i] = Math.max(nums[i] + dp[i - 2], dp[i - 1]);
		max = max < dp[len - 1] ? dp[len - 1] : max;
		return max;
	}
}
