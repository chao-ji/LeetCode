public class LC32
{
	public static void main(String[] args)
	{	
	}

	// 32. Longest Valid Parentheses
	static int longestValidParenthese(String s)
	{
		int max = 0;
		int[] dp = new int[s.length()];
		for (int i = 1; i < s.length(); i++)
			if (s.charAt(i) == ')')
			{
				int j = i - dp[i - 1] - 1;
				if (j >= 0 && s.charAt(j) == '(')
					dp[i] = dp[i - 1] + 2;
				else
					continue;
				dp[i] = j >= 1 ? dp[i] + dp[j - 1] : dp[i];
				max = max < dp[i] ? dp[i] : max;
			}
		return max;
	}
}
