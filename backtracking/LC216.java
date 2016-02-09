import java.util.*;

public class LC216
{
	public static void main(String[] args)
	{
	}

	// 216. Combination Sum III
	static List<List<Integer>> combinationSum3(int k, int n)
	{
		List<List<Integer>> list = new ArrayList<List<Integer>>();
		int[] sum = new int[1];
		for (int i = 1; i <= 9; i++)
		{
			List<Integer> path = new ArrayList<Integer>();
			path.add(i);
			sum[0] += i;
			recursive(list, path, k, n, sum);
		}
		return list;
	}

	static void recursive(List<List<Integer>> list, List<Integer> path, int k, int n, int[] sum)
	{
		if (path.isEmpty())
			return ;
		if (path.size() == k)
		{
			if (sum[0] == n)
			{
				list.add(new ArrayList<Integer>());
				list.get(list.size() - 1).addAll(path);
			}
			sum[0] -= path.get(path.size() - 1);
			path.remove(path.size() - 1);
			return ;
		}

		int last = path.get(path.size() - 1);
		for (int i = last + 1; i <= 9; i++)
		{
			path.add(i);
			sum[0] += i;
			recursive(list, path, k, n, sum);
		}

		sum[0] -= path.get(path.size() - 1);
		path.remove(path.size() - 1);
	}
}
