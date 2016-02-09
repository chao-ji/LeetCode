import java.util.*;

public class LC39
{
	public static void main(String[] args)
	{
		int[] candidates = {2, 3, 6 ,7};
		System.out.println(combinationSum(candidates, 7));
	}

	// 39. Combination Sum
	static List<List<Integer>> combinationSum(int[] candidates, int target)
	{
		List<List<Integer>> list = new ArrayList<List<Integer>>();
		Arrays.sort(candidates);
		int[] sum = new int[1];
		for (int i = 0; i < candidates.length; i++)
		{
			List<Integer> path = new ArrayList<Integer>();
			path.add(candidates[i]);
			sum[0] += candidates[i];
			recursive(list, path, candidates, i, sum, target);
		}

		return list;
	}

	static void recursive(List<List<Integer>> list, List<Integer> path, int[] candidates, int start, int[] sum, int target)
	{
		if (path.isEmpty())
			return ;

		if (sum[0] >= target)
		{
			if (sum[0] == target)
			{
				list.add(new ArrayList<Integer>());
				list.get(list.size() - 1).addAll(path);
			}
			sum[0] -= path.get(path.size() - 1);
			path.remove(path.size() - 1);
			return ;
		}

		for (int i = start; i < candidates.length; i++)
		{
			path.add(candidates[i]);
			sum[0] += candidates[i];
			recursive(list, path, candidates, i, sum, target);
		}
		sum[0] -= path.get(path.size() - 1);
		path.remove(path.size() - 1);
	}
}
