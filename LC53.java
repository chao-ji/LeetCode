public class LC53
{
	public static void main(String[] args)
	{
	}

	// 53. Maximum Subarray
	static int maxSubArray(int[] nums)
	{
		int len = nums.length;
		int[] dp = new int[len];
		int max = Integer.MIN_VALUE;
		for (int i = 0; i < len; i++)
		{
			dp[i] = i > 0 && dp[i - 1] > 0 ? nums[i] + dp[i - 1] : nums[i];
			max = max < dp[i] ? dp[i] : max;
		}
		return max;
	}
}
