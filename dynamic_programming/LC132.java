public class LC132
{
	public static void main(String[] args)
	{
	}

	// 132. Palindrome Partitioning II
	static int minCut(String s)
	{
		int len = s.length();
		int[] dp = new int[len];
		boolean[][] pal = new boolean[len][len];

		for (int i = 1; i <= len; i++)
			for (int j = 0; j <= len - i; j++)
				pal[j][j + i - 1] = s.charAt(j) == s.charAt(j + i - 1) && (i <= 2 || pal[j + 1][j + i - 2]);

		for (int i = 0; i < len; i++)
		{
			int min = i;
			for (int j = 0; j <= i; j++)
				if (pal[j][i] == true)
					min = Math.min(min, j == 0 ? 0 : dp[j - 1] + 1);
			dp[i] = min;
		}
		return dp[len - 1];
	}	
}
