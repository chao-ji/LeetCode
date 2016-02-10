import java.util.*;

public class LC40
{
	public static void main(String[] args)
	{
	}

	// 40. Combination Sum II
	static List<List<Integer>> combinationSum2(int[] candidates, int target)
	{
		List<List<Integer>> list = new ArrayList<List<Integer>>();
		Arrays.sort(candidates);
		int[] sum = new int[1];
		for (int i = 0; i < candidates.length; i++)
			if (i == 0 || candidates[i] != candidates[i - 1])
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

		for (int i = start + 1; i < candidates.length; i++)
			if (i == start + 1 || candidates[i] != candidates[i - 1])
			{
				path.add(candidates[i]);
				sum[0] += candidates[i];
				recursive(list, path, candidates, i, sum, target);
			}
		sum[0] -= path.get(path.size() - 1);
		path.remove(path.size() - 1);
	}
}
