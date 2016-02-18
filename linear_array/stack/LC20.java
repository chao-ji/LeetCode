import java.util.*;

public class LC20
{
	public static void main(String[] args)
	{
	}

	// 20. Valid Parentheses
	static boolean isValid(String s)
	{
		if (s.isEmpty())
			return true;
		List<Character> stack = new ArrayList<Character>();
		for (int i = 0; i < s.length(); i++)
		{
			char c = s.charAt(i);
			if (stack.isEmpty())
			{
				if (c == '(' || c == '{' || c == '[')
					stack.add(c);
				else
					return false;
			}
			else
			{
				char d = stack.get(stack.size() - 1);
				if (c == ')' || c == '}' || c == ']')
				{
					if ((d == '(' && c == ')') || (d == '{' && c == '}') || (d == '[' && c == ']'))
						stack.remove(stack.size() - 1);
					else
						return false;
				}
				else
					stack.add(c);
			}
		}

		if (stack.isEmpty())
			return true;
		return false;    
	}
}
