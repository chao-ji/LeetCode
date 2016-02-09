import java.util.*;

public class LC17
{
	public static void main(String[] args)
	{
		System.out.println(letterCombinations("23"));
	}

	// 17. Letter Combinations of a Phone Number	
	static List<String> letterCombinations(String digits)
	{
		String[] map = {"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
		List<String> list = new ArrayList<String>();
		if (digits == null || digits.isEmpty())
			return list;
		int[] start = new int[1];
		start[0] = 0;
		String next = map[digits.charAt(0) - 48];
		for (int i = 0; i < next.length(); i++)
		{
			StringBuilder combo = new StringBuilder();
			combo.append(next.charAt(i));
			start[0]++;
			recursive(list, combo, digits, map, start);
		}
		return list;
	}

	static void recursive(List<String> list, StringBuilder combo, String digits, String[] map, int[] start)
	{
		if (combo.length() == 0)
			return ;
		if (combo.length() == digits.length())
		{
			list.add(new String(combo));
			combo.deleteCharAt(combo.length() - 1);
			start[0]--;
			return ;
		}

		String next = map[digits.charAt(start[0]) - 48];
		for (int i = 0; i < next.length(); i++)
		{
			combo.append(next.charAt(i));
			start[0]++;
			recursive(list, combo, digits, map, start);
		}
		
		combo.deleteCharAt(combo.length() - 1);
		start[0]--;	
	}
}
