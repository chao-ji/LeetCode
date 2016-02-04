import java.util.*;

public class LC77
{
	public static void main(String[] args)
	{
	}

	// 77. Combinations
	static List<List<Integer>> combine(int n, int k)
	{
		List<List<Integer>> list = new ArrayList<List<Integer>>();
		if (k == 0)
		{
			list.add(new ArrayList<Integer>());
			return list;
		}
		else if (n < k)
			return list;

		List<List<Integer>> sub1 = combine(n - 1, k);
		for (int i = 0; i < sub1.size(); i++)
			list.add(sub1.get(i));

		List<List<Integer>> sub2 = combine(n - 1, k - 1);
		for (int i = 0; i < sub2.size(); i++)
		{
			sub2.get(i).add(n);
			list.add(sub2.get(i));
		}
		return list;
	}
}
