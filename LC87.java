public class LC87
{
	public static void main(String[] args)
	{
	}

	// 87. Scramble String
	static boolean isScramble(String s1, String s2)
	{
		int len = s1.length();    
		boolean[][][] dp = new boolean[len][len][len];
        
		for (int k = 0; k < len; k++)
			for (int i = 0; i < len - k; i++)
				for (int j = 0; j < len - k; j++)
					if (k == 0)
						dp[i][j][k] = s1.charAt(i) == s2.charAt(j);
					else
						for (int l = 0; l < k; l++)
							if ((dp[i][j][l] && dp[i + l + 1][j + l + 1][k - l - 1]) || (dp[i][j + k - l][l] && dp[i + l + 1][j][k - l - 1]))
							{
								dp[i][j][k] = true;
								break;
							}
                    
		return dp[0][0][len - 1];
	}	
}
