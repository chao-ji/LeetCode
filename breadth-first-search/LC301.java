import java.util.*;

public class LC301
{
	public static void main(String[] args)
	{
	}

	// 301. Remove Invalid Parentheses
	static List<String> removeInvalidParentheses(String s)
	{
		List<String> list = new ArrayList<String>();
		Deque<String> queue = new ArrayDeque<String>();
		Set<String> visited = new HashSet<String>();
		queue.addLast(s);
		while (!queue.isEmpty())
		{
			s = queue.removeFirst();
			int us = getUnpaired(s);
			if (us == 0)
				list.add(s);
			else
				for (int i = 0; i < s.length(); i++)
					if (s.charAt(i) == '(' || s.charAt(i)== ')')
					{
						String t = s.substring(0, i) + s.substring(i + 1, s.length());
						if (!visited.contains(t) && getUnpaired(t) < us)
						{
							visited.add(t);
							queue.addLast(t);
						}
					}
		}
		return list;	
	}

	static int getUnpaired(String s)
	{
		int right = 0;
		int match = 0;
		for (int i = 0; i < s.length(); i++)
		{
			if (s.charAt(i) == '(')
				match++;
			else if (s.charAt(i) == ')')
				match--;
			right = match < 0 ? right + 1 : right;
			match = match < 0 ? 0 : match;
		}
		return match + right;
        }
}
