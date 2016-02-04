import java.util.*;

public class LC22
{
	public static void main(String[] args)
	{
	}

	// 22. Generate Parentheses	
	static List<String> generateParenthesis(int n)
	{
		List<String> list = new ArrayList<String>();
		if (n <= 0)
		{
			list.add("");
			return list;
		}

		for (int i = 0; i < n; i++)
		{
			List<String> left = generateParenthesis(i);
			List<String> right = generateParenthesis(n - i - 1);

			for (int j = 0; j < left.size(); j++)
				for (int k = 0; k < right.size(); k++)
					list.add("(" + left.get(j) + ")" + right.get(k));
		}

		return list;
	}
}
