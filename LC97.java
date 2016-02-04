public class LC97
{
	public static void main(String[] args)
	{
	}

	// 97. Interleaving String
	static boolean isInterleave(String s1, String s2, String s3)
	{
		int m = s1.length();
		int n = s2.length();
		int p = s3.length();
		if (m + n != p)
			return false;

		boolean[][] dp = new boolean[m + 1][n + 1];
		dp[0][0] = true;
		for (int i = 1; i <= m; i++)
			if (s1.charAt(i - 1) != s3.charAt(i - 1))
				break;
			else
				dp[i][0] = true;

		for (int j = 1; j <= n; j++)
			if (s2.charAt(j - 1) != s3.charAt(j - 1))
				break;
			else
				dp[0][j] = true;

		for (int i = 1; i <= m; i++)
			for (int j = 1; j <= n; j++)
			{
				boolean match1 = s3.charAt(i + j - 1) == s1.charAt(i - 1) && dp[i - 1][j];
				boolean match2 = s3.charAt(i + j - 1) == s2.charAt(j - 1) && dp[i][j - 1];
				dp[i][j] = match1 || match2;
			}
		return dp[m][n];
	}
}
