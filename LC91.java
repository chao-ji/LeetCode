public class LC91
{
	public static void main(String[] args)
	{
	}

	// 91. Decode Ways
	static int numDecodings(String s)
	{
		if (s.length() == 0)
			return 0;
		int[] dp = new int[s.length() + 1];
		dp[0] = 1;
		for (int i = 1; i <= s.length(); i++)
		{
			int one = (int) s.charAt(i - 1) - '0';
			dp[i] = one >= 1 && one <= 9 ? dp[i - 1] : dp[i];
			if (i > 1)
			{
				int two = Integer.parseInt(s.substring(i - 2, i));
				dp[i] = two >= 10 && two <= 26 ? dp[i] + dp[i - 2] : dp[i];
			}
		}
		return dp[s.length()];
	}
}
