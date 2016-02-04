import java.util.*;

public class LC140
{
	public static void main(String[] args)
	{
	}

	// 140. Word Break II
	static List<String> wordBreak(String s, Set<String> wordDict)
	{
		int len = s.length();
		List<String> list = new ArrayList<String>();
		boolean[] breakable = new boolean[len + 1];
		breakable[len] = true;
		for (int i = len - 1; i >= 0; i--)
		{
			breakable[i] = wordDict.contains(s.substring(i));
			breakable[i] = i < len - 1 ? breakable[i] || breakable[i + 1] : breakable[i];
		}

		ArrayList<List<String>> dp = new ArrayList<List<String>>();
		list.add("");
		dp.add(list);
        
		for (int i = 1; i <= len; i++)
		{
			list = new ArrayList<String>();
			if (breakable[i] == true)
			{
				for (int j = i - 1; j >= 0; j--)
				{
					String last = s.substring(j, i);
					if (wordDict.contains(last))
					{
						List<String> prefix = dp.get(j);
						for (int k = 0; k < prefix.size(); k++)
						{
							String str = !prefix.get(k).equals("") ? prefix.get(k) + " " + last : last;
							list.add(str);
						}
					}
				}
			}
			dp.add(list);
		}
        
		return dp.get(dp.size() - 1);
	}
}
