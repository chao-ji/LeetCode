public class LC300
{
	public static void main(String[] args)
	{
	}

	// 300. Longest Increasing Subsequence
	static int lengthOfLIS(int[] nums)
	{
		int len = nums.length;
		if (len == 0)
			return 0;
		int[] dp = new int[len];
		int val = 1;
		dp[0] = 1;
		for (int i = 1; i < len; i++)
		{
			for (int j = 0; j < i; j++)
				if (nums[j] < nums[i])
					dp[i] = dp[j] > dp[i] ? dp[j] : dp[i];
			dp[i] = dp[i] + 1;
			val = val < dp[i] ? dp[i] : val;
		}
		return val;
	}
}
