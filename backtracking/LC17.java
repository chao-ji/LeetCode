import java.util.*;

public class LC17
{
	public static void main(String[] args)
	{
	}

	// 17. Letter Combinations of a Phone Number	
	static List<String> letterCombinations(String digits)
	{
		String[] map = {"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
		List<String> list = new ArrayList<String>();
		if (digits == null || digits.isEmpty())
			return list;
		else if (digits.length() == 1)
		{
			String letters = map[digits.charAt(0) - 48];
			for (int i = 0; i < letters.length(); i++)
				list.add(letters.substring(i, i + 1));
		}

		List<String> dp = letterCombinations(digits.substring(0, digits.length() - 1));
		String letters = map[digits.charAt(digits.length() - 1) - 48];
		for (int i = 0; i < dp.size(); i++)
			for (int j = 0; j < letters.length(); j++)
				list.add(dp.get(i) + letters.substring(j, j + 1));

		return list;
	}
}
