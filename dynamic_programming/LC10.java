public class LC10
{
	public static void main(String[] args)
	{
	}

	// 10. Regular Expression Matching
	static boolean isMatch(String s, String p)
	{
		int m = s.length();
		int n = p.length();
		boolean[][] res = new boolean[m + 1][n + 1];
		res[0][0] = true;

		for (int j = 2; j <= n; j++)
			res[0][j] = res[0][j - 2] && p.charAt(j - 1) == '*';

		for (int i = 1; i <= m; i++)
		{
			char sc = s.charAt(i - 1);
			for (int j = 1; j <= n; j++)
			{
				char pc = p.charAt(j - 1);
				if (pc != '*')
					res[i][j] = res[i - 1][j - 1] && (sc == pc || pc == '.');
				else
				{
					char tc = p.charAt(j - 2);
					res[i][j] = res[i][j - 2] || (res[i - 1][j] && (sc == tc || tc == '.'));
				}
			}
		}
		return res[m][n];
	}
}
