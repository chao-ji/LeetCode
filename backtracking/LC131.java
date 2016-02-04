import java.util.*;
public class LC131
{
	public static void main(String[] args)
	{
	}

	// 131. Palindrome Partitioning
	static List<List<String>> partition(String s)
	{
		int len = s.length();
		boolean[][] dp = new boolean[len][len];
		for (int i = 1; i <= len; i++)
			for (int j = 0; j < len - i + 1; j++)
				dp[j][j + i - 1] = s.charAt(j) == s.charAt(j + i - 1) && (i <= 2 || dp[j + 1][j + i - 2]);
		return partition(s, dp, 0, len - 1);
	}

	static List<List<String>> partition(String s, boolean[][] dp, int l, int h)
	{
		List<List<String>> list = new ArrayList<List<String>>();
		if (dp[l][h])
		{
			list.add(new ArrayList<String>());
			list.get(list.size() - 1).add(s.substring(l, h + 1));
		}
		if (l == h)
			return list;

		for (int i = l; i < h; i++)
			if (dp[l][i])
			{
				List<List<String>> sub = partition(s, dp, i + 1, h);
				for (int j = 0; j < sub.size(); j++)
				{
					List<String> p = new ArrayList<String>();
					p.add(s.substring(l, i + 1));
					p.addAll(sub.get(j));
					list.add(p);
				}
			}
		return list;
	}
}
