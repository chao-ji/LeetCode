import java.util.*;
public class LC131
{
	public static void main(String[] args)
	{
		System.out.println(partition("seeslaveidemonstrateyetartsnomedievalsees"));
	}

	// 131. Palindrome Partitioning
	static List<List<String>> partition(String s)
	{
		int len = s.length();
		boolean[][] dp = new boolean[len][len];
		for (int i = 1; i <= len; i++)
			for (int j = 0; j < len - i + 1; j++)
				dp[j][j + i - 1] = s.charAt(j) == s.charAt(j + i - 1) && (i <= 2 || dp[j + 1][j + i - 2]);

		List<List<String>> parts = new ArrayList<List<String>>();

		int[] start = new int[1];
		for (int i = 0; i < dp.length; i++)
			if (dp[0][i])
			{
				List<String> part = new ArrayList<String>();
				part.add(s.substring(0, i + 1));
				start[0] = i + 1;
				recursive(parts, part, dp, s, start);
			}	

		return parts;
	}

	static void recursive(List<List<String>> parts, List<String> part, boolean[][] dp, String s, int[] start)
	{
		if (part.isEmpty())
			return ;
		if (start[0] == dp.length)
		{
			parts.add(new ArrayList<String>());
			parts.get(parts.size() - 1).addAll(part);

			start[0] -= part.get(part.size() - 1).length();
			part.remove(part.size() - 1);
			return ;
		}

		for (int i = start[0]; i < dp.length; i++)
			if (dp[start[0]][i])
			{
				part.add(s.substring(start[0], i + 1));
				start[0] = i + 1;
				recursive(parts, part, dp, s, start);
			}
		start[0] -= part.get(part.size() - 1).length();
		part.remove(part.size() - 1);		
	} 
}
