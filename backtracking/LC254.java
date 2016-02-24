import java.util.*;

public class LC254
{
	public static void main(String[] args)
	{
	}

	// 254. Factor Combinations
	static List<List<Integer>> getFactors(int n)
	{
		List<List<Integer>> list = new ArrayList<List<Integer>>();
		recursive(list, new ArrayList<Integer>(), n, 2);
		return list;
	}

	static void recursive(List<List<Integer>> list, List<Integer> factor, int product, int start)
	{
		for (int i = start; i <= product / i; i++)
			if (product % i == 0)
			{
				factor.add(i);
				recursive(list, factor, product / i, i);
				factor.add(product / i);

				list.add(new ArrayList<Integer>());
				list.get(list.size() - 1).addAll(factor);

				factor.remove(factor.size() - 1);
				factor.remove(factor.size() - 1);
			}
	}
}
