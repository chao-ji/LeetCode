public class LC376
{
	public static void main(String[] args)
	{
	}

	// 376. Wiggle Subsequence
	public int wiggleMaxLength(int[] nums)
	{
		if (nums == null || nums.length == 0)
			return 0;
		int[][] dp = new int[nums.length][4];
 
		for (int i = 0; i < nums.length; i++)
			if (i == 0)
			{
				dp[i][0] = dp[i][2] = 1;
				dp[i][1] = dp[i][3] = nums[i];
			}
			else
			{
				if (nums[i] < dp[i - 1][1])
				{
					dp[i][2] = dp[i - 1][0] + 1;
					dp[i][3] = nums[i];
				}
				else
				{
					dp[i][0] = dp[i - 1][0];
					dp[i][1] = nums[i];
				}
 
				if (nums[i] > dp[i - 1][3])
				{
					if (dp[i - 1][2] + 1 > dp[i][0])
					{
						dp[i][0] = dp[i - 1][2] + 1;
						dp[i][1] = nums[i];
					}
				}
				else
				{
					if (dp[i - 1][2] > dp[i][2])
					{
						dp[i][2] = dp[i - 1][2];
						dp[i][3] = nums[i];
					}
				}
			}
 
		return Math.max(dp[nums.length - 1][0], dp[nums.length - 1][2]);
	}
}
