public class LC264
{
	public static void main(String[] args)
	{
	}

	// 264. Ugly Number II
	static int nthUglyNumber(int n)
	{
		if (n == 1)
			return 1;
		int[] dp = new int[n + 1];
		dp[1] = 1;
		int i2 = 1;
		int i3 = 1;
		int i5 = 1;
        
		for(int i = 2; i <= n; i++)
		{ 
			dp[i] = Math.min(2 * dp[i2], Math.min(3 * dp[i3], 5 * dp[i5]));
			if (dp[i] == 2 * dp[i2])
				i2++; 
			if (dp[i] == 3 * dp[i3])
				i3++;
			if (dp[i] == 5 * dp[i5])
				i5++;
		}
		return dp[n];
	}
}
