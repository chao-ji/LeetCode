import java.util.*;

public class LC216
{
	public static void main(String[] args)
	{
	}

	// 216. Combination Sum III
	static List<List<Integer>> combinationSum3(int k, int n)
	{
		return combinationSum3(k, n, 1);
	}

	static List<List<Integer>> combinationSum3(int k, int n, int s)
	{
		List<List<Integer>> list = new ArrayList<List<Integer>>();
		if (k == 1)
		{
			if (n >= s && n <= 9)
			{
				list.add(new ArrayList<Integer>());
				list.get(0).add(n);
			}
			return list;
		}
		for (int i = s; i <= 9; i++)
			if (i < n)
			{
				List<List<Integer>> sub = combinationSum3(k - 1, n - i, i + 1);
				for (int j = 0; j < sub.size(); j++)
				{
					List<Integer> p = new ArrayList<Integer>();
					p.add(i);
					p.addAll(sub.get(j));
					list.add(p);
				}
			}
		return list;    
	}
}
